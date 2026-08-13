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

# 3. BARRA LATERAL / SELEÇÃO DE COLUNAS
st.sidebar.markdown("### ⚙️ Opções de Visualização")
num_colunas = st.sidebar.radio(
    "Escolha quantas colunas deseja ver por linha:",
    options=[1, 2, 3],
    index=2,  # Padrão: 2 colunas
    horizontal=True
)

# Ajusta a altura da imagem conforme o número de colunas
altura_imagem_css = 500 if num_colunas == 1 else (420 if num_colunas == 2 else 350)

# 4. CSS Ajustado (Corrigindo a visibilidade da Sidebar)
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

    /* ESTILIZAÇÃO DA SIDEBAR (BARRA LATERAL) - CORREÇÃO DO TEXTO INVISÍVEL */
    [data-testid="stSidebar"] {{
        background-color: #F3E8DC !important; /* Fundo suave levemente diferenciado */
        border-right: 2px solid #E5C3B2 !important;
    }}

    [data-testid="stSidebar"] * {{
        color: #3E201B !important; /* Texto castanho escuro visível */
        font-family: 'Poppins', sans-serif !important;
    }}

    [data-testid="stSidebar"] h3 {{
        color: #3E201B !important;
        font-family: 'Playfair Display', serif !important;
        font-weight: 700 !important;
    }}

    /* Textos gerais no conteúdo principal */
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

    /* ALTURA DAS IMAGENS DINÂMICA */
    div[data-testid="stImage"] img {{
        height: {altura_imagem_css}px !important;
        object-fit: cover !important;
        border-radius: 12px !important;
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
        color: #FFFFFF !important;
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

    /* AJUSTE DO BOTÃO FULLSCREEN DA IMAGEM */
    button[title="View fullscreen"] {{
        font-size: 0 !important;
        background-color: rgba(30, 41, 59, 0.85) !important;
        border-radius: 8px !important;
        padding: 6px !important;
        border: none !important;
        top: 10px !important;
        right: 10px !important;
    }}

    button[title="View fullscreen"]::before {{
        content: "⛶" !important;
        font-size: 16px !important;
        color: #FFFFFF !important;
    }}

    /* Garante visibilidade da camada */
    .stApp > header, .stApp > div {{
        position: relative;
        z-index: 1;
    }}
    </style>
""", unsafe_allow_html=True)

# 5. Processamento HD das Imagens
def carregar_imagem_hd(caminho, largura=1000, altura=800):
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

# 6. Lista de Produtos
bolos = [
    {
        "nome": "Bolo de Chocolate - com Cobertura de Chocolate",
        "preco": "R$ 35,00",
        "imagem": "imagens/bolo_chocolate.jpg"
    },
    {
        "nome": "Bolo de Churros - com Cobertura de Doce de Leite",
        "preco": "R$ 35,00",
        "imagem": "imagens/bolo_churros.jpg"
    },
    {
        "nome": "Bolo de Laranja - com Cobertura de Laranja",
        "preco": "R$ 35,00",
        "imagem": "imagens/bolo_laranja.jpg"
    },
    {
        "nome": "Bolo de Limão - com Cobertura de Limão",
        "preco": "R$ 35,00",
        "imagem": "imagens/bolo_limao.jpg"
    },
    {
        "nome": "Bolo de Cenoura - com Recheio de Brigadeiro e Cobertura de Chocolate",
        "preco": "R$ 35,00",
        "imagem": "imagens/bolo_cenourabrigadeiro.jpg"
    },
    {
        "nome": "Bolo de Cenoura - com Cobertura de Chocolate",
        "preco": "R$ 35,00",
        "imagem": "imagens/bolo_cenoura.jpg"
    },
    {
        "nome": "Bolo de Milho - com Goiabada e Requeijão",
        "preco": "R$ 35,00",
        "imagem": "imagens/bolo_milho.jpg"
    },
    {
        "nome": "Bolo de Ninho - com Cobertura de Ninho",
        "preco": "R$ 35,00",
        "imagem": "imagens/bolo_ninho.jpg"
    },
    {
        "nome": "Bolo de Chocolate - Vulcão Gourmet",
        "preco": "R$ 50,00",
        "imagem": "imagens/bolo_chocolatevulcao.jpg"
    },
    {
        "nome": "Bolo de Cenoura - Vulcão Gourmet",
        "preco": "R$ 50,00",
        "imagem": "imagens/bolo_cenouravulcao.jpg"
    },
    {
        "nome": "Bolo de Ninho - Vulcão Gourmet",
        "preco": "R$ 50,00",
        "imagem": "imagens/bolo_ninhovulcao.jpg"
    },
    {
        "nome": "Pudim de Chocolate",
        "preco": "R$ 40,00",
        "imagem": "imagens/pudim_chocolate.jpg"
    },
    {
        "nome": "Pudim de Leite Condensado",
        "preco": "R$ 40,00",
        "imagem": "imagens/pudim.jpg"
    }
]

# 7. Exibição dos Cards
cols = st.columns(num_colunas)

for index, bolo in enumerate(bolos):
    with cols[index % num_colunas]:
        with st.container(border=True):
            img = carregar_imagem_hd(bolo["imagem"])
            if img:
                st.image(img, use_container_width=True)
            else:
                st.info("Foto em breve")

            st.markdown(f"<h3 style='font-size: 19px; margin-bottom: 0;'>{bolo['nome']}</h3>", unsafe_allow_html=True)
            st.markdown(f'<div class="preco-destaque">{bolo["preco"]}</div>', unsafe_allow_html=True)
            
            descricao = bolo.get("descricao", "")
            if descricao:
                st.markdown(f"<p style='font-size: 14px; line-height: 1.4;'>{descricao}</p>", unsafe_allow_html=True)
            
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