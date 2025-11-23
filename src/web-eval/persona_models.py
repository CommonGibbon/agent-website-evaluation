from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class ContextOfVisit:
    """
    Structured representation of the 'Context of Visit' block.

    We keep the semantic fields but can still reconstruct
    a JSON string that matches the original meaning.
    """
    scenario: str
    entry_point: str
    device: str
    time_pressure: str
    emotional_state: str

@dataclass(frozen=True)
class Persona:
    """
    A website-evaluating persona.

    Design goals:
    - Preserve original wording of persona fields.
    - Avoid duplicating text across attributes.
    - Provide just enough structure to plug into prompts.
    """
    id: str
    display_name: str

    profile: str
    psychographics: str

    evaluation_framework: str
    response_style: str  
    context_of_visit: ContextOfVisit

    def build_prompt_block(self) -> str:
        """
        Return a prompt snippet for the LLM that embeds this persona verbatim
        (using the original wording in each field).
        """
        lines = [
            f"--- PERSONA: {self.display_name} ---",
            "",
            "Profile:",
            self.profile.strip(),
            "",
            "Psychographics:",
            self.psychographics.strip(),
            "",
            "Cognitive & Behavioral Style and Evaluation Framework:",
            self.evaluation_framework.strip(),
            "",
            "Response Style:",
            self.response_style.strip(),
            "",
            "When evaluating the website, stay fully in character as this persona.",
        ]
        return "\n".join(lines)