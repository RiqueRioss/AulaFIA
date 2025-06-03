import streamlit as st

# Configuração da página
st.set_page_config(page_title="Minha App", page_icon="🚀")


# Título da aplicação
st.title("Minha Primeira App Streamlit")

# Texto simples
st.write("Olá, mundo!")
st.header("Cabeçalho")
st.subheader("Subcabeçalho")

# Texto
st.text("Texto simples")
st.write("Texto com markdown suportado")
st.markdown("**Texto em negrito** e *itálico*")

# Código
st.code("print('Hello World')", language='python')


# Executar com: streamlit run app.py


# Entrada de texto
nome = st.text_input("Digite seu nome:")
biografia = st.text_area("Conte sobre você:")

# Números
idade = st.number_input("Idade:", min_value=0, max_value=120)
altura = st.slider("Altura (cm):", 100, 250, 170)

# Seleção
opcao = st.selectbox("Escolha uma opção:", ["A", "B", "C"])
multiplas = st.multiselect("Múltiplas escolhas:", ["X", "Y", "Z"])

# Checkbox e radio
aceito = st.checkbox("Eu aceito os termos")
genero = st.radio("Gênero:", ["Masculino", "Feminino", "Outro"])

# Botões
if st.button("Clique aqui"):
    st.write("Botão foi clicado!")
    st.success("✅ Operação realizada com sucesso")


# Upload de arquivo único
arquivo = st.file_uploader("Envie um arquivo", type=['csv', 'txt', 'xlsx'])
if arquivo is not None:
    # Processar arquivo CSV
    import pandas as pd
    df = pd.read_csv(arquivo)
    st.dataframe(df)


# Sidebar para controles
st.sidebar.title("Controles")
st.sidebar.write("Use os controles abaixo:")

# Widgets na sidebar
opcao = st.sidebar.selectbox("Escolha uma opção:", ["Opção 1", "Opção 2", "Opção 3"])
valor = st.sidebar.slider("Valor:", 0, 100, 50)
ativo = st.sidebar.checkbox("Ativar recurso")

# Exibir informações na sidebar
st.sidebar.info("ℹ️ Informações importantes aqui")
st.sidebar.success("✅ Operação realizada com sucesso")
st.sidebar.warning("⚠️ Atenção: verifique os dados")
st.sidebar.error("❌ Erro encontrado")