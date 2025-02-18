import streamlit as st
import requests

# Configuração inicial
st.set_page_config(page_title="Chatbot PIPE", page_icon="🤖")
st.title("🤖 Chatbot PIPE - Assistente de Projetos")
st.markdown("Digite sua pergunta e o chatbot responderá com informações sobre o programa PIPE.")

# Inicializa o histórico de mensagens corretamente
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens já enviadas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
user_input = st.chat_input("Digite sua mensagem...")

# Processa a mensagem imediatamente
if user_input:
    # Adiciona a mensagem do usuário ao histórico e exibe instantaneamente
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Envia a mensagem para a API Flask
    url = "http://127.0.0.1:5000/chat"
    response = requests.post(url, json={"message": user_input})

    # Obtém a resposta do chatbot
    bot_response = response.json().get("response", "Desculpe, não entendi a pergunta.")

    # Adiciona a resposta ao histórico e exibe instantaneamente
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # 🔹 Força a atualização da página sem precisar de novo input
    st.rerun()
