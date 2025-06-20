import streamlit as st
import random

# Inicialização de variáveis na sessão
if 'numero_aleatorio' not in st.session_state:
    st.session_state.numero_aleatorio = random.randint(1, 1000)
if 'tentativas' not in st.session_state:
    st.session_state.tentativas = 0
if 'ranking' not in st.session_state:
    st.session_state.ranking = []
if 'jogo_ativo' not in st.session_state:
    st.session_state.jogo_ativo = False

st.title("🎯 Jogo da Adivinhação")
st.write("Tente adivinhar o número entre 1 e 1000!")

# Nome do jogador
nome = st.text_input("Digite seu nome:")

# Iniciar jogo
if st.button("Começar Jogo"):
    if nome:
        st.session_state.jogo_ativo = True
        st.session_state.numero_aleatorio = random.randint(1, 1000)
        st.session_state.tentativas = 0
    else:
        st.warning("Digite seu nome para começar.")

# Jogo principal
if st.session_state.jogo_ativo:
    numero = st.number_input("Digite seu palpite:", min_value=1, max_value=1000, step=1)
    if st.button("Enviar Palpite"):
        st.session_state.tentativas += 1

        if numero == st.session_state.numero_aleatorio:
            st.success(f"Parabéns, {nome}! Você acertou em {st.session_state.tentativas} tentativas.")
            st.session_state.ranking.append((nome, st.session_state.tentativas))
            st.session_state.jogo_ativo = False
        elif numero < st.session_state.numero_aleatorio:
            st.info("O número é **maior**!")
        else:
            st.info("O número é **menor**!")

# Mostrar ranking
if st.session_state.ranking:
    st.markdown("## 🏆 Ranking dos Jogadores")
    ranking_ordenado = sorted(st.session_state.ranking, key=lambda x: x[1])
    for i, (nome, tentativas) in enumerate(ranking_ordenado, start=1):
        st.write(f"{i}º lugar - {nome}: {tentativas} tentativas")
