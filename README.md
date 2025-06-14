🚀 Como Executar Localmente
1. Clone ou baixe o projeto
bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Crie um ambiente virtual (opcional)
bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
3. Instale as dependências
bash
Copiar código
pip install streamlit google-generativeai
4. Rode o aplicativo
bash
Copiar código
streamlit run app.py
🔑 Configuração da API do Google Gemini
Acesse Google AI Studio e obtenha sua API Key.

Substitua no código a chave:

python
Copiar código
genai.configure(api_key="SUA_CHAVE_AQUI")
📁 Estrutura do Código
plaintext
Copiar código
app.py                    # Código principal com interface Streamlit
requirements.txt (opcional)  # Dependências do projeto
README.md                 # Documentação do projeto
💡 Exemplo de Uso
Acesse o site local gerado pelo Streamlit

Escolha a classificação etária

Escolha o gênero de filme

(Opcional) Digite filmes que você gosta para personalizar

Clique em "Recomendar Filmes"

Veja as sugestões geradas com nome, sinopse e ano

✨ Melhorias Futuras
Integração com API do TMDB para resultados reais

Armazenar favoritos e histórico do usuário

Exportar recomendações como PDF

Design customizado com CSS / Tailwind

📄 Licença
Este projeto é apenas um exemplo educacional. Para fins comerciais, verifique as políticas de uso da API do Google.
