# 🔥 Multi-Agent AI Debate System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)

> ⚡ A real-time multi-agent AI debate system powered by local LLMs

---

## 📸 Demo

<p align="center">
  <img src="./assets/demo.png" alt="Demo UI" width="800"/>
</p>

---

## 🚀 Features

- 🧠 Multi-agent debate system (FOR / AGAINST / JUDGE)
- 🔄 Works with any topic
- ⚡ Real-time streaming using `yield`
- 💬 Shared conversation memory
- 🖥️ Gradio UI
- 🧪 Runs locally with Ollama

---

## 🏗️ Tech Stack

| Tech | Use |
|------|-----|
| Python | Backend |
| Ollama | LLM |
| Gradio | UI |
| OpenAI SDK | API wrapper |

---

## 🧠 How It Works


User Input
↓
Prompt Builder
↓
FOR Agent
↓
AGAINST Agent
↓
Judge Agent
↓
Streaming Output


---

## 📦 Installation

git clone https://github.com/your-username/llm-multi-agent-debate.git
cd llm-multi-agent-debate
pip install -r requirements.txt
ollama run llama3.2
python main.py

##🧪 Example Topics

Is AI dangerous?
Remote work vs office work
Should college be mandatory?

##📁 Project Structure
multi-agent-debate-ai/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
    └── demo.png

##👨‍💻 Author

Built as a learning project for AI Engineering 🚀
