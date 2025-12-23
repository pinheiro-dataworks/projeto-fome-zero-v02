import pandas as pd #importa bibliotecas pandas com pd
import plotly.express as px #importa Plotly Express (interface de alto nível para gráficos) como px
import plotly.graph_objects as go #importa a API de baixo nível do Plotly como go
import streamlit as st #importa o Streamlit como st para app web

def read_processed_data(): #define uma função sem parâmetros para carregar os dados processados
    return pd.read_csv("./data/processed/data.csv") #lê o arquivo CSV no caminho indicado usando pandas e retorna um DataFrame

def top_cities_restaurants(countries): #define a função que recebe countries
    df = read_processed_data() #carrega o DataFrame a partir do CSV

    grouped_df = ( #cria um DataFrame agragado e ordenado
        df.loc[df["country"].isin(countries), ["restaurant_id", "country", "city"]] #filtra linhas onde a coluna country está na lista countries, seleciona apenas restaurant_id, country, city
        .groupby(["country", "city"]) #agrupa por país e cidade
        .count() #conta linhas por grupo
        .sort_values(["restaurant_id", "city"], ascending=[False, True]) #ordena por restaurant_id em ordem decrescente (cidades com mais restaurantes primeiro), empata por city em ordem alfabética
        .reset_index() #reseta o índice para voltar a colunas normais após o groupby
    )

    fig = px.bar( #gera um gráfico de barras com Plotly Express
        grouped_df.head(10), #usa apenas as 10 primeiras linhas do DataFrame ordenado
        x="city", #define o eixo X
        y="restaurant_id", #define o eixo Y
        text="restaurant_id", #rótulo nas barras
        text_auto=".2f", #formata em duas casas decimais, a contagem é inteiro
        color="country", #colore as barras pelo país
        title="Top 10 Cidades com mais restaurantes na base de dados", #título do gráfico
        labels={ #define rótulos para eixos e legendas
            "city": "Cidade",
            "restaurant_id": "Quantidade de restaurantes",
            "country": "País",
        },
    )

    return fig #retorna a figura Plotly

def top_best_restaurants(countries): #define a função que recebe uma lista de países
    df = read_processed_data() #carrega os dados

    grouped_df = ( #repete a lógica de agrupamento, mas com filtro de avaliação
        df.loc[
            (df["aggregate_rating"] >= 4) & (df["country"].isin(countries)), #filtra linhas por restaurantes bem avaliados
            ["restaurant_id", "country", "city"],
        ]
        .groupby(["country", "city"]) #conta quantos restaurantes por país/cidade atendem o filtro
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True]) #ordena por restaurante e cidade
        .reset_index()
    )

    fig = px.bar( #cria gráfico de barras
        grouped_df.head(7), #considera as Top 7 cidades
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country",
        title="Top 7 Cidades com restaurantes com média de avaliação acima de 4",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de restaurantes",
            "country": "País",
        },
    )

    return fig

def top_worst_restaurants(countries): #define a função para piores avaliações
    df = read_processed_data()

    grouped_df = (
        df.loc[
            (df["aggregate_rating"] <= 2.5) & (df["country"].isin(countries)),
            ["restaurant_id", "country", "city"],
        ]
        .groupby(["country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(7),
        x="city",
        y="restaurant_id",
        text="restaurant_id",
        text_auto=".2f",
        color="country",
        title="Top 7 Cidades com restaurantes com média de avaliação abaixo de 2.5",
        labels={
            "city": "Cidade",
            "restaurant_id": "Quantidade de restaurantes",
            "country": "País",
        },
    )

    return fig

def most_cuisines(countries): #define a função para diversidades de culinárias
    df = read_processed_data()

    grouped_df = ( #conta os tipos únicos de culinárias
        df.loc[df["country"].isin(countries), ["cuisines", "country", "city"]]
        .groupby(["country", "city"])
        .nunique()
        .sort_values(["cuisines", "city"], ascending=[False, True])
        .reset_index()
    )

    fig = px.bar(
        grouped_df.head(10),
        x="city",
        y="cuisines",
        text="cuisines",
        color="country",
        title="Top 10 Cidades mais restaurantes com tipos culinários distintos",
        labels={
            "city": "Cidades",
            "cuisines": "Quantidade de Tipos Culinários Únicos",
            "country": "País",
        },
    )

    return fig