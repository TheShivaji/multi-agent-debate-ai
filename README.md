# 🔥 Multi-Agent AI Debate System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)

> ⚡ A real-time multi-agent AI debate system powered by local LLMs and Python streaming.

---

## 📸 Demo

<p align="center">
  <img src="./assets/demo.png" alt="Demo UI" width="800"/>
</p>

---

## 🚀 Features

- 🧠 **Multi-Agent Architecture:** Features 3 distinct personas (FOR / AGAINST / JUDGE).
- 🔄 **Dynamic Context:** Works seamlessly with any user-provided topic.
- ⚡ **Real-Time Streaming:** Built with Python generators (`yield`) for low-latency token-by-token output.
- 💬 **State Management:** Maintains shared conversation memory across multiple agent calls.
- 🖥️ **Interactive UI:** Powered by Gradio's `ChatInterface`.
- 🧪 **100% Local & Private:** Runs entirely locally using Ollama.

---

## 🏗️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core Backend & Logic |
| **Ollama** | Local LLM Engine (`llama3.2`) |
| **Gradio** | Frontend Chat Interface |
| **OpenAI SDK** | Standardized API wrapper for local models |

---

## 🧠 How It Works

The system passes the context sequentially through different agents to simulate a live debate:

```text
[User Input: Topic] 
       ↓
(Prompt Builder: Injects Chat History)
       ↓
🟢 FOR Agent (Streams response & saves to history)
       ↓
🔴 AGAINST Agent (Reads history, streams counter-argument)
       ↓
⚖️ JUDGE Agent (Evaluates both sides, streams verdict)
       ↓
[Final Debate Output]
```

---

## 📦 Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/TheShivaji/llm-multi-agent-debate.git](https://github.com/TheShivaji/llm-multi-agent-debate.git)
cd llm-multi-agent-debate
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Start the local LLM (Ollama):**
Ensure Ollama is installed on your system, then run:
```bash
ollama run llama3.2
```

**4. Launch the application:**
```bash
python app.py
```

---

## 🧪 Example Topics to Try

- *Is AI dangerous for software engineers?*
- *Remote work vs. In-office work.*
- *Should college degrees be mandatory in tech?*

---

## 📁 Project Structure

```text
llm-multi-agent-debate/
├── app.py               # Main Gradio application & AI logic
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore rules
└── assets/
    └── demo.png         # UI preview image
```

---

## 👨‍💻 Author

Built as a proof-of-concept for AI Engineering and LLM Orchestration 🚀
