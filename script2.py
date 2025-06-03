import streamlit as st

# Entrada de texto
nome = st.text_input("Digite seu nome:")
if nome:
    st.write(f"Olá, {nome}! Boas-vindas ao Streamlit.")
else:
    st.write("Digite seu nome.")

# Seleção
cor = st.radio("Escolha uma cor:", ["Vermelho", "Verde", "Azul"])
if cor:
    st.write(f"Você selecionou a cor {cor}.")

