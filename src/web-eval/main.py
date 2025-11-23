import os
from computer import PlaywrightComputer
from agent import BrowserAgent

from dotenv import load_dotenv
load_dotenv()

def main():
    target_url = "https://www.coterie.com/" # Change to your diaper site
    goal = "Add to your shopping cart the Size 1, cheapest diaper bundle"
    
    with PlaywrightComputer(initial_url=target_url) as computer:
        agent = BrowserAgent(computer, goal)
        agent.start()

if __name__ == "__main__":
    main()