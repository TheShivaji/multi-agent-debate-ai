from openai import OpenAI
import gradio as gr

# -----------------------------
# OLLAMA SETUP
# -----------------------------
ollama = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

model = "llama3.2:latest"

# -----------------------------
# AGENTS 
# -----------------------------
agents = [
    {"name": "Agent 1", "role": "FOR"},
    {"name": "Agent 2", "role": "AGAINST"},
    {"name": "Judge", "role": "JUDGE"}
]

chat_history = []

# -----------------------------
# STREAMING AI FUNCTION
# -----------------------------
def ai_stream(prompt):
    stream = ollama.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a debate assistant"},
            {"role": "user", "content": prompt}
        ],
        stream=True   # 🔥 IMPORTANT
    )

    full_response = ""

    for chunk in stream:
        if chunk.choices[0].delta.content:
            token = chunk.choices[0].delta.content
            full_response += token
            yield token   # 👈 token by token

    return full_response


# -----------------------------
# PROMPT
# -----------------------------
def make_prompt(agent, topic):
    prompt = f"Topic: {topic}\n\n"
    

    if len(chat_history) > 0:
        prompt += "Debate so far:\n"
        
        for msg in chat_history:
            prompt += msg["role"] + ": " + msg["content"] + "\n"
            

    if agent["role"] == "FOR":
        role = "You strongly SUPPORT the topic."
    elif agent["role"] == "AGAINST":
        role = "You strongly OPPOSE the topic."
    else:
        role = "You are a neutral judge."

    prompt += f"""
You are {agent['name']}.

{role}

Rules:
- Counter previous arguments
- Be direct
- Do not repeat

Start now:
"""
    
    return prompt


# -----------------------------
# MAIN FUNCTION (STREAMING UI)
# -----------------------------
def run_debate(topic, history):
    global chat_history
    chat_history = []
    

    output = ""
    for agent in agents:
        prompt = make_prompt(agent, topic)
        
        # show agent name first
        output += f"\n\n### {agent['name']}:\n"
        print("agents in ",output)
        yield output

        response_text = ""

        # 🔥 STREAM LOOP
        for token in ai_stream(prompt):
            response_text += token
            output += token
            yield output   # live update

        # save final response
        chat_history.append({
            "role": agent["name"],
            "content": response_text
        })
   

# -----------------------------
# UI
# -----------------------------
app = gr.ChatInterface(fn=run_debate)

app.launch()