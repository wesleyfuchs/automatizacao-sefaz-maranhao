from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from io import BytesIO

# # Caminho para o executável do Tesseract (altere conforme necessário)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# URL da página web
url = 'sua_url_aqui'

# Inicializar o driver do Selenium (certifique-se de ter o WebDriver adequado para o seu navegador)
driver = webdriver.Chrome()
driver.get(url)

# Obter o código HTML da página
html = driver.page_source

# Fechar o navegador
driver.quit()

# Analisar o HTML com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontrar a tag img com o id "form1:captcha"
img_tag = soup.find('img', {'id': 'form1:captcha'})

# Obter o valor do atributo src
img_src = img_tag['src']

# Ler a imagem diretamente do atributo src usando BytesIO
img_data = BytesIO(driver.get(img_src).content)
imagem = Image.open(img_data)

# Extrair texto da imagem
texto_extraido = pytesseract.image_to_string(imagem)

# Exibindo o texto extraído
print("Texto extraído:")
print(texto_extraido)
