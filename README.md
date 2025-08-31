---

# 🧠 Smart Personal Assistant

A lightweight **AI-powered personal assistant** (think *Jarvis*, but simpler).
Built with **Speech Recognition**, **Natural Language Processing (NLP)**, and **System Automation**.

This project demonstrates **AI + system integration skills** by combining voice control with intelligent automation.

---

## 🚀 Features

* 🎙 **Voice Commands** – Hands-free interaction using speech recognition.
* 📧 **Email Automation** – Send and manage emails with natural commands.
* 📰 **Fetch News** – Get the latest news headlines on demand.
* 💻 **PC Control** – Open/close applications, control system settings.
* 🤖 **ChatGPT Integration** – Local integration for conversational responses.
* 🔌 **Extensible** – Easily add new commands and integrations.

---

## 🛠 Tech Stack

* **Python 3.10+**
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – for voice input
* [Transformers (HuggingFace)](https://huggingface.co/transformers/) – NLP processing
* [PyAudio](https://pypi.org/project/PyAudio/) – microphone support
* [smtplib / email](https://docs.python.org/3/library/smtplib.html) – email handling
* [OpenAI API / Local ChatGPT](https://platform.openai.com/) – conversational intelligence
* [OS / Subprocess](https://docs.python.org/3/library/subprocess.html) – system automation

---

## 📂 Project Structure

```bash
smart-personal-assistant/
│── assistant/
│   ├── speech_recognition.py   # Handles microphone input
│   ├── nlp_processor.py        # HuggingFace NLP intent recognition
│   ├── automation.py           # System & app control logic
│   ├── email_client.py         # Send & manage emails
│   ├── news_fetcher.py         # Fetches live news
│   └── chat_integration.py     # ChatGPT / AI conversation
│
│── main.py                     # Entry point
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
```

---

## ⚡ Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/smart-personal-assistant.git
cd smart-personal-assistant
```

2. **Set up virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set environment variables** (e.g., for email & OpenAI)

```bash
export OPENAI_API_KEY="your_api_key"
export EMAIL_USER="your_email@example.com"
export EMAIL_PASS="your_password"
```

---

## ▶️ Usage

Run the assistant:

```bash
python main.py
```

Then simply say:

* *"Send an email to John saying meeting at 3 PM"*
* *"What’s the latest tech news?"*
* *"Open Spotify"*
* *"Chat with me"*

---

## 🌟 Why This Project?

This assistant goes beyond simple chatbots by integrating **AI with real-world automation**:

* Demonstrates **NLP intent classification + action mapping**.
* Showcases **system-level automation (emails, apps, news)**.
* Flexible for **future AI integrations** (smart home, APIs, IoT).

---

## 📌 Future Improvements

* 🔉 Text-to-Speech responses
* 📅 Calendar & scheduling support
* 🏠 Smart home integration (IoT devices)
* 🔐 Voice authentication for security

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss.

---

## 📜 License

This project is licensed under the **MIT License** – free to use, modify, and share.

---

Would you like me to make this **README more recruiter-friendly** (focused on your portfolio) or **developer-friendly** (step-by-step setup & contribution guide)?
