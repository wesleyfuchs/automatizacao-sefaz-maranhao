from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Inicializar o driver do Selenium (certifique-se de ter o WebDriver correspondente ao seu navegador instalado)
driver = webdriver.Chrome()

# Abrir a página da web
driver.get("https://sistemas1.sefaz.ma.gov.br/download-nfe/")

# time.sleep(5)
# Aguardar um pouco para garantir que a página está carregada completamente
driver.implicitly_wait(10)

# Switch to iframe if applicable
iframe = driver.find_element(By.NAME, 'mainFrame')
driver.switch_to.frame(iframe)

# Now find the element
# element = driver.find_element(By.NAME, 'form1:dtIniInputDate')
element = driver.find_element(By.ID, 'form1:dtIniPopupButton')

# # Obter as coordenadas do elemento
# element_location = element.location
# element_size = element.size

# # Exibir as coordenadas
# print("Coordenadas X:", element_location['x'])
# print("Coordenadas Y:", element_location['y'])

element.click()
time.sleep(1)
botao_calendario = driver.find_element(By.ID, 'form1:dtIniDayCell25')
botao_calendario.click()


# element = driver.find_element(By.NAME, 'form1:dtIniInputDate')
element = driver.find_element(By.ID, 'form1:dtFinPopupButton')

# Obter as coordenadas do elemento
element_location = element.location
element_size = element.size
element.click()
time.sleep(1)
botao_calendario = driver.find_element(By.ID, 'form1:dtFinDayCell15')
botao_calendario.click()


# Localizar o elemento da imagem pelo ID ou por outro seletor adequado
elemento_imagem = driver.find_element(By.ID, "form1:captcha")

# Obter a localização e as dimensões da imagem
localizacao = elemento_imagem.location
tamanho = elemento_imagem.size

# Capturar a área da tela correspondente à imagem
driver.save_screenshot("screenshot.png")
imagem_screenshot = Image.open("screenshot.png")
area_imagem = (
    localizacao['x'], localizacao['y'],
    localizacao['x'] + tamanho['width'], localizacao['y'] + tamanho['height']
)
imagem_cortada = imagem_screenshot.crop(area_imagem)
imagem_cortada.save("imagem_cortada.png")

# Usar o PyTesseract para extrair texto da imagem
texto_extraido = pytesseract.image_to_string(Image.open("imagem_cortada.png"))


# # Imprimir o texto extraído
print(texto_extraido)

input_captcha = driver.find_element(By.NAME, 'form1:j_id35')
input_captcha.send_keys(texto_extraido) 
# input_captcha.send_keys("123456")

time.sleep(5)
# Fechar o navegador
driver.quit()
