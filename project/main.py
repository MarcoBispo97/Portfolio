import streamlit as st
from deep_translator import GoogleTranslator

# Função para traduzir textos


def tradutor(texto, traduzir):
    if traduzir:
        return GoogleTranslator(source="pt", target="en").translate(texto)
    else:
        return texto

# Função para exibir o conteúdo da página selecionada


def show_page(page_name, traduzir):
    st.title(tradutor("Portfolio Cientista de dados:\nMarco A.Bispo", traduzir))

    if page_name == "navigation":
        st.write(tradutor("Conteúdo da página de navegação", traduzir))
    elif page_name == "data":
        st.write(tradutor("Conteúdo da página de dados", traduzir))
    elif page_name == "exploratory_analysis":
        st.write(tradutor("Conteúdo da página de análise exploratória", traduzir))
    elif page_name == "statistical_analysis":
        st.write(tradutor("Conteúdo da página de análise estatística", traduzir))
    elif page_name == "prediction_model":
        st.write(tradutor("Conteúdo da página de modelo de previsão", traduzir))
    elif page_name == "about_me":
        st.write(
            tradutor("Conteúdo da página sobre mim e onde me encontrar", traduzir))


def main():
    global traduzir_en  # Declarando traduzir_en como global

    if 'traduzir_en' not in globals():  # Verifica se traduzir_en não está definido
        traduzir_en = True  # Define traduzir_en como True por padrão

    # Selecionar idioma
    language = st.sidebar.selectbox(
        'Language', ['🇺🇸 EN', '🇧🇷 PT'])

    # Definir traduzir_en baseado na seleção de idioma
    if language == '🇧🇷 PT':
        traduzir_en = False
    else:
        traduzir_en = True

    # Botões na barra lateral para navegação
    if st.sidebar.button(tradutor("🧭 Navegação", traduzir_en)):
        st.query_params(page="navigation")
        show_page("navigation", traduzir_en)

    if st.sidebar.button(tradutor("📚 Dados", traduzir_en)):
        st.query_params(page="data")
        show_page("data", traduzir_en)

    if st.sidebar.button(tradutor("📊 Análise exploratória", traduzir_en)):
        st.query_params(page="exploratory_analysis")
        show_page("exploratory_analysis", traduzir_en)

    if st.sidebar.button(tradutor("📈 Análise estatística", traduzir_en)):
        st.query_params(page="statistical_analysis")
        show_page("statistical_analysis", traduzir_en)

    if st.sidebar.button(tradutor("🧮 Modelo de previsão", traduzir_en)):
        st.query_params(page="prediction_model")
        show_page("prediction_model", traduzir_en)

    if st.sidebar.button(tradutor("🔎 Sobre mim e onde me encontrar", traduzir_en)):
        st.query_params(page="about_me")
        show_page("about_me", traduzir_en)


if __name__ == "__main__":
    main()
