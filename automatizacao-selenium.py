from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
# from seleniumwire import webdriver
from PIL import Image
import pytesseract
import time

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_imagem(elemento_imagem):
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
    # texto_extraido = texto_extraido.strip()
    # Remover todos os espaços possíveis (espaços em branco, tabulações, quebras de linha)
    texto_extraido = texto_extraido.replace(" ", "").replace("\n", "").replace("\t", "")

    # Imprimir o texto extraído
    print(texto_extraido)
    
    return texto_extraido

# Inicializar o driver do Selenium (certifique-se de ter o WebDriver correspondente ao seu navegador instalado)
# Configurar o webdriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# # Configurar o webdriver com o suporte ao selenium-wire
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(options=options)

# Abrir a página da web
driver.get("https://sistemas1.sefaz.ma.gov.br/download-nfe/")

# Aguardar um pouco para garantir que a página está carregada completamente
driver.implicitly_wait(10)

# Seleciona o frame
iframe = driver.find_element(By.NAME, 'mainFrame')
driver.switch_to.frame(iframe)

# Encontrar o elemento IE Empresa
input_empresa = driver.find_element(By.NAME, 'form1:j_id11')
input_empresa.send_keys("123235669") 
time.sleep(1)
# Encontrar o elemento CPF Socio
input_socio = driver.find_element(By.NAME, 'form1:j_id13')
input_socio.send_keys("96051868372") 
time.sleep(1)
# Encontrar o elemento Protocolo DIEF
input_dief = driver.find_element(By.NAME, 'form1:j_id15')
input_dief.send_keys("9550787") 
time.sleep(1)

# Encontrar o elemento do calendario pop up (data inicial)
element = driver.find_element(By.ID, 'form1:dtIniPopupButton')
# Executa as ações
element.click()
time.sleep(1)
botao_calendario = driver.find_element(By.ID, 'form1:dtIniDayCell2')
botao_calendario.click()

# Encontrar o elemento do calendario pop up (data final)
element = driver.find_element(By.ID, 'form1:dtFinPopupButton')
# Executa as ações
element.click()
time.sleep(1)
botao_calendario = driver.find_element(By.ID, 'form1:dtFinDayCell15')
botao_calendario.click()

# Localizar o elemento da imagem pelo ID 
elemento_imagem = driver.find_element(By.ID, "form1:captcha")

texto_extraido = ocr_imagem(elemento_imagem)

# Encontrar o campo para inserir o Captcha
input_captcha = driver.find_element(By.NAME, 'form1:j_id35')
# Limpar o conteúdo do campo
input_captcha.clear()
input_captcha.send_keys(texto_extraido) 
# input_captcha.send_keys("123456")
time.sleep(2)

# Encontrar o elemento Baixar XML
element_baixar_xml = driver.find_element(By.NAME, 'form1:j_id41')
element_baixar_xml.click()
# time.sleep(3)

# Esperar até 10 segundos para ver se o download inicia ou uma mensagem é exibida
try:
    # Esperar pelo início do download
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-messages-warn-detail')))
    
    # Verificar se é uma mensagem de erro de captcha
    try:
        captcha_error_message = driver.find_element(By.XPATH, "//span[contains(@class, 'ui-messages-warn-detail') and text()='Código da imagem está inválido.']").text
        if captcha_error_message:
            print(f"Erro no captcha: {captcha_error_message}")
            # Pode tentar novamente aqui antes de sair ou lançar uma exceção
            # Localizar o elemento da imagem pelo ID 
            elemento_imagem = driver.find_element(By.ID, "form1:captcha")
            texto_extraido = ocr_imagem(elemento_imagem)
            time.sleep(2)
            # Encontrar o campo para inserir o Captcha
            input_captcha = driver.find_element(By.NAME, 'form1:j_id35')
            # Limpar o conteúdo do campo
            input_captcha.clear()
            input_captcha.send_keys(texto_extraido) 
            time.sleep(2)
            # Encontrar o elemento Baixar XML
            element_baixar_xml = driver.find_element(By.NAME, 'form1:j_id41')
            element_baixar_xml.click()
    except NoSuchElementException:
        # Se o bloco 'try' foi bem-sucedido, continue aqui para verificar outros elementos
        pass
    # Verificar se é uma mensagem de ausência de download
    try:
        no_download_message = driver.find_element(By.XPATH, "//span[contains(@class, 'ui-messages-warn-detail') and text()='A consulta foi realizada com sucesso porém não foram encontradas notas.']").text
        if no_download_message:
            print(f"Nada para baixar: {no_download_message}")
            # Pode sair do loop ou fazer outra ação apropriada
    except NoSuchElementException:
        pass
        # Se não houver mensagens relevantes, continue no loop ou faça outra ação apropriada
except TimeoutException:
    # Se não houver download iniciado, e não há mensagens de erro ou de ausência de download
    # presume-se que o download foi iniciado corretamente
    print("Download iniciado com sucesso!")

time.sleep(2)
# Fechar o navegador
driver.quit()


# <span class="ui-messages-warn-detail">A consulta foi realizada com sucesso porém não foram encontradas notas.</span>
# <span class="ui-messages-warn-detail">Código da imagem está inválido.</span>
# <span class="ui-messages-warn-detail">Todos os campos com (*) devem ser informados.</span>