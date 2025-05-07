import streamlit as st

# URL da imagem no GitHub (versão RAW)
image_url = "https://raw.githubusercontent.com/pita2004/chatbot/main/4616304.png"

# Aplicando o fundo com CSS
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 Chatbot com Fundo do GitHub")
st.write("A imagem de fundo está carregando diretamente do GitHub! 🚀")
