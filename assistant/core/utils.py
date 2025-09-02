import pyttsx3

_tts_engine = None

def speak(text: str):
    global _tts_engine
    if _tts_engine is None:
        _tts_engine = ppttsx3.init()
        _tts_engine.setProperty('rate', 185)
    _tts_engine.say(text)
    _tts_engine.runAndWait()