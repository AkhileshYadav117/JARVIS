# 🤖 JARVIS — Voice-Controlled AI Assistant

<p align="center">
  <b>Your Personal AI Assistant for Voice Commands, AI Answers, Web Automation & Music</b>
</p>

<p align="center">
  🎙️ Voice Recognition • 🧠 Gemini AI • 🌐 Web Search • 🎵 Music • 🔊 Text-to-Speech
</p>

---

## ✨ Features

- 🎙️ **Voice Recognition** — Convert speech into commands
- 🧠 **Google Gemini AI** — Intelligent answers and reasoning
- 🔊 **Text-to-Speech** — Voice responses using `pyttsx3`
- 🎵 **Music Player** — Play songs from your personal library
- 🌐 **Web Automation** — Open websites and perform searches
- 📰 **News API** — Get real-time news
- ⚡ **Lightweight & Fast** — Built with Python

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core Development |
| 🧠 Google Gemini | AI Responses |
| 🎙️ SpeechRecognition | Voice Input |
| 🔊 pyttsx3 | Text-to-Speech |
| 🌐 webbrowser | Web Automation |
| 📡 requests | API Integration |
| 🔐 python-dotenv | Environment Variables |

---

## 📂 Project Structure

```text
JARVIS/
├── main.py
├── client.py
├── musicLibrary.py
├── README.md
├── .gitignore
└── .env              # Local only

🚀 Installation
1. Clone the Repository
git clone https://github.com/AkhileshYadav117/jarvis.git
cd jarvis
2. Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate
3. Install Dependencies
pip install SpeechRecognition pyttsx3 google-genai requests python-dotenv
4. Configure API Keys

Create a .env file in the project directory:

GEMINI_API_KEY=your_gemini_api_key
newsapi=your_newsapi_key
5. Run JARVIS
python main.py
💬 Example Commands
"Open YouTube"
"Search Python tutorials"
"Play music"
"What is Artificial Intelligence?"
"Give me the latest news"
🔐 Security

API keys are stored in .env and excluded from Git using .gitignore.

⚠️ Never commit your API keys or other sensitive credentials to GitHub.

⭐ If you found this project useful, consider giving it a Star.

<p align="center"> <b>🤖 JARVIS — Turning Your Voice Into Action.</b> </p>


