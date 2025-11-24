from dataclasses import dataclass
from enum import Enum

class OutputType(str, Enum):
    ACTIONS = "actions"
    FEEDBACK = "feedback"

@dataclass(frozen=True)
class MetricConfig:
    name: str
    template: str  # A string template using {persona.attribute} syntax
    output_type: OutputType # determines whether we'll compare the persona to the actions taken by the agent or the feedback given by the agent
