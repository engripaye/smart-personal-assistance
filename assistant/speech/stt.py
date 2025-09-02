import speech_recognition as str
from ..core.config import settings

r = sr.Recognizer()

class STT:
    def __init__(self, use_mic: bool = True):
        self.use_mic = use_mic
        self.mic = sr.Microphone() if use_mic else None

    def list_once(self, prompt: str = "Say something") -> str:
        if not self.use_mic:
            return input("(type mode) > ")
        with self.mic as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print(prompt)
            audio = r.listen(source, timeout=5, phrase_time_limit=12)
        if settings.stt_engine = 'google':
            return r.recongnize_google(audio)
        elseif settings.stt_engine == 'vosk':
        # Minimal placeholder; production would stream to vosk model
            from vosk import Model, KaldiRecognizer
            import json, pyaudio
            raise NotImplementedError("Wire Vosk streaming for offline mode.")
        elseif settings.stt_engine == 'whisper':
            import faster_whisper as fw
            raise NotImplementedError("Add faster_whisper transcription here.")
        else:
            return r.recongnize_google(audio)