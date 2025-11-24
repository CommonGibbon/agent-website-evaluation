import os
import json
from datetime import datetime
from web_eval.core.computer import PlaywrightComputer
from web_eval.core.agent import BrowserAgent
from web_eval.config.personas import persona_registry
from web_eval.config.questions import feedback_questions

from dotenv import load_dotenv
load_dotenv()

def main():
    # Create timestamped log directory
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_dir = os.path.join("logs", timestamp)
    os.makedirs(log_dir, exist_ok=True)

    target_url = "https://www.coterie.com/" # Change to your diaper site
    objective = "Add to your shopping cart the Size 1, cheapest diaper bundle"
    for persona_name, persona in persona_registry.items():
        print(f"Starting persona: {persona_name}")
        
        # Define JSON output path
        log_path = os.path.join(log_dir, f"{persona.id}.json")
        
        # Configure computer based on persona's device preference
        device_type = persona.context_of_visit.device
        
        with PlaywrightComputer(initial_url=target_url, device_type=device_type) as computer:
            agent = BrowserAgent(computer, objective, persona, log_path, feedback_questions=feedback_questions)
            agent.start()

if __name__ == "__main__":
    main()