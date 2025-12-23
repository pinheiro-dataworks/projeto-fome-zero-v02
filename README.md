# Projeto Fome Zero - Comunidade DS

## 📍 [Main Page]

Este módulo implementa uma aplicação interativa de visualização de restaurantes utilizando **Streamlit** e **Folium**. As principais funcionalidades incluem:

### 🎯 Barra Lateral (Sidebar)
- **Logo e Branding**: Exibe a logomarca do projeto "Fome Zero"
- **Filtro de Países**: Permite selecionar múltiplos países para visualizar restaurantes específicos
- **Download de Dados**: Oferece download dos dados já processados em formato CSV

### 📊 Dashboard Principal
Exibe métricas agregadas em cards informativos:
- Total de restaurantes cadastrados
- Quantidade de países na plataforma
- Número de cidades cobertas
- Total de avaliações realizadas
- Tipos de culinárias oferecidas

### 🗺️ Mapa Interativo
- **Visualização Geográfica**: Mapa interativo com marcadores de restaurantes
- **Clusterização de Marcadores**: Agrupa restaurantes próximos para melhor legibilidade
- **Popups Informativos**: Ao clicar em um marcador, exibe:
  - Nome do restaurante
  - Preço médio para duas pessoas
  - Tipo de culinária
  - Avaliação agregada (0-5.0)
- **Ícones Coloridos**: Cada marcador possui cor personalizada conforme categoria

### ⚙️ Fluxo de Dados
1. Carrega e processa dados brutos do CSV
2. Filtra restaurantes conforme seleção de países
3. Renderiza dashboard com métricas e mapa geográfico

**Tecnologias**: Streamlit, Folium, Pandas, PIL


## 📍 [Cities ]

Esta página Streamlit oferece uma análise interativa de dados de cidades e restaurantes.Funcionalidades Principais:
Filtro por País: Selecione os países de interesse através de um filtro no sidebar.
Visualizações: Exibe diversos gráficos para explorar os dados:

### Top cidades com maior número de restaurantes.
1. Os melhores restaurantes, baseados em avaliações.
2. Os piores restaurantes, baseados em avaliações.
3. As culinárias mais comuns e sua distribuição.

Layout Otimizado: Os gráficos de "Melhores Restaurantes" e "Piores Restaurantes" são apresentados lado a lado em um layout de duas colunas para facilitar a comparação

## 📍 [Countries ]

Este aplicativo Streamlit oferece uma visão interativa e abrangente sobre dados de países. Ele carrega dados processados e permite aos usuários filtrar múltiplos países através de uma sidebar intuitiva.A interface principal, apresentada em um layout amplo (wide), exibe quatro visualizações dinâmicas geradas com Plotly:
1. Restaurantes por país
2. Cidades por país
3. Média de votos por país (em coluna dedicada)
4. Preço médio do prato por país (em coluna dedicada)

Com o título ":earth_americas: Visão Países", a ferramenta facilita a exploração e comparação de métricas importantes entre diferentes nações de forma clara e eficiente.Aqui está o resumo pronto para seu README.md:Visão Países: Análise Interativa com StreamlitEste aplicativo Streamlit oferece uma visão interativa e abrangente sobre dados de países. 

Ele carrega dados processados e permite aos usuários filtrar múltiplos países através de uma sidebar intuitiva.A interface principal, apresentada em um layout amplo (wide), exibe quatro visualizações dinâmicas geradas com Plotly:
1. Restaurantes por país
2. Cidades por país
3. Média de votos por país (em coluna dedicada)
4. Preço médio do prato por país (em coluna dedicada)

## 📍 [Cuisines ]

Este aplicativo Streamlit oferece uma plataforma interativa para explorar dados de restaurantes, permitindo análises detalhadas por países e tipos de culinária.

## Propósito
O objetivo principal é fornecer uma ferramenta visual e fácil de usar para que os usuários possam analisar e descobrir os melhores restaurantes e tendências culinárias em diferentes regiões geográficas.

## Funcionalidades Principais

Filtros Interativos na Barra Lateral:
1. Seleção de Países: Escolha múltiplos países para focar a análise.
2. Quantidade de Restaurantes (Top N): Ajuste o número de restaurantes a serem exibidos nas visualizações.
3. Seleção de Culinárias: Filtre por tipos específicos de culinária.
4. Visualização Dinâmica: Todas as visualizações são atualizadas em tempo real com base nas seleções dos filtros.

## Componentes Visuais
1. Tabela de Restaurantes: Exibe uma lista detalhada dos "Top N" restaurantes, com base nos filtros aplicados.
2. Gráficos de Culinárias (Plotly):
    Melhores Culinárias: Gráfico que destaca os tipos de culinária com melhor avaliação ou desempenho.
    Piores Culinárias: Gráfico que mostra os tipos de culinária com menor avaliação ou desempenho.
3. Métricas Chave: Apresenta métricas resumidas relevantes para a análise.

## Tecnologias Utilizadas
Streamlit: Framework Python para construção rápida de aplicações web interativas.
Plotly: Biblioteca para criação de gráficos interativos e visualmente ricos.
Python: Linguagem de programação principal.


## Como Usar
1. Acesse o aplicativo.
2. Na barra lateral esquerda, utilize os filtros para:
    Selecionar os países de interesse (ex: "Brazil", "England").
    Ajustar o slider para definir quantos restaurantes você deseja ver (ex: "10").
    Escolher os tipos de culinária que deseja analisar (ex: "Japanese", "Italian").
3. Observe como a tabela de restaurantes e os gráficos de melhores/piores culinárias são atualizados instantaneamente na página principal, refletindo suas seleções.