import streamlit as st
import pandas as pd

# Tentar carregar o dataset e tratar possíveis erros
try:
    df = pd.read_csv("dataset.csv", encoding="utf-8")
except FileNotFoundError:
    df = pd.DataFrame(columns=["pergunta", "resposta"])
    st.warning("⚠️ O ficheiro de dados não foi encontrado. A criar um novo vazio.")
except Exception as e:
    st.error(f"Erro ao carregar o ficheiro de dados: {e}")
    df = pd.DataFrame(columns=["pergunta", "resposta"])

# Guardar dataset na sessão do Streamlit
if "df" not in st.session_state:
    st.session_state.df = df

# Função para obter resposta com base em palavras-chave
def obter_resposta(pergunta):
    pergunta = pergunta.lower()
    melhor_resposta = "Não encontrei uma solução para esse problema. Tenta reformular a pergunta."
    maior_relevância = 0

    for _, row in st.session_state.df.iterrows():
        palavras_chave = row["pergunta"].lower().split()
        relevância = sum(1 for palavra in palavras_chave if palavra in pergunta)

        if relevância > maior_relevância:
            maior_relevância = relevância
            melhor_resposta = row["resposta"]

    return melhor_resposta

# Função para adicionar nova pergunta e resposta ao dataset
def adicionar_pergunta_resposta(nova_pergunta, nova_resposta):
    novo_dado = pd.DataFrame({"pergunta": [nova_pergunta], "resposta": [nova_resposta]})
    st.session_state.df = pd.concat([st.session_state.df, novo_dado], ignore_index=True)
    st.session_state.df.to_csv("dataset.csv", index=False, encoding="utf-8")  # Guardar no ficheiro
    st.success("Nova pergunta e resposta adicionadas e guardadas no ficheiro de dados!")

# Interface no Streamlit
st.title("💬 Chatbot de Apoio Técnico")
st.write("Escreve o teu problema e eu tentarei ajudar!")

# Caixa de texto para inserir o problema
pergunta = st.text_input("Qual é o teu problema?")

# Caixa de texto para adicionar uma nova pergunta e resposta
st.subheader("Adicionar Nova Pergunta e Resposta")
nova_pergunta = st.text_input("Nova Pergunta")
nova_resposta = st.text_area("Nova Resposta")

if st.button("Adicionar"):
    if nova_pergunta and nova_resposta:
        adicionar_pergunta_resposta(nova_pergunta, nova_resposta)
    else:
        st.warning("⚠️ Preenche ambos os campos antes de adicionar.")

if pergunta:
    resposta = obter_resposta(pergunta)
    st.write("🔧 **Solução:**", resposta)

if pergunta:
    resposta = obter_resposta(pergunta)
    st.write("🔧 Solução:", resposta)


