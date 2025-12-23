import streamlit as st
import utils.cuisines_data as cdt #importa um módulo utilitário próprio como cdt - função de leitura de dados e geração de métricas/gráficos

def make_sidebar(df):
    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect( #cria um controle de multi-seleção para escolher os países
        "Escolha os paises que deseja visualizar as informações",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    top_n = st.sidebar.slider( #cria um slider numérico na sidebar
        "Selecione a quantidade de restaurantes que deseja visualizar", 1, 20, 10 #intervalo mínima 1 e máximo 20, valor padrão 10
    )

    cuisines = st.sidebar.multiselect(
        "Escolha os tipos de culinária ",
        df.loc[:, "cuisines"].unique().tolist(),
        default=[
            "Home-made",
            "BBQ",
            "Japanese",
            "Brazilian",
            "Arabian",
            "American",
            "Italian",
        ],
    )

    return list(countries), top_n, list(cuisines) #retorna a seleção do usuário

def main():
    st.set_page_config(page_title="Cuisines", page_icon="🍽️", layout="wide") #configura a página

    df = cdt.read_processed_data() #usa o cdt para carregar os dados

    countries, top_n, cuisines = make_sidebar(df) #chama a função sidebar para capturar a seleção do usuário

    st.markdown("# :fork_and_knife_with_plate: Visão Tipos de Culinárias") #título principal

    df_restaurants = cdt.top_restaurants(countries, cuisines, top_n) #chama função utilitária que retorna um DataFrame com os top restaurantes, filtrando por countries e cuisines, limitado a top_n

    st.markdown(f"## Melhores restaurantes dos principais tipos de Culinárias")

    cdt.write_metrics() #chama a função utilitária para escrever métricas

    st.markdown(f"## Top {top_n} Restaurantes") # f"..." → f-string do Python que permite inserir variáveis dentro de uma string usando {variável}.
    # ## Top {top_n} Restaurantes → Sintaxe Markdown/ ## cria um heading de nível 2 (equivalente a <h2> em HTML)/ {top_n} é substituído pelo valor da variável top_n

    st.dataframe(df_restaurants) #exibe o dataframe de restaurantes em grid interativo (ordenável, rolável)

    best, worst = st.columns(2)

    with best:
        fig = cdt.top_best_cuisines(countries, top_n)

        st.plotly_chart(fig, use_container_width=True)

    with worst:
        fig = cdt.top_worst_cuisines(countries, top_n)

        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":

    main()
