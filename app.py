import streamlit as st
import requests

st.set_page_config(page_title="Chatbot PIPE", page_icon="🤖")
st.title("🤖 Chatbot PIPE - Assistente de Projetos")
st.markdown("Digite sua pergunta e o chatbot responderá com informações sobre o programa PIPE.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Digite sua mensagem...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    url = "http://127.0.0.1:5000/chat"
    response = requests.post(url, json={"message": user_input})

    bot_response = response.json().get("response", "Desculpe, não entendi a pergunta.")

    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    st.rerun()
