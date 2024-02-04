import pandas as pd
import plotly_express as px

dados = pd.read_excel("vendas.xlsx")

#verificando os dados do arquivo

print("\n primeiras 10 linhas")
print(dados.head(10))

print("\n últimas 10 linhas")
print(dados.tail(10))

print("\n saber linhas e colunas")
print(dados.shape)

print("\n saber tipos dos dados")
print(dados.info())

print("\n selecionar coluna")
print(dados.preco)

print("\n gerando estatísticas")
print(dados.preco.describe())

print("\n contagem agrupando dados de uma coluna")
print(dados.loja.value_counts())

print("\n agrupando dados de colunas")
print(dados.groupby("loja").preco.sum())
print("\n ")
print(dados.groupby(["estado", "cidade"]).preco.mean())

#criando excel com os dados solicitados
dados.groupby(["estado", "cidade", "loja"]).preco.sum().to_excel("faturamento.xlsx")

#criando gráficos com plotly_express

#gráfico de contagem de uma coluna
graficoVendasLoja = px.histogram(dados, x="loja", title="Vendas por loja")

#gráfico de soma da coluna y, agrupada pela coluna x
px.histogram(dados, x="loja", y="preco", title="Faturamento por loja", text_auto=True)

#gráfico de soma da coluna y, agrupada pela coluna x, definindo cores para uma terceira coluna
graficoFaturamento = px.histogram(dados, x="loja", y="preco", title="Faturamento por loja", text_auto=True, color="forma_pagamento")

#gerando arquivos dos gráficos
graficos = [graficoVendasLoja, graficoFaturamento]

for grafico in graficos:
    grafico.write_html(grafico.layout.title.text+".html")



#criando gráficos por coluna
colunas = ["loja", "estado", "cidade", "data"]

for coluna in colunas:
    grafico = px.histogram(dados, x=f"{coluna}", y="preco", title=f"Faturamento por {coluna}", text_auto=True, color="forma_pagamento")
    grafico.write_html(f"grafico-faturamento-{coluna}.html")