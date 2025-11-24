import os
import time
import json
from google import genai
from google.genai import types
from rich.console import Console
from rich.table import Table
from computer import PlaywrightComputer, EnvState
from persona_models import ContextOfVisit, Persona

class BrowserAgent:
    def __init__(self, computer: PlaywrightComputer, objective: str, persona: Persona, log_path: str, feedback_questions: list[str] = None):
        self.computer = computer
        self.objective = objective
        self.log_path = log_path
        self.feedback_questions = feedback_questions or []
        self.client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        self.prompt = self._build_prompt_block(persona)
        self.history = [
            types.Content(role="user", parts=[
                types.Part(text=self.prompt)
            ])
        ]
        self.action_log = []
        self.feedback_log = []
        self.step_count = 0
        self.start_time = time.time()

    def _build_prompt_block(self, persona: Persona) -> str:
        prompt = f"""
        {persona.build_prompt_block()} \n
        You are currently {persona.context_of_visit.scenario} and you have arrived at this website through {persona.context_of_visit.entry_point}.
        You are feeling {persona.context_of_visit.emotional_state}, with {persona.context_of_visit.time_pressure.value} time pressure.
        You are using a {persona.context_of_visit.device.value} device.
        Your ultimate objective is to {self.objective}
        """

        return prompt 

    def start(self):
        try:
            while True:
                self.step_count += 1
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
                    if part.text: self.action_log.append(f"[AI Thought]: {part.text}")

                # 3. Execute Tool Calls
                function_calls = [p.function_call for p in candidate.content.parts if p.function_call]
                if not function_calls:
                    self.action_log.append("Task Complete or No Action Taken.")
                    break

                function_responses = []
                for call in function_calls:
                    self.action_log.append(f"[Action]: {call.name} {call.args}")
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
            
            # 5. Generate Feedback
            self._generate_feedback()
        finally:
            self._save_logs()

    def _generate_feedback(self):
        """
        Runs the post-task feedback generation by asking the agent the configured questions.
        """
        if not self.feedback_questions:
            return
        
        for question in self.feedback_questions:
            # Add the question to the history as a user prompt
            question_content = types.Content(role="user", parts=[
                types.Part(text=f"FEEDBACK PHASE: {question}")
            ])
            self.history.append(question_content)
            
            # Create filtered history for feedback (text only, no tools/images)
            filtered_history = []
            for content in self.history:
                filtered_parts = []
                for part in content.parts:
                    if part.text:
                        filtered_parts.append(types.Part(text=part.text))
                
                if filtered_parts:
                    filtered_history.append(types.Content(role=content.role, parts=filtered_parts))

            # Ask Gemini for the answer (text only, no tools needed)
            response = self.client.models.generate_content(
                model='gemini-2.5-flash', 
                contents=filtered_history
            )
            # could use a structured response here to increase answer split reliability, but I haven't had issues so far
            answer_candidate = response.candidates[0]
            answer_text = "".join([p.text for p in answer_candidate.content.parts if p.text])
            
            # Save the Q&A
            self.feedback_log.append({
                "question": question,
                "answer": answer_text
            })
            
            # Add answer to history to maintain context
            self.history.append(answer_candidate.content)

    def _save_logs(self):
        duration = time.time() - self.start_time
        log_data = {
            "goal": self.objective,
            "prompt": self.prompt,
            "action_list": self.action_log,
            "feedback": self.feedback_log,
            "total_time": round(duration, 2),
            "total_steps": self.step_count
        }
        
        try:
            with open(self.log_path, 'w') as f:
                json.dump(log_data, f, indent=2)
        except Exception as e:
            print(f"Failed to save logs: {e}")

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