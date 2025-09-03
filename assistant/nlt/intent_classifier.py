from transformers import pipeline
import re


# Zero-shot classification with candidate labels
labels = [
    "send_email",
    "get_news",
    "open_app",
    "chat",
]


_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


INTENT_PATTERNS = {
    "send_email": r"(?:send|compose|draft).*email|email (?:to )?(?P<to>\S+@\S+)",
    "get_news": r"(?:news|headlines|what's happening)(?: about (?P<topic>[\w\s]+))?",
    "open_app": r"(?:open|launch|start) (?P<app>[\w\s]+)",
    "chat": r"(?:ask|explain|what is|who is|how do I|tell me).*",
}


class Intent:
    def __init__(self, name: str, score: float, slots: dict):
    self.name, self.score, self.slots = name, score, slots


class IntentClassifier:
    def classify(self, text: str) -> Intent:
# heuristic slots first
slots = {}
for name, pattern in INTENT_PATTERNS.items():
    m = re.search(pattern, text, re.IGNORECASE)
if m:
    slots.update({k:v for k,v in m.groupdict().items() if v})
res = _classifier(text, candidate_labels=labels)
name = res['labels'][0]
score = res['scores'][0]
return Intent(name=name, score=float(score), slots=slots)