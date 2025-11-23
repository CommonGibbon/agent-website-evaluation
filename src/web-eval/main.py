import os
from computer import PlaywrightComputer
from agent import BrowserAgent
from personas import persona_registry

from dotenv import load_dotenv
load_dotenv()

def main():
    target_url = "https://www.coterie.com/" # Change to your diaper site
    objective = "Add to your shopping cart the Size 1, cheapest diaper bundle"
    for persona_name, persona in persona_registry.items():
        print("Starting persona:", persona_name)
        with PlaywrightComputer(initial_url=target_url) as computer:
            agent = BrowserAgent(computer, objective, persona)
            agent.start()

if __name__ == "__main__":
    main()