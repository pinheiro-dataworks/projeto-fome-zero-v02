import streamlit as st #importa a biblioteca Streamlit como st

import utils.cities_data as cdt #importa o módulo local utils.cities_data como cdt

def make_sidebar(df): #constroi os filtros no sidebar
    st.sidebar.markdown("## Filtros") #escreve o título "Filtros"

    countries = st.sidebar.multiselect( #escolhas os países que deseja
        "Escolha os paises que deseja visualizar as informações",
        df.loc[:, "country"].unique().tolist(), #opções obtidas de "country"
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    return list(countries) #garante que o retorno seja exatamente uma lista de strings

def main(): #define a função principal
    st.set_page_config(page_title="Cities", page_icon="🏙️", layout="wide") #configura a página do Streamlit

    df = cdt.read_processed_data() #chama a função para ler os dados processados

    countries = make_sidebar(df) #constrói o sidebar e obtém a lista de países selecionados pelo usuário

    st.markdown("# :cityscape: Visão Cidades") #exibe um título na página com emoji e texto

    fig = cdt.top_cities_restaurants(countries) #gera um gráfico Plotly com as top cidades

    st.plotly_chart(fig, use_container_width=True) #renderiza o gráfico Plotly ocupando a largura do container
    
    best, worst = st.columns(2) #cria duas colunas lado a lado, atribui referências para elas

    with best: #contexto da coluna esquerda para renderização do que vier dentro
        fig = cdt.top_best_restaurants(countries) #monta figura com os melhores restaurantes

        st.plotly_chart(fig, use_container_width=True) #exibe o gráfico dos melhores restaurantes dentro da coluna esquerda

    with worst: #contexto da coluna direita
        fig = cdt.top_worst_restaurants(countries) #monta a figura com os piores restaurantes

        st.plotly_chart(fig, use_container_width=True) #exibe o gráfico dos piores restaurantes

    fig = cdt.most_cuisines(countries) #figura com as culinárias mais presentes

    st.plotly_chart(fig, use_container_width=True) #exibe gráfico de culinárias mais comuns

if __name__ == "__main__": #garante que só executa quando o arquivo for rodado diretamente
    main() #inicia Streamlit