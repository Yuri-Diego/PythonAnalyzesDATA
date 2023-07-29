# Testando a Biblioteca Pandas para Tratamento de Dados

import plotly.express as px    # Ferramenta para Criacao de Graficos
import pandas as pd   # Importando a Biblioteca de analise de Dados

tabela = pd.read_csv("cancelamentos.csv")  

display(tabela) # Visualizar a Tabela por display (utilizado em arquivos ipynb)

# --------------------------------------- Tratamento de dados --------------------------------------- #

display(tabela.info())    # Funcao para verificar se ha alguma coluna sem Dados


tabela = tabela.dropna()   # Funcao para 'Droppar'(Remover) linhas com alguma coluna vazia.
display(tabela.info())


tabela = tabela.drop("CustomerID", axis=1)   # Funcao para 'Droppar'(Remover) a coluna nomeada "CustomerID"
display(tabela)

# --------------------------------------- Analise inicial dos Dados --------------------------------------- #

# Funcao para mostrar quantidade de Cancelamentos em Porcentagem
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))


# --------------------------------------- Analise superficial dos Dados --------------------------------------- #

# Funcao para agrupar as colunas das tabelas e calcular a media
display(tabela.groupby("duracao_contrato").mean(numeric_only=True))   # Qual duracao de contrato Cancelou mais
display(tabela.groupby("assinatura").mean(numeric_only=True))         # Qual Assinatura Cancelou mais
display(tabela.groupby("sexo").mean(numeric_only=True))               # Qual Sexo Cancelou mais

# Removendo a Assinatura Monthly para analisar a porcentagem de Cancelamento
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]   
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# --------------------------------------- Analise Profunda dos Dados com Graficos --------------------------------------- #

# Utilizando a Biblioteca Plotly para Exibir dados no formato de Grafico
grafico = px.histogram(tabela, x="duracao_contrato", color="cancelou", text_auto=True)   # Grafico da Coluna "duracao_contrato"
grafico.show()   # Exibir o grafico

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop("CustomerID", axis=1)
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()


# --------------------------------------- CONCLUSAO --------------------------------------- #

# A partir da Analise dos Graficos, conseguimos destacar os seguintes pontos possiveis para os Cancelamentos:
# - Apos de 21 Dias de atraso
# - Depois de 5 ligacoes para o Call Center
# - Contratos Mensais tem quase 100% de cancelamentos
tabela = tabela[tabela["dias_atraso"]<=20]
tabela = tabela[tabela["ligacoes_callcenter"]<5]
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
display(tabela)
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# Conclusao:
# Se resolvermos esses problemas, conseguimos reduzir o cancelamento de 56.7% para algo em torno de 18.4%