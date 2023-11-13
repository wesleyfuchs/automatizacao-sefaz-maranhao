import pyautogui
import time


time.sleep(5)

imagem_path = 'C:/Users/wesley/Desktop/scripts/automatizacao-sefaz-maranhao/calendario-icone.png'
coordenadas = pyautogui.locateOnScreen(imagem_path)

# Verifica se a imagem foi encontrada
if coordenadas is not None:
    # Obtém as coordenadas do centro da imagem
    x, y = pyautogui.center(coordenadas)

    # Clica nas coordenadas encontradas
    pyautogui.click(x, y)
else:
    print("Imagem não encontrada na tela.")