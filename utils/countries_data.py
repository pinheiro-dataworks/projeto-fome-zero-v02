import pandas as pd
import plotly.express as px
import plotly.graph_objects as go #importa Plotly Graph Objects como go, interface de baixo nível para gráficos mais customizados
import streamlit as st

def read_processed_data(): #define a função que lê e retorna o DataFrame processado
    return pd.read_csv("./data/processed/data.csv") #usa pandas.read_csv para carregar o arquivo CSV

def countries_restaurants(countries): #define a função que recebe uma lista de países (countries) e produz um gráfico com a quantidad e de restaurantes por país
    df = read_processed_data() #lê os dados do CSV e armazena no DataFrame df

    grouped_df = ( 
        df.loc[df["country"].isin(countries), ["restaurant_id", "country"]] #filtra as linhas cujo country está na alista countries e seleciona apenas as colunas restaurant_id e country
        .groupby("country") #agrupa os dados por país
        .count()  #conta quantas linhas existem por país
        .sort_values("restaurant_id", ascending=False) #ordena o resultado em ordem descrescente pela contagem de restaurant_id
        .reset_index() #reseta o índice para transformar o índice do groupby em coluna normal (country vira coluna)
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="restaurant_id",
        text="restaurant_id",
        title="Quantidade de restaurantes registrados por país",
        labels={
            "country": "Paises",
            "restaurant_id": "Quantidade de restaurantes",
        },
    )

    return fig

def countries_cities(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["city", "country"]]
        .groupby("country")
        .nunique()
        .sort_values("city", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="city",
        text="city",
        title="Quantidade de cidades registrados por país",
        labels={
            "country": "Paises",
            "city": "Quantidade de cidades",
        },
    )

    return fig

def countries_mean_votes(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["votes", "country"]]
        .groupby("country")
        .mean()
        .sort_values("votes", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="votes",
        text="votes",
        text_auto=".2f",
        title="Média de avaliações feitas por país",
        labels={
            "country": "Paises",
            "votes": "Quantidade de avaliações",
        },
    )

    return fig

def countries_average_plate(countries):
    df = read_processed_data()

    grouped_df = (
        df.loc[df["country"].isin(countries), ["average_cost_for_two", "country"]]
        .groupby("country")
        .mean()
        .sort_values("average_cost_for_two", ascending=False)
        .reset_index()
    )

    fig = px.bar(
        grouped_df,
        x="country",
        y="average_cost_for_two",
        text="average_cost_for_two",
        text_auto=".2f",
        title="Média de preço de um prato para duas pessoas por país",
        labels={
            "country": "Paises",
            "average_cost_for_two": "Preço de prato para duas pessoas",
        },
    )

    return fig