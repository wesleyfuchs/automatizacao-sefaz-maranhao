import pyautogui
import pytesseract
from PIL import Image
import time

# Certifique-se de configurar o caminho para o executável do Tesseract no seu sistema
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ... Seu código existente para automatizar ações na página web ...
time.sleep(3)

# o campo que sera utilizado tem 100x25
# coordenadas aproximadas 
# Coordenadas (x, y): 315, 460
# Coordenadas (x, y): 415, 485

# Especifica as coordenadas dos dois cantos opostos do quadrado
x1, y1 = 804, 515  # Canto superior esquerdo
x2, y2 = 876, 542  # Canto inferior direito

# Captura uma imagem da região específica da tela
screenshot = pyautogui.screenshot('screenshot.png', region=(x1, y1, x2 - x1, y2 - y1))

# Carrega a imagem usando a biblioteca PIL (Pillow)
image = Image.open('screenshot.png')

# Usa o Tesseract para fazer OCR na imagem
texto_ocr = pytesseract.image_to_string(image)

# Imprime o texto reconhecido
print("Texto OCR:", texto_ocr)

# Continue com o restante do seu código...
