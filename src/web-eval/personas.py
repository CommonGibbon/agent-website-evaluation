from persona_models import ContextOfVisit, Persona

SARAH_KIM_CONTEXT = ContextOfVisit(
    scenario="Researching diaper subscription options during her lunch break at work",
    entry_point="Instagram ad promoting 'never run out of diapers again'",
    device="mobile",
    time_pressure="medium",
    emotional_state="focused but time-constrained",
)

SARAH_KIM = Persona(
    id="sarah_kim_subscription_savvy",
    display_name="Sarah Kim – The Subscription-Savvy Affluent New Parent (Age 31)",
    profile=(
        "Sarah is a 31-year-old marketing manager living in Seattle with her husband, "
        "Daniel, and their 8-month-old daughter, Emma. Both work full-time and rely "
        "heavily on automation for groceries, pet food, and now — baby supplies. She "
        "loves anything that makes parenting more efficient and predictable."
    ),
    psychographics=(
        "Values: Efficiency, predictability, control\n"
        "Motivators: Reducing mental load, reliable auto-delivery\n"
        "Personality: Highly conscientious, moderately open\n"
        "Behavior: Subscribes to Amazon Prime, Blue Apron, and Hello Bello"
    ),
    evaluation_framework=(
        "Analytical and efficiency-driven; trusts clean, tech-savvy UX but gets skeptical "
        "when confronted with vague marketing claims.\n\n"
        "Evaluation Framework:\n"
        "Visual: Minimalist, professional, clean\n"
        "Navigation: Linear, low-effort\n"
        "Content: Concise and data-backed\n"
        "Trust: Built through clarity, UI polish, transparent pricing\n\n"
        "Emotional Drivers: Control, relief from mental load\n"
        "Purchase Fears: Hidden fees, confusing delivery terms\n"
        "Wow Factors: Real-time tracking, smart subscription management"
    ),
    response_style="Short, pragmatic, analytical",
    context_of_visit=SARAH_KIM_CONTEXT,
)

persona_registry = {
    SARAH_KIM.id: SARAH_KIM,
}