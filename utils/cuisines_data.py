import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def read_processed_data():
    return pd.read_csv("./data/processed/data.csv")

def top_cuisines():
    df = read_processed_data()

    cuisines = { #cria um dicionário com chaves de cinco culinárias, cada valor inicialmente é uma string vazia
        "Italian": "",
        "American": "",
        "Arabian": "",
        "Japanese": "",
        "Brazilian": "",
    }

    cols = [ #define uma lista de colunas que serão selecionadas do DataFrame para compor o resultado
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes",
    ]

    for key in cuisines.keys(): #itera sobre cada tipo de culinária (as chaves do dicionário cuisines)

        lines = df["cuisines"] == key #cria uma séria booleana (filtro) que é True nas linhas em que a coluna "cuisines" é igual à culinária atual (key)

        cuisines[key] = ( #bloco cuisines
            df.loc[lines, cols] #filtra o DataFrame df para manter somente as linhas do tipo culinária atual e apenas as colunas definidas em cols
            .sort_values(["aggregate_rating", "restaurant_id"], ascending=[False, True]) #ordena o resultado
            .iloc[0, :] #seleciona a primeira linha do DataFrame resultante
            .to_dict() #converte essa linha única em um dicionário Python. O resultado é atribuído a cuisines[key]
        )

    return cuisines #retorna o dicionário cuisines, agora mapeando cada culinária para os dados do seu melhor restaurante

def write_metrics(): #define uma função que escreve métricas no layout do Streamlit, em colunas paralelas, para as cinco culinárias

    cuisines = top_cuisines() #busca o dicionário de melhores restaurantes por culinária

    italian, american, arabian, japonese, brazilian = st.columns(len(cuisines)) #cria cinco colunas lado a lado no layout do Streamlit

    with italian:
        st.metric( #cria um cartão de métrica dentro da coluna italian
            label=f'Italiana: {cuisines["Italian"]["restaurant_name"]}',
            value=f'{cuisines["Italian"]["aggregate_rating"]}/5.0', #exibe nota do restaurante no formato nota/5.0
            help=f"""
            País: {cuisines["Italian"]['country']}\n
            Cidade: {cuisines["Italian"]['city']}\n
            Média Prato para dois: {cuisines["Italian"]['average_cost_for_two']} ({cuisines["Italian"]['currency']})
            """, #texto de ajuda (tooltip) multilinha com país e cidade
        )

    with american:
        st.metric(
            label=f'Italiana: {cuisines["American"]["restaurant_name"]}',
            value=f'{cuisines["American"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["American"]['country']}\n
            Cidade: {cuisines["American"]['city']}\n
            Média Prato para dois: {cuisines["American"]['average_cost_for_two']} ({cuisines["American"]['currency']})
            """,
        )

    with arabian:
        st.metric(
            label=f'Italiana: {cuisines["Arabian"]["restaurant_name"]}',
            value=f'{cuisines["Arabian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Arabian"]['country']}\n
            Cidade: {cuisines["Arabian"]['city']}\n
            Média Prato para dois: {cuisines["Arabian"]['average_cost_for_two']} ({cuisines["Arabian"]['currency']})
            """,
        )

    with japonese:
        st.metric(
            label=f'Italiana: {cuisines["Japanese"]["restaurant_name"]}',
            value=f'{cuisines["Japanese"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Japanese"]['country']}\n
            Cidade: {cuisines["Japanese"]['city']}\n
            Média Prato para dois: {cuisines["Japanese"]['average_cost_for_two']} ({cuisines["Japanese"]['currency']})
            """,
        )

    with brazilian:
        st.metric(
            label=f'Italiana: {cuisines["Brazilian"]["restaurant_name"]}',
            value=f'{cuisines["Brazilian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Brazilian"]['country']}\n
            Cidade: {cuisines["Brazilian"]['city']}\n
            Média Prato para dois: {cuisines["Brazilian"]['average_cost_for_two']} ({cuisines["Brazilian"]['currency']})
            """,
        )

    return None

def top_restaurants(countries, cuisines, top_n): #define uma função que retorna os Top N restaurantes (por nota) filtrando por países e tipos de culinária
    df = read_processed_data()

    cols = [ #bloco lista colunas que serão retornadas no resultado
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "aggregate_rating",
        "votes",
    ]
    #linhas cujo cuisines pertençam ao conjunto/lista cuisines & cujo country pertença ao conjunto/lista countries
    lines = (df["cuisines"].isin(cuisines)) & (df["country"].isin(countries)) 

    dataframe = df.loc[lines, cols].sort_values( #filtra e seleciona colunas, depois ordena
        ["aggregate_rating", "restaurant_id"], ascending=[False, True]
    )

    return dataframe.head(top_n)

def top_best_cuisines(countries, top_n):
    df = read_processed_data()

    lines = df["country"].isin(countries) #filtro booleano: mantém linhas cujo país está em countries

    grouped_df = (
        df.loc[lines, ["aggregate_rating", "cuisines"]] #filtra pos país e mantém só as colunas de interessa
        .groupby("cuisines")
        .mean() #agrupa por tipo de culinária e calcula a média das colunas numéricas
        .sort_values("aggregate_rating", ascending=False) #ordena pela média da nota de forma descrescente (melhores no topo)
        .reset_index() #restaura cuisines como coluna
        .head(top_n) #manté apenas as Top N culinárias
    )

    fig = px.bar( #cria o gráfico de barras com Plotly Express
        grouped_df.head(top_n), #garante que só as top N linhas são plotadas
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"Top {top_n} Melhores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação Média",
        },
    )

    return fig #retorna a figura construída para ser exibida no Streamlit


def top_worst_cuisines(countries, top_n):
    df = read_processed_data()

    lines = df["country"].isin(countries)

    grouped_df = (
        df.loc[lines, ["aggregate_rating", "cuisines"]]
        .groupby("cuisines")
        .mean()
        .sort_values("aggregate_rating")
        .reset_index()
        .head(top_n)
    )

    fig = px.bar(
        grouped_df.head(top_n),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"Top {top_n} Piores Tipos de Culinárias",
        labels={
            "cuisines": "Tipo de Culinária",
            "aggregate_rating": "Média da Avaliação Média",
        },
    )

    return fig