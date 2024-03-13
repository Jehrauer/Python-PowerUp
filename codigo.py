# PASSO A PASSO DO PROJETO 

import time
import pyautogui
import pandas

pyautogui.PAUSE = 0.5

# PASSO 1: Entrar no sistema da empresa
# Abrir o Navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Dar uma pausa especifica  diferente da PAUSE num determinado local
time.sleep(2)

# PASSO 2: Fazer o Login
pyautogui.click(x=2921, y=470)
pyautogui.write("puthonimpressionador@gmail.com")
# Passo 2.1: Escrever a senha
pyautogui.press("tab")
pyautogui.write("sua senha aqui")
# Passo 2.2: Clicar em logar
pyautogui.click(x=3249, y=671)
time.sleep(3)

# PASSO 3: Importar a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# PASSO 4: Cadastrar 1 produto
# para cada linha da minha tabela produto.csv
for linha in tabela.index:  # o que vc quer fazer para cada linha da tabela (os comandos abaixo do for devem estar a frente do comando-TAB)   
    # clicar no primeiro campo
    pyautogui.click(x=3033, y=320)
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Marca
    pyautogui.write(tabela.loc[linha, "marca"]) # outra opcao para escrever o codigo sem criar a variavel (exemplo: marca = tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"]) 
    pyautogui.press("tab")
    # Categoria
    # tranforma uma string numerico para texto - comando str()
    # str(1) -> transforma 1 em "1"
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # Preco unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) # deve se colocar o mesmo texto da tabela
    pyautogui.press("tab")
    # Custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # Observaçoes
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # Enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000) # voltar para o incio da pagina

# PASSO 5: Repetir o processo de cadastro ate acabar a base da dados