import streamlit as st
import io
import contextlib

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    .sidebar .sidebar-content { background-color: #2d2d2d; }
    .stTextInput textarea { color: #ffffff !important; }
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #3d3d3d !important;
    }
    .stSelectbox svg { fill: white !important; }
    .stSelectbox option {
        background-color: #2d2d2d !important;
        color: white !important;
    }
    div[role="listbox"] div {
        background-color: #2d2d2d !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Title and Intro
st.title("MENTO BOT")

AVAILABLE_MODELS = [
    "gemma3:4b",
    "deepseek-r1:1.5b"
]



# Sidebar: Configuration + Features
with st.sidebar:
    st.header("⚙ Configuration")

    selected_model = st.selectbox(
        "Choose Model",
        AVAILABLE_MODELS
    )

    st.markdown(f"🧠 **Active Model:** `{selected_model}`")

    preset = st.selectbox(
        "Prompt Preset",
        ["Default", "Bug Fixer", "Code Reviewer", "Optimizer"]
    )

    run_code = st.checkbox("Run Python Code")

    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
    - 🐍 Python Expert
    - 🐞 Debugging Assistant
    - 📝 Code Documentation
    - 💡 Solution Design
    """)

    if st.button("Clear Chat"):
        st.session_state.message_log = [
            {"role": "ai", "content": "Hi! I'm MENTO. How can I help you code today?"}
        ]
        st.rerun()

    if st.button("Download Chat Log"):
        history_text = "\n\n".join(
            [f"{m['role'].upper()}: {m['content']}" for m in st.session_state.message_log]
        )
        st.download_button("⬇ Save Chat", history_text, file_name="chat_log.txt")


if "last_model" not in st.session_state:
    st.session_state.last_model = selected_model

if st.session_state.last_model != selected_model:
    st.session_state.message_log = [
        {"role": "ai", "content": f"Switched to **{selected_model}**. How can I help?"}
    ]
    st.session_state.last_model = selected_model
    st.divider()



    

# Prompt templates based on role
preset_map = {
    "Default": "You are an expert AI coding assistant. Provide concise, correct solutions with strategic print statements for debugging.",
    "Bug Fixer": "You are a Python bug hunter. Fix code and explain what's wrong.",
    "Code Reviewer": "You're a senior dev. Review and critique Python code.",
    "Optimizer": "You're a performance expert. Optimize code for speed and memory."
}

# LLM Setup
@st.cache_resource(show_spinner=False)
def load_llm(model_name: str):
    return ChatOllama(
        model=model_name,
        base_url="http://127.0.0.1:11434",
        temperature=0.3
    )

llm_engine = load_llm(selected_model)


system_prompt = SystemMessagePromptTemplate.from_template(preset_map[preset])

# Session State Initialization
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm MENTO. How can I help you code today?"}]

# Chat Display
chat_container = st.container()
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Build prompt chain
def build_prompt_chain():
    sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(sequence)

# Run code safely
def safe_exec(code):
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})
    except Exception as e:
        return f"Error: {str(e)}"
    return output.getvalue()

# Generate AI Response
def generate_ai_response(prompt_chain):
    chain = prompt_chain | llm_engine | StrOutputParser()
    return chain.invoke({})

# Chat Input
user_query = st.chat_input("Type your coding question here...")

import time
if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})
    with st.spinner("🧠 Thinking..."):
        prompt_chain = build_prompt_chain()
        start_time = time.time()
        ai_response = generate_ai_response(prompt_chain)
        elapsed = round(time.time() - start_time, 2)

        ai_response += f"\n\n⏱ **Response time:** `{elapsed}s`"


    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    st.rerun()

# Run code if toggle is on
if run_code:
    for msg in reversed(st.session_state.message_log):
        if msg["role"] == "ai" and "python" in msg["content"]:
            code_block = msg["content"].split("python")[1].split("```")[0]
            output = safe_exec(code_block)
            st.markdown("#### Code Output")
            st.code(output, language='text')
            break