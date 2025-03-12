import streamlit as st
from transformers import pipeline
from textblob import TextBlob
import random

st.title("Smart Chat Bot")

# Inicializar histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Função para gerar resposta inteligente
def generate_response(user_input):
    if user_input.lower() == "piada":
        jokes = [
            "Por que o livro de matemática ficou triste? Porque tinha muitos problemas!",
            "O que o zero disse para o oito? Belo cinto!",
            "Como o oceano se comunica? Ele manda ondas!"
        ]
        return random.choice(jokes)

    elif user_input.lower() == "ajuda":
        return "Comandos disponíveis:\n- 'piada' para ouvir uma piada\n- 'ajuda' para ver esta mensagem\n- Ou apenas converse comigo!"

    # Analisar sentimento do usuário
    sentiment = TextBlob(user_input).sentiment.polarity

    if sentiment > 0:
        mood = "Parece que você está animado! 😃"
    elif sentiment < 0:
        mood = "Sinto que você pode estar triste. Se precisar de algo, estou aqui! 💙"
    else:
        mood = "Entendi! Vamos continuar conversando. 😊"

    # Gerar resposta usando IA
    chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
    response = chatbot(user_input, max_length=50, do_sample=True)[0]["generated_text"]

    return f"{mood}\n\n{response}"

# Exibir mensagens do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Processar entrada do usuário
if prompt := st.chat_input("Fale comigo!"):
    # Exibir mensagem do usuário
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Gerar resposta inteligente
    response = generate_response(prompt)

    # Exibir resposta do bot
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Salvar resposta no histórico
    st.session_state.messages.append({"role": "assistant", "content": response})
