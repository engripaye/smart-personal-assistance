from typing import Dict, Any
from utils import speak


class Router:
    def __init__(self, skills: Dict[str, Any]):
        self.skills = skills  # {intent: skill_instance}

    def handle(self, intent: str, text: str, slots: dict) -> str:
        skill = self.skills.get(intent)
        if not skill:
            return "I don't have a skill for that yet."
        try:
            result = skill.run(text=text, **slots)
            if result:
                speak(result)
            return result or "Done."
        except Exception as e:
            msg = f"Something went wrong. {e}"
            speak(msg)
            return msg
