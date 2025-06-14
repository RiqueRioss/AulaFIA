import streamlit as st
import google.generativeai as genai

# Configura a API key do Gemini
genai.configure(api_key="AIzaSyCypmU70v-JMILExV16mab91fe5ppY5xIo")

# Carrega o modelo
model = genai.GenerativeModel("gemini-2.0-flash")

def gerar_recomendacoes(classificacao):
    prompt = (
        f"Recomende 5 filmes que sejam apropriados para a classificação etária {classificacao}. "
        "Para cada filme, diga o nome, uma pequena sinopse e o ano de lançamento."
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar recomendações: {str(e)}"

# Título do site
st.title("🎬 Recomendador de Filmes por Classificação Etária")

# Opções de classificação etária
classificacoes = [
    "Livre",
    "10 anos",
    "12 anos",
    "14 anos",
    "16 anos",
    "18 anos"
]

# Seleção da classificação
escolha = st.selectbox("Escolha a classificação etária:", classificacoes)

# Botão de gerar recomendação
if st.button("Recomendar Filmes"):
    with st.spinner("Buscando recomendações..."):
        resultado = gerar_recomendacoes(escolha)
        st.subheader("🎥 Recomendações de Filmes:")
        st.write(resultado)
