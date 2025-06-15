import streamlit as st
import google.generativeai as genai

chave = st.secrets["CHAVE"]

# Configura a API key do Gemini
genai.configure(api_key= chave)

# Carrega o modelo
model = genai.GenerativeModel("gemini-2.0-flash")

# Função para gerar recomendações com base na classificação, gênero e filmes favoritos
def gerar_recomendacoes(prompt):
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
escolha_classificacao = st.selectbox("Escolha a classificação etária:", classificacoes, index = None, placeholder = "Deixe em branco, caso queira qualquer classificação etária.")
if (escolha_classificacao):
    escolha_classificacao = "apropriados para a classificação etária: " + escolha_classificacao + ", "
else:
    escolha_classificacao = ""

# Seleção do gênero
escolha_genero = st.selectbox("Escolha o gênero do filme:", generos,index= None, placeholder = "Deixe em branco, caso queira qualquer gênero.")
if (escolha_genero):
    if(escolha_genero == "Outros"):
        escolha_genero = st.text_input("Qual gênero você deseja?")
    escolha_genero = "do gênero: "+ escolha_genero + ", "
else:
    escolha_genero = ""

# Campo opcional de filmes favoritos
filmes_favoritos = st.text_area(
    "Digite alguns filmes que você gosta:",
    placeholder="Ex: Vingadores, Matrix, O Senhor dos Anéis",
)
if (filmes_favoritos):
    filmes_favoritos = "semelhantes a estes: "+ filmes_favoritos
if(not filmes_favoritos and not escolha_classificacao and not escolha_genero):
    st.warning("Escolha pelo menos uma opção das anteriores!")
else:
    prompt = f"Recomende 5 filmes que sejam " + escolha_classificacao + escolha_genero + filmes_favoritos
    # Botão de gerar recomendação
    if st.button("Recomendar Filmes"):
        with st.spinner("Buscando recomendações..."):
            resultado = gerar_recomendacoes(prompt)
            st.subheader("🎥 Recomendações de Filmes:")
            st.write(resultado)

