from web_eval.models.metrics import MetricConfig, OutputType

PSYCHOGRAPHICS_METRIC_ACTIONS = MetricConfig(
    name="Psychographics Alignment (Actions)",
    template="Psychographics: {persona.psychographics}",
    output_type=OutputType.ACTIONS
)

EVAL_FRAMEWORK_METRIC_ACTIONS = MetricConfig(
    name="Evaluation Framework Alignment (Actions)",
    template="Evaluation Framework: {persona.evaluation_framework}",
    output_type=OutputType.ACTIONS
)

CONTEXT_METRIC_ACTIONS = MetricConfig(
    name="Context of Visit Alignment (Actions)",
    template="""
    Scenario: {persona.context_of_visit.scenario}
    Entry Point: {persona.context_of_visit.entry_point}
    Time Pressure: {persona.context_of_visit.time_pressure}
    Emotional State: {persona.context_of_visit.emotional_state}
    Device: {persona.context_of_visit.device}
    """,
    output_type=OutputType.ACTIONS
)

RESPONSE_STYLE_METRIC_ACTIONS = MetricConfig(
    name="Response Style Alignment (Actions)",
    template="Response Style: {persona.response_style}",
    output_type=OutputType.ACTIONS
)

PSYCHOGRAPHICS_METRIC_FEEDBACK = MetricConfig(
    name="Psychographics Alignment (Feedback)",
    template="Psychographics: {persona.psychographics}",
    output_type=OutputType.FEEDBACK
)

EVAL_FRAMEWORK_METRIC_FEEDBACK = MetricConfig(
    name="Evaluation Framework Alignment (Feedback)",
    template="Evaluation Framework: {persona.evaluation_framework}",
    output_type=OutputType.FEEDBACK
)

CONTEXT_METRIC_FEEDBACK = MetricConfig(
    name="Context of Visit Alignment (Feedback)",
    template="""
    Scenario: {persona.context_of_visit.scenario}
    Entry Point: {persona.context_of_visit.entry_point}
    Time Pressure: {persona.context_of_visit.time_pressure}
    Emotional State: {persona.context_of_visit.emotional_state}
    Device: {persona.context_of_visit.device}
    """,
    output_type=OutputType.FEEDBACK
)

RESPONSE_STYLE_METRIC_FEEDBACK = MetricConfig(
    name="Response Style Alignment (Feedback)",
    template="Response Style: {persona.response_style}",
    output_type=OutputType.FEEDBACK
)

METRIC_REGISTRY = [
    PSYCHOGRAPHICS_METRIC_ACTIONS,
    EVAL_FRAMEWORK_METRIC_ACTIONS,
    CONTEXT_METRIC_ACTIONS,
    RESPONSE_STYLE_METRIC_ACTIONS,
    PSYCHOGRAPHICS_METRIC_FEEDBACK,
    EVAL_FRAMEWORK_METRIC_FEEDBACK,
    CONTEXT_METRIC_FEEDBACK,
    RESPONSE_STYLE_METRIC_FEEDBACK,
]
