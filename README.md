# 🤖 JARVIS – Voice-Controlled Desktop AI Assistant

JARVIS is a Python-powered virtual assistant designed to perform tasks, automate system workflows, and answer complex queries via natural voice commands—much like Amazon's Alexa or Apple's Siri. By integrating real-time web browsing, music playback, and LLM intelligence via Google Gemini, JARVIS turns speech input into instant action.

---

## ✨ Features

* **🎙️ Voice Recognition & TTS:** Listens to speech input and responds back using offline text-to-speech engine (`pyttsx3`).
* **🧠 Gemini AI Intelligence:** Powered by Google's GenAI API for reasoning, answering general questions, and complex tasks.
* **🎵 Custom Music Library:** Play favorite songs or playlists directly via voice triggers.
* **🌐 Web Automation & Search:** Open key websites (YouTube, Google, StackOverflow, etc.) and perform quick web searches instantly.
* **⚡ HTTP Requests Integration:** Fetch real-time data using custom API integrations.

---

## 🛠️ Built With

* **[Python](https://www.python.org/)** - Core Programming Language
* **`speech_recognition`** - Captures audio from the microphone and converts it into text
* **`pyttsx3`** - Text-to-speech conversion library (works offline)
* **`google-genai`** - Google Gemini API integration for dynamic AI capabilities
* **`webbrowser`** - System default browser controller
* **`requests`** - HTTP library to interact with web APIs

---

## 🚀 Getting Started

Follow these instructions to set up and run JARVIS on your local machine.

### Prerequisites

* **Python 3.8+** installed on your system.
* A working **Microphone** and **Speakers**.
* A **Google Gemini API Key** (Get one from [Google AI Studio](https://aistudio.google.com/)).

### Installation

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/jarvis.git](https://github.com/YOUR_USERNAME/jarvis.git)
   cd jarvis
