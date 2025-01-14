import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=1146, y=1357) # Escolhendo o perfil do chrome

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
pyautogui.click(x=1558, y=667) # localização campo login/usuario
pyautogui.write('claytonlcorrea@gmail.com')

time.sleep(1)
pyautogui.click(x=3768, y=207)
pyautogui.hotkey('tab')
pyautogui.write('********')
pyautogui.hotkey('tab')
pyautogui.press('enter')

base = pandas.read_csv('produtos.csv')

for linha in base.index:
    pyautogui.click(x=1538, y=457) # Clicando no primeiro campo
    
    codigo = base.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.hotkey('tab')
    
    marca = base.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.hotkey('tab')
    
    tipo = base.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.hotkey('tab')
    
    categoria = base.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.hotkey('tab')
    
    preco = base.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.hotkey('tab')
    
    custo = base.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.hotkey('tab')
    
    obs = ""
    pyautogui.write(str(obs))
    
    pyautogui.hotkey('tab')
    pyautogui.press('enter')
    
    