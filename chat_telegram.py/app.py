import streamlit as st
import subprocess
import os

st.set_page_config(page_title="bot ativo", layout="centered")

st.title("🤖 bot telegram")
st.success(" o serviço está ativo no render.")

# Inicia o bot UMA ÚNICA VEZ
if "bot_iniciado" not in st.session_state:
    st.session_state.bot_iniciado = True
    subprocess.Popen(["python", "bot.py"])

st.markdown("""
este web service existe apenas para manter o bot online.
use o telegram para conversar com o bot.

""")

