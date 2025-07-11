import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="Tabela Nutricional", layout="centered")

st.title("🍽️ Gerador de Tabela Nutricional (ANVISA)")
st.markdown("Preencha os dados abaixo e baixe a imagem PNG gerada com tamanho fixo 400x300 px.")

# Entrada da porção
porcao = st.text_input("Porção", "100g")

dados = []

# Nutrientes padrão
nutrientes = [
    "Valor energético",
    "Carboidratos",
    "Açúcares totais",
    "Açúcares adicionados",
    "Proteínas",
    "Gorduras totais",
    "Gorduras saturadas",
    "Gorduras trans",
    "Fibra alimentar",
    "Sódio"
]

# Campos extras opcionais
extras = {
    "Lactose": st.checkbox("Incluir Lactose"),
    "Galactose": st.checkbox("Incluir Galactose"),
    "Cálcio": st.checkbox("Incluir Cálcio")
}

# Coleta de dados padrão
for nutriente in nutrientes:
    qtde = st.text_input(f"{nutriente} - Quantidade", "", key=nutriente + "_qtde")
    vd = st.text_input(f"{nutriente} - %VD", "", key=nutriente + "_vd")
    dados.append((nutriente, qtde, vd))

# Campos extras
for extra, incluir in extras.items():
    if incluir:
        qtde = st.text_input(f"{extra} - Quantidade", "", key=extra + "_qtde")
        vd = st.text_input(f"{extra} - %VD", "", key=extra + "_vd")
        dados.append((extra, qtde, vd))

# Botão para gerar imagem
if st.button("Gerar Imagem PNG"):
    largura, altura = 400, 300
    img = Image.new("RGB", (largura, altura),
