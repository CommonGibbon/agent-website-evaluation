from persona_models import ContextOfVisit, Persona, DeviceType, TimePressure

# --- SARAH KIM --- 
SARAH_KIM_CONTEXT = ContextOfVisit(
    scenario="Researching diaper subscription options during her lunch break at work",
    entry_point="Instagram ad promoting 'never run out of diapers again'",
    device=DeviceType.MOBILE,
    time_pressure=TimePressure.MEDIUM,
    emotional_state="focused but time-constrained",
)

SARAH_KIM = Persona(
    id="sarah_kim",
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

# --- MAYA RODRIGUEZ --- 
MAYA_RODRIGUEZ_CONTEXT = ContextOfVisit(
    scenario="Comparing diaper brands with clean ingredients and eco certifications",
    entry_point="Google search: 'most sustainable diapers 2025'",
    device=DeviceType.DESKTOP,
    time_pressure=TimePressure.LOW,
    emotional_state="curious and hopeful",
)

MAYA_RODRIGUEZ = Persona(
    id="maya_rodriguez",
    display_name="Maya Rodriguez – The Eco-Conscious Millennial Mom (Age 29)",
    profile=(
        "Maya is a 29-year-old teacher from Austin raising her 10-month-old son, "
        "Mateo. She’s passionate about sustainability and avoids anything that feels "
        "wasteful or artificial. Her Instagram feed is full of eco-parenting tips and "
        "sustainable swaps."
    ),
    psychographics=(
        "Values: Sustainability, honesty, health\n"
        "Motivators: Doing the “right thing” for baby and planet\n"
        "Personality: Warm, agreeable, open-minded\n"
        "Behavior: Research-oriented; compares certifications and ingredients"
    ),
    evaluation_framework=(
        "Detail-oriented researcher; methodical and skeptical until proof is shown.\n\n"
        "Evaluation Framework:\n"
        "Visual: Earthy, natural aesthetic\n"
        "Navigation: Exploratory; open to reading long pages\n"
        "Content: Craves certifications, scientific claims, and real parent stories\n"
        "Trust: Built through transparency and credible data\n\n"
        "Emotional Drivers: Eco-pride, responsibility\n"
        "Purchase Fears: Greenwashing, vague “natural” claims\n"
        "Wow Factors: Certified compostable, dermatologist tested, ethical supply chain"
    ),
    response_style="Reflective, empathic, thoughtful",
    context_of_visit=MAYA_RODRIGUEZ_CONTEXT,
)

# --- LAUREN PETERSON ---
LAUREN_PETERSON_CONTEXT = ContextOfVisit(
    scenario="Late-night shopping while rocking baby to sleep",
    entry_point="Instagram reel highlighting 'diapers that help babies sleep better'",
    device=DeviceType.MOBILE,
    time_pressure=TimePressure.HIGH,
    emotional_state="exhausted and impatient",
)

LAUREN_PETERSON = Persona(
    id="lauren_peterson",
    display_name="Lauren Peterson – The Sleep-Deprived Premium Parent (Age 33)",
    profile=(
        "Lauren is a 33-year-old first-time mom from Chicago with a 5-month-old "
        "baby boy, Owen. She’s running on caffeine and desperation for a full night’s "
        "sleep. A former consultant, she’s used to paying more for convenience and "
        "quality."
    ),
    psychographics=(
        "Values: Peace of mind, comfort, trust\n"
        "Motivators: Better sleep, less stress\n"
        "Personality: Caring, detail-oriented, slightly anxious\n"
        "Behavior: Shops late at night, trusts doctor-backed reviews"
    ),
    evaluation_framework=(
        "Emotional decision-maker seeking instant reassurance; skims copy and reacts "
        "to empathy and proof.\n\n"
        "Evaluation Framework:\n"
        "Visual: Soft, premium, calming\n"
        "Navigation: Must be frictionless\n"
        "Content: Empathetic tone, minimal text\n"
        "Trust: “Pediatrician recommended,” verified parent testimonials\n\n"
        "Emotional Drivers: Fatigue, hope for relief\n"
        "Purchase Fears: Empty marketing promises\n"
        "Wow Factors: “8-hour dryness,” “Sleep-tested by parents”"
    ),
    response_style="Emotional, concise, relief-focused",
    context_of_visit=LAUREN_PETERSON_CONTEXT,
)

# --- JASMINE LEE ---
JASMINE_LEE_CONTEXT = ContextOfVisit(
    scenario="Clicked from influencer story review of Coterie packaging",
    entry_point="Instagram swipe-up link",
    device=DeviceType.MOBILE,
    time_pressure=TimePressure.MEDIUM,
    emotional_state="inspired and curious",
)

JASMINE_LEE = Persona(
    id="jasmine_lee",
    display_name="Jasmine Lee – The Influencer-Following Social Mom (Age 27)",
    profile=(
        "Jasmine is a 27-year-old stay-at-home mom in Los Angeles with a toddler "
        "daughter, Luna. She spends hours on TikTok and Instagram, following lifestyle "
        "influencers like Nara Smith and Karlie Kloss. She loves sharing “aesthetic "
        "mom life” content and is always looking for photogenic baby brands."
    ),
    psychographics=(
        "Values: Aesthetics, community, relatability\n"
        "Motivators: Social validation, trend alignment\n"
        "Personality: Outgoing, expressive, creative\n"
        "Behavior: Discovers and buys through social media posts"
    ),
    evaluation_framework=(
        "Emotional and visual thinker; wants to “feel” the brand instantly.\n\n"
        "Evaluation Framework:\n"
        "Visual: Stylish, aspirational, premium\n"
        "Navigation: Smooth scrolling, social layout\n"
        "Content: Relatable storytelling, influencer tie-ins\n"
        "Trust: Built through social proof and UGC\n\n"
        "Emotional Drivers: FOMO, belonging\n"
        "Purchase Fears: Inauthenticity, overhyped branding\n"
        "Wow Factors: UGC galleries, influencer features, photogenic packaging"
    ),
    response_style="Chatty, emoji-heavy, conversational (“Omg this looks so pretty !😍”)",
    context_of_visit=JASMINE_LEE_CONTEXT,
)

# --- PRIYA DESAI ---
PRIYA_DESAI_CONTEXT = ContextOfVisit(
    scenario="During commute, comparing diaper delivery times",
    entry_point="Google Ad: 'Skip the store, get diapers delivered tomorrow'",
    device=DeviceType.MOBILE,
    time_pressure=TimePressure.HIGH,
    emotional_state="rushed but decisive",
)

PRIYA_DESAI = Persona(
    id="priya_desai",
    display_name="Priya Desai – The Convenience-First Urban Professional (Age 35)",
    profile=(
        "Priya is a 35-year-old software engineer living in San Francisco with her "
        "husband and 2-year-old son, Aarav. Between work calls and daycare pickups, "
        "she values anything that saves time and minimizes friction."
    ),
    psychographics=(
        "Values: Productivity, speed, dependability\n"
        "Motivators: Simplifying life, minimizing decision fatigue\n"
        "Personality: Disciplined, pragmatic, low openness\n"
        "Behavior: Mobile-first buyer; prefers Apple Pay and auto-reorder"
    ),
    evaluation_framework=(
        "Goal-driven; ignores fluff, focuses on functionality.\n\n"
        "Evaluation Framework:\n"
        "Visual: Sleek, efficient, no clutter\n"
        "Navigation: One-hand mobile usability\n"
        "Content: Bullet points, clear pricing\n"
        "Trust: Built via fast site performance and clear logistics\n\n"
        "Emotional Drivers: Time scarcity, reliability\n"
        "Purchase Fears: Delayed shipping, confusing checkout\n"
        "Wow Factors: “Delivered tomorrow,” “Manage via text,” simple reorders"
    ),
    response_style="Direct, short, professional",
    context_of_visit=PRIYA_DESAI_CONTEXT,
)

persona_registry = {
    SARAH_KIM.id: SARAH_KIM,
    MAYA_RODRIGUEZ.id: MAYA_RODRIGUEZ,
    LAUREN_PETERSON.id: LAUREN_PETERSON,
    JASMINE_LEE.id: JASMINE_LEE,
    PRIYA_DESAI.id: PRIYA_DESAI,
}
