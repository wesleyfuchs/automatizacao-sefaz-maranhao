import pyautogui
import pytesseract
from PIL import Image

# Certifique-se de configurar o caminho para o executável do Tesseract no seu sistema
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Defina as coordenadas da região desejada
x1, y1 = 0, 10  # Canto superior esquerdo
x2, y2 = 0, 10  # Canto inferior direito

# ... Seu código existente para automatizar ações na página web ...

# Captura uma imagem da região específica da tela
screenshot = pyautogui.screenshot('screenshot.png', region=(x1, y1, x2 - x1, y2 - y1))

im = pyautogui.screenshot('teste.png', region=(0,0, 300, 400))

# Carrega a imagem usando a biblioteca PIL (Pillow)
image = Image.open('screenshot.png')

# Usa o Tesseract para fazer OCR na imagem
texto_ocr = pytesseract.image_to_string(image)

# Imprime o texto reconhecido
print("Texto OCR:", texto_ocr)

# Continue com o restante do seu código...
