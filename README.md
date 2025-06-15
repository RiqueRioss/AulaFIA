# Como Executar Localmente(GIT)
1. Clone
crie ou entre na pasta desejada
clone o repositório:
git clone https://github.com/RiqueRioss/AulaFIA.git
2. Crie um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
3. Instale as dependências no CMD
Copiar código
pip install streamlit
pip install google-generativeai
4. Rode o aplicativo(CMD)
Copiar código
streamlit run app.py

# Configuração da API do Google Gemini
Acesse Google AI Studio e obtenha sua API Key.
Substitua no código no arquivo localizado em script3.py e na linha 4 a chave:

Exemplo: chave = "Sua Chave"

# Exemplo de Uso
Acesse o site local gerado pelo Streamlit

Escolha a classificação etária

Escolha o gênero de filme

Digite filmes que você gosta para personalizar

Clique em "Recomendar Filmes"
Veja as sugestões geradas com nome, sinopse e ano
