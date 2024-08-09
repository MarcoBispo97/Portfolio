import streamlit as st
from deep_translator import GoogleTranslator
from PIL import Image

st.set_page_config(layout="wide")
def tradutor(texto, traduzir):
    if traduzir:
        return GoogleTranslator(source="pt", target="en").translate(texto)
    else:
        return texto


language = st.sidebar.selectbox('Idiom/Idioma', ['🇺🇸 EN', '🇧🇷 PT'])
traduzir_en = language == '🇺🇸 EN'

def show_page(page_name, traduzir = traduzir_en):
    st.title(tradutor("Portfolio Cientista de dados:", traduzir))
    

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

        NAME = "Marco A.Bispo"
        EMAIL = "marcobispo97@gmail.com"
        SOCIAL_MEDIA = {
            "Linkedin":"https://www.linkedin.com/in/marco-bispo-b66274150/",
            "Whatsapp":'https://api.whatsapp.com/send?phone=5512988881997&text=Hi%2C%20I%27m%20glad%20you%20called%20me%20on%20github%2C%20what%20can%20I%20help%3F',
            "Github":"https://github.com/MarcoBispo97",
            "Instagram":"https://www.instagram.com/marco_bispo/"
        }
        DESCRIPTION = tradutor("Cientista de dados, auxiliando empresas no suporte à tomada de decisões baseada em dados.",traduzir)
        CERTIFICATIONS = {
            "🏆 Microsoft Certified: Azure Fundamentals (AZ900)": "https://www.credly.com/badges/2b977e42-0f0e-464a-a615-a2464d6b5fb4/linked_in_profile",
            "🏆 Microsoft Certified: Azure Data Fundamentals (DP900)": "https://www.credly.com/badges/ed1eb507-7e0a-490f-b763-3633da59cc54/linked_in_profile",
            "🏆 Microsoft Certified: Azure AI Fundamentals  (AI900)": "https://www.credly.com/badges/af64b9d8-5c0c-4f16-ad28-dd05e469ab4f/public_url",
            "🏆 Academy Accreditation - Databricks Lakehouse Fundamentals": "https://credentials.databricks.com/ab70488a-904f-44f0-9db1-da7674d94cc1",
        }
        #st.header(tradutor("🔎 Olá !", traduzir), divider="blue")
        texto_traduzido = tradutor("🔎 Olá !", traduzir)
        st.markdown(
            f"<h2 style='text-align: center; color: white;'>{texto_traduzido}</h2>",
            unsafe_allow_html=True )
        col1, col2 = st.columns(2, gap="small")
        with col1:
            cola, colb, colc = st.columns(3)

            with cola:
                st.write(' ')

            with colb:
                st.markdown(
                """
                <style>
                    [data-testid="stImage"] img {
                        display: block;
                        margin-left: auto;
                        margin-right: auto;
                    }
                </style>
                """, 
                unsafe_allow_html=True)
                st.image(profile_pic, width=230)

            with colc:
                st.write(' ')
            

        with col2:
            st.title(NAME)
            st.write(DESCRIPTION)
            st.download_button(
                label=tradutor(" 📄 Download do Currículo", traduzir),
                data=PDFbyte,
                file_name="Marco_Bispo_CV.pdf",  # Substitua aqui pelo nome do arquivo desejado
                mime="application/octet-stream",
            )
            st.write("📫", EMAIL)

        st.write('\n')
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]({link})")

        # --- EXPERIENCE & QUALIFICATIONS ---
        st.write('\n')
        st.subheader("Experience & Qulifications", divider="blue")
        st.write(tradutor(
            """
            - ✔️ 5 anos de experiência extraindo insights acionáveis ​​de dados

            - ✔️ Grande experiência prática e conhecimento em Python, estatística, SQL e Excel

            - ✔️ Boa compreensão em estatística e suas respectivas aplicações

            - ✔️ Excelente colega de trabalho e com forte senso de iniciativa nas tarefas

            """, traduzir))
        
        # --- SKILLS ---
        st.write('\n')
        st.subheader("Hard Skills", divider="blue")
        st.write(tradutor(
            """
            - 👩‍💻 Programação:
                Python (Scikit-learn, Pandas, NumPy, XGBoost, Statsmodels, SciPy)
                SQL, VBA, C
            - 📊 Visualização de dados: MS Excel, Streamlit, Plotly, seaborn, matplotlib
            - 🧮 Modelagem Supervisionada: Regressão logística, Regressão linear, Árvores de decisão, floresta aleatória, Xboost
            - 🧮 Modelagem não Supervisionada: T-sne, PCA, DBSCAN, K-Means
            - 🎲 Bancos de dados: Postgres, MySQL, SQLite3
            - 🗄️ AWS: Athena, S3, Glue | AZURE: Databricks, Machine Learning
        """, traduzir))

        # --- WORK HISTORY ---
        st.write('\n')
        st.subheader(tradutor("Experiências", traduzir), divider="blue")

        # --- JOB 1
        st.write(tradutor("🚧 **Cientista de dados | Nuvem-Tecnologia 📍Brasil - Cuiabá, Mato Grosso**", traduzir))
        st.write(tradutor("🗓️ 02/2023 - Atualmente", traduzir))
        st.write(tradutor(
            """
        - ► Python: Aprendizado de Máquina, Pandas, Numpy, Sklearn, Seaborn, Pyplot, Streamlit, Scipy
        - ► Modelagem de produtividade, anomalias, análise estatística e análise exploratória    
        - ► PCA, Pearson, PACF, ADF, KPSS, Granger-Causalidade, Poisson
        - ► AWS: Athena (SQL), S3, Glue
        - ► Casos de uso voltados para o agronegócio
        """, traduzir))

        # --- JOB 2
        st.write('\n')
        st.write(tradutor("🚧 **Cientista de dados | Dataside 📍Brasil - São Paulo, São José dos Campos**", traduzir))
        st.write("🗓️ 02/2023 - 02/2024")
        st.write(tradutor(
            """
        - ► Pandas, Numpy, Sklearn, Azure ML, PySpark, Databricks
        - ► Desenvolvimento de modelo de ML
        - ► Regressão linear/logística
        - ► Análise Exploratória
        - ► Estudos de caso orientados para o mercado, RPA
        """, traduzir))

        # --- JOB 3
        st.write('\n')
        st.write(tradutor("🚧 **Estágio | Volkswagen 📍Brasil - São Paulo, Taubaté**", traduzir))
        st.write("🗓️ 09/2020 - 12/2021")
        st.write(tradutor(
            """
        - ► Economia de óleo, economizando 200 KR$ por ano no setor de estamparia
        - ► Automação de processos com Python e VBA dentro do SAP
        - ► Utilização de notebook jupyter para big data, no setor de manutenção
        - ► Manipulação de bancos de dados SQLite
        - ► Desenvolvimento de aplicações industriais e questionários
        - ► Análise e desenvolvimento de OEE e KPI de qualidade
        - ► Apresentação gerencial de suprimentos na War Room
        - ► Coordenação de pequenos projetos de inovação na área (indústria 4.0) envolvendo impressão 3D
        """, traduzir))

        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.subheader(tradutor("Educação",traduzir), divider="blue")
            st.write(tradutor("""🔢 **Matemática | UNITAU 09/2022 - 04/2024**""", traduzir))
            st.write(tradutor("""💡 **Engenharia Elétrica e Eletrônica | UNITAU** 01/2017 - 12/2021""", traduzir))


        with col2:
            st.subheader(tradutor("Certificados",traduzir), divider="blue")
            for project, link in CERTIFICATIONS.items():
                st.write(f"[{project}]({link})")
        

def main(traduzir = traduzir_en):
    st.sidebar.title(tradutor("🧭 Navegação:", traduzir))
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
