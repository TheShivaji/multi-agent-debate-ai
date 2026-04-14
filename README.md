# 🔥 Multi-Agent AI Debate System 🤖⚔️

### ⚡ Real-Time Multi-Agent Reasoning powered by Local LLMs

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)

> 🧠 A production-style **multi-agent AI system** that simulates real-time debates using local LLMs with streaming responses.

---

## 🎯 Why This Project?

Most AI apps rely on a **single LLM response**.
This project demonstrates **Agentic AI orchestration**, where multiple agents:

* Think independently 🧠
* Share context 🔄
* Compete + evaluate ⚔️

👉 Result: **More structured, intelligent, and explainable outputs**

---

## 📸 Demo

<p align="center">
  <img src="./assets/demo1.png" width="800"/>
  <img src="./assets/demo2.png" width="800"/>
  <img src="./assets/demo3.png" width="800"/>
</p>

---

## 🚀 Core Features

### 🧠 Multi-Agent Architecture

* 🟢 **FOR Agent** → Supports the argument
* 🔴 **AGAINST Agent** → Challenges the argument
* ⚖️ **JUDGE Agent** → Evaluates both sides

---

### ⚡ Real-Time Streaming

* Token-by-token output using Python `yield`
* Low latency & live experience

---

### 🔄 Shared Context System

* Maintains memory across agents
* Enables coherent multi-step reasoning

---

### 🖥️ Interactive UI

* Built with Gradio `ChatInterface`
* Clean and responsive chat layout

---

### 🔒 Fully Local & Private

* Runs on **Ollama (llama3.2)**
* No external API calls
* Complete data privacy

---

## 📌 Highlights

✔ Multi-agent orchestration system
✔ Real-time streaming architecture
✔ Local LLM execution (privacy-first)
✔ Context-aware reasoning across agents
✔ Clean modular design

---

## 🏗️ System Architecture

```text
User Input (Topic)
        ↓
Prompt Builder (Injects History)
        ↓
🟢 FOR Agent (Argument Generation)
        ↓
🔴 AGAINST Agent (Counter Argument)
        ↓
⚖️ JUDGE Agent (Evaluation & Verdict)
        ↓
Final Output (Structured Debate)
```

---

## 🛠️ Tech Stack

| Layer        | Technology                 |
| ------------ | -------------------------- |
| 🐍 Backend   | Python                     |
| 🧠 LLM       | Ollama (llama3.2)          |
| 🎨 UI        | Gradio                     |
| 🔌 API Layer | OpenAI SDK (Local Wrapper) |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash id="clone1"
git clone https://github.com/TheShivaji/llm-multi-agent-debate.git
cd llm-multi-agent-debate
```

### 2️⃣ Install Dependencies

```bash id="install1"
pip install -r requirements.txt
```

### 3️⃣ Start Local LLM (Ollama)

```bash id="ollama1"
ollama run llama3.2
```

---

### 4️⃣ Run the App

```bash id="run1"
python app.py
```

---

## 🧪 Example Topics

Try testing the system with:

* Is AI dangerous for software engineers?
* Remote work vs in-office work
* Should college degrees be mandatory in tech?
* Is open-source better than proprietary software?

---

## 📁 Project Structure

```text
llm-multi-agent-debate/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
    ├── demo1.png
    ├── demo2.png
    └── demo3.png
```

---

## 🚀 Future Improvements

* 🧠 Add memory persistence (Redis / DB)
* 🎭 Add dynamic agent personalities
* 🌐 Deploy with Docker + GPU support
* 📊 Debate scoring metrics

---

## 👨‍💻 Author

### **Shivaji Jagdale**

🚀 Full-Stack Developer | 🤖 AI Engineer | ⚡ Agentic Systems Builder

* 🧠 Building **Multi-Agent AI Systems & GenAI Apps**
* ⚡ Focused on **LLM orchestration & real-time systems**
* 🔐 Strong foundation in **backend & scalable architecture**
* 💡 Passionate about solving complex problems with AI

---

## 🌐 Connect with Me

* 🐙 GitHub: https://github.com/TheShivaji
* 💼 LinkedIn: https://linkedin.com/in/your-link
* 📧 Email: [your-email@example.com](mailto:your-email@example.com)

---

## ⭐ Support

If you found this project useful:

⭐ Star this repo
🍴 Fork it
📢 Share it

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

---


