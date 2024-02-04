import matplotlib.pyplot as plt
import yfinance
import time
import pyautogui
import pyperclip
import webbrowser
from webbrowser import register

acao = input("Digite o ticker da ação desejada: ")

# apenas pra agilizar a parte de digitar um ticker
if acao == '':
    acao = "PETR4.SA"

dadosAcao = yfinance.Ticker(acao).history("6mo")
print(dadosAcao)
fechamentoAcao = dadosAcao.Close

cotacaoMaxima = fechamentoAcao.max()
cotacaoMinina = fechamentoAcao.min()
cotacaoAtual = fechamentoAcao[-1]

# gera um gráfico com as cotações do período informado
fechamentoAcao.plot()

# saber posição do mouse (time.sleep é o tempo pra posicionar o mouse)
#time.sleep(5)
#pyautogui.position()
#print(pyautogui.position())

# abrindo o email
email = input("Digite o email do destinatário: ")
path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
chrome = webbrowser.get('chrome')
chrome.open_new_tab('chrome://newtab')

pyautogui.PAUSE = 2
pyautogui.hotkey("alt", "tab")
pyautogui.write("www.gmail.com")
pyautogui.hotkey("enter")
pyautogui.click(x=98, y=207)

# escrevendo e enviando o email
pyperclip.copy(email)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy("Dados solicitados")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

#letra 'f' que permite por variáveis em string, independente do tipo de aspas
mensagem = f"""
Seguem os dados solicitados,

Os últimos 6 meses da ação {acao}:

Cotação máxima: R${round(cotacaoMaxima, 2)}
Cotação mínima: R${round(cotacaoMinina, 2)}
Cotação atual: R${round(cotacaoAtual, 2)}

Qualquer dúvida, só chamar
"""

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")