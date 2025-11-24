import sys
from eval_loader import load_eval_cases
from eval_metrics import psychographics_match, eval_framework_match, context_match
from rich.console import Console
from rich.table import Table

from dotenv import load_dotenv
load_dotenv()

def print_results_table(psycho_scores, eval_scores, context_scores):
    console = Console()
    table = Table(title="Evaluation Results")

    table.add_column("Persona", style="cyan", no_wrap=True)
    table.add_column("Psychographics", justify="right", style="magenta")
    table.add_column("Eval Framework", justify="right", style="green")
    table.add_column("Context", justify="right", style="yellow")

    # Get all unique personas
    all_personas = sorted(set(psycho_scores.keys()) | set(eval_scores.keys()) | set(context_scores.keys()))

    for persona in all_personas:
        p_score = psycho_scores.get(persona, "N/A")
        e_score = eval_scores.get(persona, "N/A")
        c_score = context_scores.get(persona, "N/A")
        
        table.add_row(
            str(persona), 
            f"{p_score:.2f}" if isinstance(p_score, (int, float)) else str(p_score),
            f"{e_score:.2f}" if isinstance(e_score, (int, float)) else str(e_score),
            f"{c_score:.2f}" if isinstance(c_score, (int, float)) else str(c_score)
        )

    console.print(table)

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
        
        # 2. Evaluation Framework
        eval_scores = eval_framework_match(cases)
        
        # 3. Context
        context_scores = context_match(cases)
        
        print("\n")
        print_results_table(psycho_scores, eval_scores, context_scores)
        
    else:
        print("Usage: python run_eval.py <path_to_log_directory>")

if __name__ == "__main__":
    main()