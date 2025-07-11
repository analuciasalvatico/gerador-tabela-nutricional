import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="Tabela Nutricional", layout="centered")

st.title("🍽️ Gerador de Tabela Nutricional (ANVISA)")
st.markdown("Preencha os dados abaixo e baixe a imagem PNG gerada com tamanho automático.")

# Nutrientes principais
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

# Extras opcionais (fora do formulário para não resetar)
extras = {
    "Lactose": st.checkbox("Incluir Lactose"),
    "Galactose": st.checkbox("Incluir Galactose"),
    "Cálcio": st.checkbox("Incluir Cálcio")
}

# Formulário principal
with st.form("formulario_nutricional"):
    porcao = st.text_input("Porção", "100g")

    dados = []
    for nutriente in nutrientes:
        qtde = st.text_input(f"{nutriente} - Quantidade", "0", key=nutriente+"_q")
        vd = st.text_input(f"{nutriente} - %VD", "0", key=nutriente+"_v")
        dados.append((nutriente, qtde, vd))

    for extra, ativo in extras.items():
        if ativo:
            qtde = st.text_input(f"{extra} - Quantidade", "0", key=extra+"_q")
            vd = st.text_input(f"{extra} - %VD", "0", key=extra+"_v")
            dados.append((extra, qtde, vd))

    submit = st.form_submit_button("Gerar Imagem PNG")

# Se clicou no botão
if submit:
    st.markdown("### Prévia dos dados:")
    st.write(dados)

    largura = 400
    altura = 100 + len(dados) * 25
    img = Image.new("RGB", (largura, altura), "white")
    draw = ImageDraw.Draw(img)

    try:
        fonte = ImageFont.truetype("arial.ttf", 14)
    except:
        fonte = ImageFont.load_default()

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

    for nome, qtde, vd in dados:
        draw.text((10, y), nome, font=fonte)
        draw.text((160, y), qtde, font=fonte)
        draw.text((300, y), vd, font=fonte)
        y += 20

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.image(byte_im, caption="Imagem gerada com dados")
    st.download_button("📥 Baixar imagem PNG", byte_im, file_name="tabela_nutricional.png", mime="image/png")
