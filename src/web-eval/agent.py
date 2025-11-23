import os
import time
from google import genai
from google.genai import types
from rich.console import Console
from rich.table import Table
from computer import PlaywrightComputer, EnvState
from persona_models import ContextOfVisit, Persona

class BrowserAgent:
    def __init__(self, computer: PlaywrightComputer, objective: str, persona: Persona):
        self.computer = computer
        self.objective = objective
        self.client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        self.history = [
            types.Content(role="user", parts=[
                types.Part(text=self._build_prompt_block(persona))
            ])
        ]

    def _build_prompt_block(self, persona: Persona) -> str:
        prompt = f"""
        {persona.build_prompt_block()} \n
        You are currently {persona.context_of_visit.scenario} and you have arrived at this website through {persona.context_of_visit.entry_point}.
        You are feeling {persona.context_of_visit.emotional_state}, with {persona.context_of_visit.time_pressure} time pressure.
        You are using a {persona.context_of_visit.device} device.
        Your ultimate objective is to {self.objective}
        """

        return prompt 

    def start(self):
        print(f"Goal: {self.objective}")
        while True:
            # 1. Ask Gemini what to do next
            response = self.client.models.generate_content(
                model='gemini-2.5-computer-use-preview-10-2025', 
                contents=self.history,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(computer_use=types.ComputerUse(environment=types.Environment.ENVIRONMENT_BROWSER))]
                )
            )

            # 2. Process Response
            candidate = response.candidates[0]
            self.history.append(candidate.content) # Add model thought to history
            
            # Print reasoning (Thinking out loud)
            for part in candidate.content.parts:
                if part.text: print(f"[AI Thought]: {part.text}")

            # 3. Execute Tool Calls
            function_calls = [p.function_call for p in candidate.content.parts if p.function_call]
            if not function_calls:
                print("Task Complete or No Action Taken.")
                break

            function_responses = []
            for call in function_calls:
                print(f"[Action]: {call.name} {call.args}")
                result = self._execute_action(call)
                
                # Format result for Gemini
                function_responses.append(types.FunctionResponse(
                    name=call.name,
                    response={"url": result.url} if isinstance(result, EnvState) else result,
                    parts=[types.FunctionResponsePart(inline_data=types.FunctionResponseBlob(
                        mime_type="image/png", data=result.screenshot
                    ))] if isinstance(result, EnvState) else []
                ))

            # 4. Feed results back to Gemini
            self.history.append(types.Content(role="user", parts=[
                types.Part(function_response=fr) for fr in function_responses
            ]))

    def _execute_action(self, call):
        name = call.name
        args = call.args
        # Map denormalized coords
        w, h = self.computer.screen_size
        x = int(args.get("x", 0) / 1000 * w)
        y = int(args.get("y", 0) / 1000 * h)

        if name == "open_web_browser": return self.computer.get_state()
        if name == "navigate": return self.computer.navigate(args["url"])
        if name == "click_at": return self.computer.click_at(x, y)
        if name == "type_text_at": return self.computer.type_text_at(x, y, args["text"])
        if name == "scroll_document": return self.computer.scroll(args["direction"])
        return {"error": "Unknown command"}