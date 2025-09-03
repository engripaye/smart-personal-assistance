from abc import ABC, abstractmethod


class Skill(ABC):
    @abstractmethod
    def run(self, text: str, **kwargs) -> str:
    ...