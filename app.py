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
    img = Image.new("RGB", (largura, altura), "white")
    draw = ImageDraw.Draw(img)
    fonte = ImageFont.load_default()

    # Cabeçalho da tabela
    draw.rectangle([0, 0, largura - 1, altura - 1], outline="black")
    draw.text((10, 10), "INFORMAÇÃO NUTRICIONAL", fill="black", font=fonte)
    draw.text((10, 30), f"Porção de {porcao}", fill="black", font=fonte)

    y = 55
    draw.text((10, y), "Nutriente", font=fonte)
    draw.text((160, y), "Quant.", font=fonte)
    draw.text((300, y), "%VD", font=fonte)
    y += 15
    draw.line([0, y, largura, y], fill="black")
    y += 5

    for item in dados:
        if y + 20 > altura:
            break
        nome, qtde, vd = item
        draw.text((10, y), nome, font=fonte)
        draw.text((160, y), qtde, font=fonte)
        draw.text((300, y), vd,
