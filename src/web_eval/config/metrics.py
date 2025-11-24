from web_eval.models.metrics import MetricConfig

PSYCHOGRAPHICS_METRIC = MetricConfig(
    name="Psychographics Alignment",
    template="Psychographics: {persona.psychographics}"
)

EVAL_FRAMEWORK_METRIC = MetricConfig(
    name="Evaluation Framework Alignment",
    template="Evaluation Framework: {persona.evaluation_framework}"
)

CONTEXT_METRIC = MetricConfig(
    name="Context of Visit Alignment",
    template="""
    Scenario: {persona.context_of_visit.scenario}
    Entry Point: {persona.context_of_visit.entry_point}
    Time Pressure: {persona.context_of_visit.time_pressure}
    Emotional State: {persona.context_of_visit.emotional_state}
    Device: {persona.context_of_visit.device}
    """
)

METRIC_REGISTRY = [
    PSYCHOGRAPHICS_METRIC,
    EVAL_FRAMEWORK_METRIC,
    CONTEXT_METRIC,
]