import streamlit as st
from PIL import Image, ImageOps
import base64

# 1. Configuração da Página
st.set_page_config(
    page_title="Bolos Artesanais da Tê | Cardápio",
    page_icon="🎂",
    layout="wide"
)

# 2. Converte a logo para Base64 (fundo)
def get_image_base64(path):
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except Exception:
        return ""

logo_base64 = get_image_base64("imagens/logo.png")

# 3. CSS — Texto do Botão em BRANCO SÓLIDO (#FFFFFF)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;800&family=Poppins:wght@400;600&display=swap');

    /* Fundo Creme com a Logo Suave ao Fundo */
    .stApp {{
        background-color: #FAF4EB !important;
        background-image: url("data:image/png;base64,{logo_base64}");
        background-repeat: no-repeat;
        background-position: center 65%;
        background-attachment: fixed;
        background-size: 500px auto;
    }}

    /* Camada que suaviza a logo do fundo */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(250, 244, 235, 0.90);
        z-index: 0;
    }}

    /* Textos gerais em Castanho/Marrom Escuro */
    .stApp, .stApp p, .stApp div, .stApp span, .stApp label {{
        color: #3E201B !important;
        font-family: 'Poppins', sans-serif;
    }}

    /* Títulos Principais */
    h1, h2, h3, h4 {{
        color: #3E201B !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 800 !important;
    }}

    /* Cards dos Bolos */
    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: #FFFFFF !important;
        border-radius: 18px !important;
        border: 2px solid #E5C3B2 !important;
        box-shadow: 0 8px 24px rgba(62, 32, 27, 0.08) !important;
        padding: 18px;
        z-index: 2;
    }}

    /* Tag do Preço */
    .preco-destaque {{
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-weight: bold;
        color: #2E5B32 !important;
        background-color: #EBF4EC;
        padding: 6px 16px;
        border-radius: 8px;
        display: inline-block;
        margin: 10px 0;
    }}

    /* BOTÃO DE PEDIDO — Fundo Marrom e Texto BRANCO em Destaque */
    .stButton > button, 
    div[data-testid="stLinkButton"] > a,
    div[data-testid="stLinkButton"] a,
    div[data-testid="stLinkButton"] a * {{
        background-color: #3E201B !important;
        color: #FFFFFF !important; /* TEXTO BRANCO FORÇADO */
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        border: none !important;
        text-decoration: none !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}

    .stButton > button:hover, 
    div[data-testid="stLinkButton"] > a:hover {{
        background-color: #5A3029 !important;
        color: #FFFFFF !important;
    }}

    /* Garante visibilidade da camada */
    .stApp > header, .stApp > div {{
        position: relative;
        z-index: 1;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. Processamento HD das Imagens
def carregar_imagem_hd(caminho, largura=800, altura=600):
    try:
        img = Image.open(caminho).convert("RGB")
        return ImageOps.fit(img, (largura, altura), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
    except Exception:
        return None

# --- TOPO: LOGO CENTRALIZADA ---
col1, col2, col3 = st.columns([1, 1.2, 1])
with col2:
    try:
        st.image("imagens/logo.png", use_container_width=True)
    except Exception:
        st.title("Bolos Artesanais da Tê")

st.markdown("<h2 style='text-align: center; margin-top: 12px;'>Confira nossos bolos artesanais e faça seu pedido!</h2>", unsafe_allow_html=True)
st.divider()

# 5. Lista de Produtos
bolos = [
    {
        "nome": "Bolo de Chocolate - com Cobertura de Chocolate",
        "preco": "R$ 35,00",
        "descricao": "Massa fofinha de cacau 70% com recheio e cobertura de brigadeiro gourmet.",
        "imagem": "imagens/bolo_chocolate.jpg"
    },
    {
        "nome": "Bolo de Churros - com Cobertura de Doce de Leite",
        "preco": "R$ 35,00",
        "descricao": "Massa fofinha de cacau 70% com recheio e cobertura de brigadeiro gourmet.",
        "imagem": "imagens/bolo_churros.jpg"
    },
    {
        "nome": "Bolo de Laranja - com Cobertura de Laranja",
        "preco": "R$ 35,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/bolo_laranja.jpg"
    },
    {
        "nome": "Bolo de Limão - com Cobertura de Limão",
        "preco": "R$ 35,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/bolo_limao.jpg"
    },
    {
        "nome": "Bolo de Cenoura - com Recheio de Brigadeiro e Cobertura de Chocolate",
        "preco": "R$ 35,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/bolo_cenourabrigadeiro.jpg"
    },
    {
        "nome": "Bolo de Cenoura - com Cobertura de Chocolate",
        "preco": "R$ 35,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/bolo_cenoura.jpg"
    },
    {
        "nome": "Bolo de Milho - com Goiabada e Requeijão",
        "preco": "R$ 35,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/bolo_milho.jpg"
    },
    {
        "nome": "Bolo de Ninho - com Cobertura de Ninho",
        "preco": "R$ 35,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/bolo_ninho.jpg"
    },
    {
        "nome": "Bolo de Chocolate - Vulcão Gourmet",
        "preco": "R$ 50,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/bolo_chocolatevulcao.jpg"
    },
    {
        "nome": "Bolo de Cenoura - Vulcão Gourmet",
        "preco": "R$ 50,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/bolo_cenouravulcao.jpg"
    },
    {
        "nome": "Bolo de Ninho - Vulcão Gourmet",
        "preco": "R$ 50,00",
        "descricao": "O clássico de cenoura com uma generosa camada de cobertura cremosa.",
        "imagem": "imagens/bolo_ninhovulcao.jpg"
    },
    {
        "nome": "Pudim de Chocolate",
        "preco": "R$ 40,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/pudim_chocolate.jpg"
    },
    {
        "nome": "Pudim de Leite Condensado",
        "preco": "R$ 40,00",
        "descricao": "Massa leve com creme confeiteiro e morangos frescos selecionados.",
        "imagem": "imagens/pudim.jpg"
    }
]

# 6. Exibição dos Cards
cols = st.columns(3)

for index, bolo in enumerate(bolos):
    with cols[index % 3]:
        with st.container(border=True):
            img = carregar_imagem_hd(bolo["imagem"])
            if img:
                st.image(img, use_container_width=True)
            else:
                st.info("Foto em breve")

            st.markdown(f"<h3 style='font-size: 20px; margin-bottom: 0;'>{bolo['nome']}</h3>", unsafe_allow_html=True)
            st.markdown(f'<div class="preco-destaque">{bolo["preco"]}</div>', unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 14px; line-height: 1.4;'>{bolo['descricao']}</p>", unsafe_allow_html=True)
            
            link_wa = f"https://wa.me/5564992290542?text=Olá!%20Gostaria%20de%20encomendar%20o%20{bolo['nome']}"
            st.link_button("✨ FAZER PEDIDO NO WHATSAPP", link_wa, use_container_width=True)

# --- RODAPÉ ---
st.divider()
st.markdown("""
    <p style='text-align: center; font-size: 14px; color: #3E201B;'>
        <b>Bolos Artesanais da Tê</b><br>
        <i>Feito com amor e ingredientes selecionados</i>
    </p>
""", unsafe_allow_html=True)