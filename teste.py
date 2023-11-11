import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from io import BytesIO

# Caminho para o executável do Tesseract (altere conforme necessário)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# URL da página
url_pagina = 'https://quadlayers.com/add-captcha-to-woocommerce-login/'

# Função para obter a URL da imagem a partir do HTML da página
def obter_url_imagem(url_pagina):
    response = requests.get(url_pagina)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Substitua 'class_da_imagem' pela classe real da imagem
    imagem = soup.find('img', {'class': 'aligncenter'})
    url_imagem = imagem['src']

    return url_imagem

# Função para realizar OCR em uma imagem a partir da URL
def ocr_em_imagem_url(url):
    response = requests.get(url)
    imagem = Image.open(BytesIO(response.content))
    texto = pytesseract.image_to_string(imagem)
    return texto

# Obtendo a URL da imagem a partir do HTML da página
url_imagem = obter_url_imagem(url_pagina)

# Exemplo de uso
texto_extraido = ocr_em_imagem_url(url_imagem)

# Exibindo o texto extraído
print("Texto extraído:")
print(texto_extraido)
