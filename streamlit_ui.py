from doc_qa_with_memory import agent_executor
import streamlit as st

st.set_page_config(layout="wide")
st.title("💬 ChatEnzyme")
st.caption("🚀 A chatbot about enzymes")
with st.sidebar:
    st.title("📚 Chatbot about enzymes")
    "💻 [View the source code](https://github.com/JinyuanSun/ChatEnzyme)"

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if len(st.session_state["messages"]) > 0:
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.spinner("Thinking..."):
        response = agent_executor({"input": prompt})
        msg = response["output"]

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)