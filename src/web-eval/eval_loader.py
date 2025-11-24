import json
import os
from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from pathlib import Path

from persona_models import Persona
from personas import persona_registry

@dataclass
class EvalCase:
    """
    Represents a single evaluation case, pairing a Persona definition
    with the execution log from a specific run.
    """
    persona: Persona
    log_data: Dict[str, Any]

def load_eval_cases(log_dir: str) -> List[EvalCase]:
    """
    Scans the specified log directory for JSON files.
    Matches JSON filenames (assuming 'persona_id.json') to the persona registry.
    Returns a list of matched EvalCase objects.
    """
    eval_cases = []
    log_path = Path(log_dir)

    if not log_path.exists():
        print(f"Warning: Log directory {log_dir} does not exist.")
        return []

    # Iterate over all json files in the directory
    for file_path in log_path.glob("*.json"):
        try:
            # Assume filename matches persona_id (e.g., sarah_kim.json -> sarah_kim)
            persona_id = file_path.stem
            
            if persona_id not in persona_registry:
                print(f"Skipping {file_path.name}: Persona ID '{persona_id}' not found in registry.")
                continue

            with open(file_path, 'r', encoding='utf-8') as f:
                log_data = json.load(f)

            case = EvalCase(
                persona=persona_registry[persona_id],
                log_data=log_data,
            )
            eval_cases.append(case)
            
        except Exception as e:
            print(f"Error loading {file_path}: {e}")

    return eval_cases
