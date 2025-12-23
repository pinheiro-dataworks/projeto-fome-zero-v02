import folium #folium usado para criar mapas interativos
import pandas as pd #pandas para manipulação de dados tabulares
import streamlit as st #streamlit para construção da interface web interativa
from folium.plugins import MarkerCluster #importa o plugin do folium para agrupar marcadores no mapa - clusterização
from PIL import Image #pillow (PIL) para carregar/manipular imagens streamlit
from streamlit_folium import folium_static #função para renderizar um objeto folium dentro de um app streamlit

from utils import general_data as gd #importa um módulo utilitário próprio e o referencia como gd
from utils.process_data import process_data #função própria para processar/limpar os dados brutos

RAW_DATA_PATH = f"./data/raw/data.csv" #define o caminho do arquivo CSV bruto a ser processado

def create_sidebar(df): #constroi a barra lateral do app e retorna os países selecionados
    #comentário de documentação
    """
    nova doc
    """
    image_path = "./img/" #caminho onde está a logo marca
    image = Image.open(image_path + "logo.png") #carrega a imagem usando PIL

    #Antes
    #col1, col2 = st.sidebar.columns([1, 4], gap="small") #cria duas colunas na sidebar (proporções 1:4) com um pequeno espaçamento
    #col1.image(image, width=35) #imagem com largura 35px
    #col2.markdown("# Fome Zero") #título como heading

    #Depois
    with st.sidebar:
        st.image(image, width=200)
    #    st.markdown("# Fome Zero")
    ##
    
    st.sidebar.markdown("## Filtros") #seção de subtítulo - filtro

    countries = st.sidebar.multiselect( #controle multiseleção
        "Escolha os paises que deseja visualizar os restaurantes",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    st.sidebar.markdown("### Dados Tratados") #subtítulo para informar os dados tratados para download

    processed_data = pd.read_csv("./data/processed/data.csv") #lê com pandas um CSV de dados tratados para download

    st.sidebar.download_button( #cria um botão download
        label="Download",
        data=processed_data.to_csv(index=False, sep=";"),
        file_name="data.csv",
        mime="text/csv",
    )

    return list(countries) #retorna a lista de países selecioandos

def create_map(dataframe):
    f = folium.Figure(width=1920, height=1080) #cria o container Figure para o mapa com tamanho fixo

    m = folium.Map(max_bounds=True).add_to(f) #cria mapa basem(Leaflet) e adiciona-o à Figure f
                    #max_bounds=True impede arrastar o mapa para fora dos limites mundiais
    marker_cluster = MarkerCluster().add_to(m) #cria um clustar para agrupar marcadores próximo uns dos outros e adiciona ao mapa

    for _, line in dataframe.iterrows(): #itera linha a linha no  DataFrame filtrado, para gerar um marcador por restaurante

        name = line["restaurant_name"] #nome do restaurante
        price_for_two = line["average_cost_for_two"]  #custo médio para 2 pessoas
        cuisine = line["cuisines"] #tipos de culinária
        currency = line["currency"] #moeda
        rating = line["aggregate_rating"] #nota agragada
        color = f'{line["color_name"]}' #cor do ícone do marcador, conversão para string

        #construção do HTML do popup
        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 ({}) para dois"
        html += "<br />Type: {}"
        html += "<br />Aggregate Rating: {}/5.0"
        html = html.format(name, price_for_two, currency, cuisine, rating)

        popup = folium.Popup( #cria um popup folium a partir do HTML
            folium.Html(html, script=True),
            max_width=500,
        )

        folium.Marker( #cria marcadores nas coordenadas
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"), #define um ícone "home" do Font Awesome
        ).add_to(marker_cluster)

    folium_static(m, width=1024, height=768) #renderiza o mapa m no app streamlit

def main():

    df = process_data(RAW_DATA_PATH) #chama a função utilitária para ler e processar o CSV bruto

    st.set_page_config(page_title="Home", page_icon="📊", layout="wide") #define metadados e layout da página streamlit

    selected_countries = create_sidebar(df) #monta a sidebar e obtém os países selecionados pelo usuário

    st.markdown("# Projeto Fome Zero") #títutlo principal da página

    st.markdown("## O lugar ideal para encontrar seu restaurante favorito!") #subtítulo 

    st.markdown("### Temos as seguintes marcas dentro da nossa plataforma:") #abre a seção de métricas

    restaurants, countries, cities, ratings, cuisines = st.columns(5) #cria 5 colunas lado a lado para exibir as métricas

    restaurants.metric( #mostra a métrica de quantidade de restaurantes
        "Restaurantes cadastrados",
        gd.qty_restaurants(df),
    )

    countries.metric( #métrica com total de países
        "Países cadastrados",
        gd.qty_countries(df),
    )

    cities.metric( #métrica com total de cidades
        "Cidades cadastradas",
        gd.qty_cities(df),
    )

    ratings.metric( #exibe a quantidade total de avaliações
        "Avaliações feitas na plataforma",
        f"{gd.qty_ratings(df):,}".replace(",", "."), #formata com seprador de milhar default (vírgula) e troca vírgula por ponto
    )

    cuisines.metric( #exibe a quantidade de tipos de culinária
        f"Tipos de Culinárias\nOferecidas",
        f"{gd.qty_cuisines(df):,}",
    )

    map_df = df.loc[df["country"].isin(selected_countries), :] #filtra o DataFrame para manter somente linhas com países selecionados

    create_map(map_df) #gera e exibe o mapa interativo com os restaurantes filtrados

    return None #retorno explícito

#bloco de execução - garante que o bloco seguinte só roda se o arquivo for executado diretamente
if __name__ == "__main__":
    main()
