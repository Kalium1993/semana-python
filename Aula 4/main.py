import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly

codigo = input("Digite o código da ação: ")
if codigo == '':
    codigo = "PETR4.SA"

dados = yf.Ticker(codigo).history("2y")

#Tratamento de dados
#resetar o índice
treinamento = dados.reset_index()

#acessando 2 ou mais colunas
treinamento[["Date", "Close"]]

#manipulando a coluna Date
treinamento["Date"] = treinamento["Date"].dt.date

#filtrar dados
colunas = ["Date", "Close"]
treinamento = treinamento[colunas]

#alterar nomes das colunas
treinamento.columns = ["ds", "y"]

#Criando e treinando o modelo de Machine Learning
#criando modelo
modelo = Prophet()

#treinando modelo
modelo.fit(treinamento)

#gerando previsões
periodo = modelo.make_future_dataframe(90)

previsoes = modelo.predict(periodo)

#Visualização de Dados
plot_plotly(modelo, previsoes).show()