import tkinter as tk
import pyautogui
import time
import pytesseract
from PIL import Image

"""
Nome do Programa: [Automatização Sefaz-MA]
Autor: [Wesley Fuchs]
Data de Criação: [06/11/2023]

Este programa foi criado para automatizar as solicitações de exportação de documentos no Sefaz MA

Instruções de Uso: 
- 

Histórico de Versões:
- [Versão 1.0 (/11/2023): ]


"""

# o campo que sera utilizado tem 100x25
# coordenadas aproximadas 
# Coordenadas (x, y): 315, 460
# Coordenadas (x, y): 415, 485

# Especifica as coordenadas dos dois cantos opostos do quadrado
x1, y1 = 804, 515  # Canto superior esquerdo
x2, y2 = 876, 542  # Canto inferior direito

# Lista das datas que serão utilizadas
date_sets = [("01/01/2023", "31/01/2023"), ("01;02;2023", "28;02;2023")]
# date_sets = [
#     ("01/11/2023", "30/11/2023"),
#     ("01/10/2023", "31/10/2023"),
#     ("01/09/2023", "30/09/2023"),
#     ("01/08/2023", "31/08/2023"),
#     ("01/07/2023", "31/07/2023"),
#     ("01/06/2023", "30/06/2023"),
#     ("01/05/2023", "31/05/2023"),
#     ("01/04/2023", "30/04/2023"),
#     ("01/03/2023", "31/03/2023"),
#     ("01/02/2023", "28/02/2023"),
#     ("01/01/2023", "31/01/2023"),
#     ("01/12/2022", "31/12/2022"),
#     ("01/11/2022", "30/11/2022"),
#     ("01/10/2022", "31/10/2022"),
#     ("01/09/2022", "30/09/2022"),
#     ("01/08/2022", "31/08/2022"),
#     ("01/07/2022", "31/07/2022"),
#     ("01/06/2022", "30/06/2022"),
#     ("01/05/2022", "31/05/2022"),
#     ("01/04/2022", "30/04/2022"),
#     ("01/03/2022", "31/03/2022"),
#     ("01/02/2022", "28/02/2022"),
#     ("01/01/2022", "31/01/2022"),
#     ("01/12/2021", "31/12/2021"),
#     ("01/11/2021", "30/11/2021"),
#     ("01/10/2021", "31/10/2021"),
#     ("01/09/2021", "30/09/2021"),
#     ("01/08/2021", "31/08/2021"),
#     ("01/07/2021", "31/07/2021"),
#     ("01/06/2021", "30/06/2021"),
#     ("01/05/2021", "31/05/2021"),
#     ("01/04/2021", "30/04/2021"),
#     ("01/03/2021", "31/03/2021"),
#     ("01/02/2021", "28/02/2021"),
#     ("01/01/2021", "31/01/2021"),
#     ("01/12/2020", "31/12/2020"),
#     ("01/11/2020", "30/11/2020"),
#     ("01/10/2020", "31/10/2020"),
#     ("01/09/2020", "30/09/2020"),
#     ("01/08/2020", "31/08/2020"),
#     ("01/07/2020", "31/07/2020"),
#     ("01/06/2020", "30/06/2020"),
#     ("01/05/2020", "31/05/2020"),
#     ("01/04/2020", "30/04/2020"),
#     ("01/03/2020", "31/03/2020"),
#     ("01/02/2020", "29/02/2020"),
#     ("01/01/2020", "31/01/2020"),
#     ("01/12/2019", "31/12/2019"),
#     ("01/11/2019", "30/11/2019"),
#     ("01/10/2019", "31/10/2019"),
#     ("01/09/2019", "30/09/2019"),
#     ("01/08/2019", "31/08/2019"),
#     ("01/07/2019", "31/07/2019"),
#     ("01/06/2019", "30/06/2019"),
#     ("01/05/2019", "31/05/2019"),
#     ("01/04/2019", "30/04/2019"),
#     ("01/03/2019", "31/03/2019"),
#     ("01/02/2019", "28/02/2019"),
#     ("01/01/2019", "31/01/2019"),
#     ("01/12/2018", "31/12/2018"),
#     ("01/11/2018", "30/11/2018")
# ]
    

def automatizar_sefaz():  
    """aaaa
    """  

    # Tempo para o usuario clicar no lugar certo
    time.sleep(10)

    for data in date_sets:
        time.sleep(3)

        # ? tabs para checkbox 'Data inicial'
        for _ in range(0):
            pyautogui.press('tab')
    
        # Escrever a 'Data Inicial'
        pyautogui.typewrite(data[0], interval=0.1)
        
        # Selecionar o campo 'Data Final'
        pyautogui.press('tab')
    
        # Escrever a 'Data Final'
        pyautogui.typewrite(data[1], interval=0.1)
        
        # Selecionar o campo 'Digite o código' *Captcha
        for _ in range(2):
            pyautogui.press('tab')
        
        # Captura uma imagem da região específica da tela
        screenshot = pyautogui.screenshot('screenshot-captcha.png', region=(x1, y1, x2 - x1, y2 - y1))
        
        # Carrega a imagem usando a biblioteca PIL (Pillow)
        image = Image.open('screenshot-captcha.png')
        
        # Usa o Tesseract para fazer OCR na imagem
        texto_ocr = pytesseract.image_to_string(image)

        # Digita o texto reconhecido
        pyautogui.typewrite(texto_ocr, interval=0.1)

        # 3 tabs para botão 'Baixar XML'
        for _ in range(3):
            pyautogui.press('tab')
        
        # Pressionar o botão 'Baixar XML'
        pyautogui.press('space')
        time.sleep(1)

    status_label.config(text="Ação concluída!")


# Configurações da janela do tkinter
window = tk.Tk()
window.title("Automatização Sefaz-MA")
window.geometry("300x150")

nfce_button = tk.Button(window, text="-------", command=automatizar_sefaz)
status_label = tk.Label(window, text="")

nfce_button.pack(fill="both", pady=15, padx=40)
nfce_button.configure(border=2)
status_label.pack()

window.mainloop()
