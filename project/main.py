import streamlit as st
from deep_translator import GoogleTranslator
from PIL import Image


def tradutor(texto, traduzir):
    if traduzir:
        return GoogleTranslator(source="pt", target="en").translate(texto)
    else:
        return texto

# Função para exibir o conteúdo da página selecionada
language = st.sidebar.selectbox('Idiom/Idioma', ['🇺🇸 EN', '🇧🇷 PT'])
traduzir_en = language == '🇺🇸 EN'

def show_page(page_name, traduzir = traduzir_en):
    st.title(tradutor("Portfolio Cientista de dados:", traduzir))
    st.header(tradutor("Feito por: Marco A.Bispo", traduzir), divider=True)

    if page_name == "📖 Menu":
        st.write(tradutor("MENU !", traduzir))


    elif page_name == tradutor("📚 Dados",traduzir):
        st.write(tradutor("Conteúdo da página de dados", traduzir))
    elif page_name == tradutor("📊 Análise exploratória",traduzir):
        st.write(tradutor("Conteúdo da página de análise exploratória", traduzir))
    elif page_name == tradutor("📈 Análise estatística",traduzir):
        st.write(tradutor("Conteúdo da página de análise estatística", traduzir))
    elif page_name == tradutor("🧮 Modelagem",traduzir):
        st.write(tradutor("Conteúdo da página de modelo de previsão", traduzir))
    elif page_name == tradutor("🔎 Sobre mim e onde me encontrar",traduzir):
        

        css_file = "C:\\Users\\marco\\Documents\\data_science\\Portfolio\\about_me\\main.css"
        resume_file = "C:\\Users\\marco\\Documents\\data_science\\Portfolio\\about_me\\Marco Bispo c.v..pdf"
        profile_pic = "C:\\Users\\marco\\Documents\\data_science\\Portfolio\\about_me\\profile-pic-official.png"

        # Abrindo e aplicando o arquivo CSS
        with open(css_file) as f:
            st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

        # Abrindo e lendo o arquivo PDF
        with open(resume_file, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Abrindo e carregando a imagem de perfil
        profile_pic = Image.open(profile_pic)

        # Exibir o PDF no Streamlit
        st.download_button(
            label="Baixar Currículo",
            data=PDFbyte,
            file_name="Curriculo.pdf",
            mime="application/pdf",
        )
        NAME = "Marco A.Bispo"
        EMAIL = "marcobispo97@gmail.com"
        SOCIAL_MEDIA = {
            "Linkedin":"https://www.linkedin.com/in/marco-bispo-b66274150/",
            "Github":"https://github.com/MarcoBispo97",
            "Instagram":"https://www.instagram.com/marco_bispo/"
        }
        DESCRIPTION = tradutor("Cientista de dados, auxiliando empresas no suporte à tomada de decisões baseada em dados.",traduzir)
        st.header(tradutor("🔎 Olá !", traduzir))
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.image(profile_pic, width=230)

        with col2:
            st.title(NAME)
            st.write(DESCRIPTION)
            st.download_button(
                label=" 📄 Download Resume",
                data=PDFbyte,
                file_name="Marco_Bispo_CV.pdf",  # Substitua aqui pelo nome do arquivo desejado
                mime="application/octet-stream",
            )
            st.write("📫", EMAIL)

        st.write('\n')
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]({link})")

def main(traduzir = traduzir_en):
    st.sidebar.title(tradutor("🧭 Navegação", traduzir))
    page = st.sidebar.radio(
        tradutor("Escolha uma página", traduzir_en),
        [tradutor('📖 Menu',traduzir),
        tradutor("📚 Dados",traduzir),
        tradutor("📊 Análise exploratória",traduzir),
        tradutor("📈 Análise estatística",traduzir),
        tradutor("🧮 Modelagem",traduzir),
        tradutor("🔎 Sobre mim e onde me encontrar",traduzir)]
        ,index=0
    )

    show_page(page, traduzir_en)


if __name__ == "__main__":
    main()
