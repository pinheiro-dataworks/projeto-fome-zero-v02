import inflection #importa a biblioteca inflection para transformar textos
import pandas as pd #importa o pandas e o chama de pd para manipulação de dados tabulares

COUNTRIES = { #dicionário que mapeia um código numérico de país (chave int) para o nome do país (valor str)
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

COLORS = { #dicionário que mapeia um código de cor (hexadecimal em str) para um nome de cor (valor str)
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

def rename_columns(dataframe):
    df = dataframe.copy() #faz uma cópia do DataFrame para evitar alterar o original por referência

    title = lambda x: inflection.titleize(x) #define uma função anônima que converte um texto para Title Case (primeira letra de cada palavra maiúscula)

    snakecase = lambda x: inflection.underscore(x) #converte um texto para snake_case

    spaces = lambda x: x.replace(" ", "") #define uma função anônima que remove espaços do texto

    cols_old = list(df.columns) #obtém a lista de nomes de colunas atuais do DataFrame

    cols_old = list(map(title, cols_old)) #aplica Title Case a todos os nomes de colunas

    cols_old = list(map(spaces, cols_old)) #Remove todos os espaços dos nomes (aps Title Case)

    cols_new = list(map(snakecase, cols_old)) #Converte o resultado para snake_case

    df.columns = cols_new #atribui a lista de novos nomes de colunas ao DataFrame

    return df #retorna o DataFrame com colunas renomeadas

def country_name(country_id):
    return COUNTRIES[country_id]

def color_name(color_code):
    return COLORS[color_code]

def create_price_tye(price_range): #classifica o campo price_range em uma categoria textual
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"


def adjust_columns_order(dataframe):
    df = dataframe.copy() #copia o DataFrame

    new_cols_order = [ #retorna o DataFrame reindezado com as colunas na ordem especificada
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "address",
        "locality",
        "locality_verbose",
        "longitude",
        "latitude",
        "cuisines",
        "price_type",
        "average_cost_for_two",
        "currency",
        "has_table_booking",
        "has_online_delivery",
        "is_delivering_now",
        "aggregate_rating",
        "rating_color",
        "color_name",
        "rating_text",
        "votes",
    ]

    return df.loc[:, new_cols_order]


def process_data(file_path):
    df = pd.read_csv(file_path) #lê o arquivo CSV em file_path

    df = rename_columns(df)  #padroniza os nomes das colunas para snake_case

    df = df.dropna() #remove quaisquer linhas com valores ausentes em qualquer coluna

    df["price_type"] = df.loc[:, "price_range"].apply(lambda x: create_price_tye(x)) #cria a coluna price_type a partir de price_range

    df["country"] = df.loc[:, "country_code"].apply(lambda x: country_name(x))

    df["color_name"] = df.loc[:, "rating_color"].apply(lambda x: color_name(x))

    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

    df = df.drop(df[(df["cuisines"] == "Drinks Only")].index) #remove linhas cuja cozinha (primeira) é exatamente "Drinks Only"

    df = df.drop(df[(df["cuisines"] == "Mineira")].index)

    df = df.drop_duplicates() #remove linhas duplicadas 

    df = adjust_columns_order(df)

    df.to_csv("./data/processed/data.csv", index=False) #salva o DataFrame processado em ./data/processed/data.csv sem a coluna de índice

    return df #retorna o DataFrame final processado