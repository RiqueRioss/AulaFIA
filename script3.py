import streamlit as st
import google.generativeai as genai

# Configura a API key do Gemini
genai.configure(api_key="AIzaSyCypmU70v-JMILExV16mab91fe5ppY5xIo")

# Carrega o modelo
model = genai.GenerativeModel("gemini-2.0-flash")

# Função para gerar recomendações com base na classificação, gênero e filmes favoritos
def gerar_recomendacoes(classificacao, genero, filmes_favoritos):
    if filmes_favoritos.strip():
        prompt = (
            f"Recomende 5 filmes semelhantes a estes: {filmes_favoritos}. "
            f"As recomendações devem ser do gênero {genero} e apropriadas para a classificação etária {classificacao}. "
            "Para cada filme, diga o nome, uma pequena sinopse e o ano de lançamento."
        )
    else:
        prompt = (
            f"Recomende 5 filmes do gênero {genero} que sejam apropriados para a classificação etária {classificacao}. "
            "Para cada filme, diga o nome, uma pequena sinopse e o ano de lançamento."
        )

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar recomendações: {str(e)}"

# Título do site
st.title("🎬 Recomendador de Filmes por Idade e Gênero")

# Opções de classificação etária
classificacoes = [
    "Livre",
    "10 anos",
    "12 anos",
    "14 anos",
    "16 anos",
    "18 anos"
]

# Opções de gênero
generos = [
    "Aventura",
    "Terror",
    "Ficção Científica",
    "Comédia",
    "Drama",
    "Animação",
    "Outros"
]

# Seleção da classificação etária
escolha_classificacao = st.selectbox("Escolha a classificação etária:", classificacoes)

# Seleção do gênero
escolha_genero = st.selectbox("Escolha o gênero do filme:", generos)

# Campo opcional de filmes favoritos
filmes_favoritos = st.text_area(
    "Digite alguns filmes que você gosta (opcional):",
    placeholder="Ex: Vingadores, Matrix, O Senhor dos Anéis"
)

# Botão de gerar recomendação
if st.button("Recomendar Filmes"):
    with st.spinner("Buscando recomendações..."):
        resultado = gerar_recomendacoes(escolha_classificacao, escolha_genero, filmes_favoritos)
        st.subheader("🎥 Recomendações de Filmes:")
        st.write(resultado)
