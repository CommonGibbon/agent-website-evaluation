import sys
import csv
import os
from typing import Dict
from rich.console import Console
from rich.table import Table

from web_eval.evaluation.loader import load_eval_cases
from web_eval.evaluation.metrics import run_metric_eval
from web_eval.config.metrics import METRIC_REGISTRY

from dotenv import load_dotenv
load_dotenv()

def print_results_table(all_scores: Dict[str, Dict[str, float]]):
    """
    all_scores structure: { metric_name: { persona_id: score } }
    """
    console = Console()
    table = Table(title="Evaluation Results")

    # Columns
    table.add_column("Persona", style="cyan", no_wrap=True)
    for metric_config in METRIC_REGISTRY:
        table.add_column(metric_config.name, justify="right")

    # Rows
    # Collect all unique persona IDs found in any of the results
    all_personas = set()
    for m_scores in all_scores.values():
        all_personas.update(m_scores.keys())
    
    for persona_id in sorted(all_personas):
        row_data = [str(persona_id)]
        for metric_config in METRIC_REGISTRY:
            score = all_scores.get(metric_config.name, {}).get(persona_id, "N/A")
            formatted_score = f"{score:.2f}" if isinstance(score, (int, float)) else str(score)
            row_data.append(formatted_score)
        
        table.add_row(*row_data)

    console.print(table)

def export_results_csv(all_scores: Dict[str, Dict[str, float]], output_dir: str = "report_data", filename: str = "realism_eval.csv"):
    """
    Exports the evaluation results to a CSV file.
    """
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filepath = os.path.join(output_dir, filename)
    
    # Collect all unique persona IDs
    all_personas = set()
    for m_scores in all_scores.values():
        all_personas.update(m_scores.keys())
    
    with open(filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Header: Persona, followed by each metric name
        header = ["Persona"] + [metric_config.name for metric_config in METRIC_REGISTRY]
        writer.writerow(header)
        
        # Rows
        for persona_id in sorted(all_personas):
            row = [str(persona_id)]
            for metric_config in METRIC_REGISTRY:
                score = all_scores.get(metric_config.name, {}).get(persona_id, "N/A")
                row.append(score) 
            writer.writerow(row)
            
    print(f"Results exported to {filepath}")

def main():
    if len(sys.argv) > 1:
        log_dir = sys.argv[1]
        print(f"Loading logs from: {log_dir}")
        cases = load_eval_cases(log_dir)
        
        if not cases:
            print("No valid cases found. Exiting.")
            sys.exit(1)

        print(f"Found {len(cases)} cases. Starting evaluation...\n")

        # Dictionary to store results: { metric_name: { persona_id: score } }
        all_results = {}

        # Dynamically run all metrics in the registry
        for metric_config in METRIC_REGISTRY:
            scores = run_metric_eval(cases, metric_config)
            all_results[metric_config.name] = scores

        print("\n")
        print_results_table(all_results)
        export_results_csv(all_results)
        
    else:
        print("Usage: python run_evaluation.py <path_to_log_directory>")

if __name__ == "__main__":
    main()