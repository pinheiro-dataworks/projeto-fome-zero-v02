import streamlit as st #importa biblioteca Streamlit

import utils.countries_data as cdt #importa um módulo local (utils.countries_data) que contém funções para leitura de dados e geração de gráficos
#cdt é o apelido para facilitar a chamada

def make_sidebar(df): #define e função make_sidebar que recebe um dataframe df e constrói filtros na barra lateral
    st.sidebar.markdown("## Filtros") #escreve o tírulo dos filtros na barra lateral

    countries = st.sidebar.multiselect( #cria um componente de seleção múltipla na sidebar
        "Escolha os paises que deseja visualizar as informações",
        df.loc[:, "country"].unique().tolist(), #extrai a coluna country, pega os valores únicos e converte para lista
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"], #define a seleção inicial 
    )

    return list(countries) #retorna a lista de países selecionados pelo usuário

def main(): #define a função principal da aplicação
    #configurando a página - título da aba do navegador; ícone da página; layout
    st.set_page_config(page_title="Countries", page_icon="🌍", layout="wide")

    df = cdt.read_processed_data() #função para ler dados já processados

    countries = make_sidebar(df) #constrói a barra lateral e captura a lista de países selecionados

    st.markdown("# :earth_americas: Visão Países") #exibe o título principal na página com emoji

    fig = cdt.countries_restaurants(countries) # gera uma figura com alguma métrica relacionada

    st.plotly_chart(fig, use_container_width=True) #renderiza a figura Plotly app, expandindo para a largura disponível do container

    fig = cdt.countries_cities(countries) #gera outra figura

    st.plotly_chart(fig, use_container_width=True) #exibe uma figura com largura fluida

    votes, plate_price = st.columns(2) #cria duas colunas lado a lado e atribui os containers a votes e plate_price

    with votes: #abre um contexto para inserir componentes dentro da coluna votes
        fig = cdt.countries_mean_votes(countries) #gera um gráfico considerando os países selecionados

        st.plotly_chart(fig, use_container_width=True) #exibe o gráfico na coluna votes

    with plate_price: #abre um contexto para inserir componentes dentro da coluna plate_price
        fig = cdt.countries_average_plate(countries) #gera um gráfico considerando os países selecionados

        st.plotly_chart(fig, use_container_width=True) #exibe o gráfico na coluna plate_price

    return None #retorna explicitamente None
    #Em python, o retorno padrão de uma função sem return já é none

if __name__ == "__main__": #garante que o bloco abaixo só será executado quando o arquivo for rodado diretamente
    main() #chama a função principal, iniciando o app Streamlit
