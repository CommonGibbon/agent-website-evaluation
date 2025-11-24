from dataclasses import dataclass

@dataclass(frozen=True)
class MetricConfig:
    name: str
    template: str  # A string template using {persona.attribute} syntax