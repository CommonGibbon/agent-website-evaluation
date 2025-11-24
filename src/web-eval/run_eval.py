import sys
from eval_loader import load_eval_cases
from eval_metrics import psychographics_match, eval_framework_match, context_match

from dotenv import load_dotenv
load_dotenv()

def main():
    if len(sys.argv) > 1:
        log_dir = sys.argv[1]
        print(f"Loading logs from: {log_dir}")
        cases = load_eval_cases(log_dir)
        
        if not cases:
            print("No valid cases found. Exiting.")
            sys.exit(1)

        print(f"Found {len(cases)} cases. Starting evaluation...\n")

        # 1. Psychographics
        psycho_scores = psychographics_match(cases)
        print("Psychographics Scores:", psycho_scores)
        
        # 2. Evaluation Framework
        eval_scores = eval_framework_match(cases)
        print("Evaluation Framework Scores:", eval_scores)
        
        # 3. Context
        context_scores = context_match(cases)
        print("Context Scores:", context_scores)
        
    else:
        print("Usage: python run_eval.py <path_to_log_directory>")

if __name__ == "__main__":
    main()