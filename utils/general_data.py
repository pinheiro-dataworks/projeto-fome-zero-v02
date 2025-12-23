import pandas as pd
from .process_data import process_data #faz um import relativo da função process_data de um módulo local

def qty_restaurants(dataframe): #define uma função que recebe um DataFrame (Pandas) como parâmetro
    return dataframe.shape[0] #retorna o número de linhas do DataFrame (quantidade de registros). shape[0] é equivalente a len(dataframe)

def qty_countries(dataframe): #define função para contar países distintos
    return dataframe.loc[:, "country"].nunique() #seleciona a coluna "country" com .loc[:,"country"] (todas as linhas, coluna "country")
    #aplica.unique() para contar o número de valores distintos (exclui NaN por padrão)
def qty_cities(dataframe):
    return dataframe.loc[:, "city"].nunique()

def qty_ratings(dataframe):
    return dataframe.loc[:, "votes"].sum()

def qty_cuisines(dataframe):
    return dataframe.loc[:, "cuisines"].nunique()