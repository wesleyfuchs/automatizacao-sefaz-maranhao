from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
# from seleniumwire import webdriver
import tkinter as tk
from PIL import Image
import pytesseract
import time

# Caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def automatizar_sefaz(num_empresa, num_socio, num_dief):
    
    dataset = [("6", "36"), ("4", "33"), ("1", "31"), ("5", "35"), ("3", "32"), ("0", "30"), 
               ("5", "34"), ("2", "32"), ("2", "29"), ("6", "36"), ("3", "33"), ("1", "30"),
               ("5", "35"), ("3", "32"), ("0", "30"), ("4", "34"), ("2", "31"), ("6", "36"),
               ("4", "33"), ("1", "31"), ("1", "28"), ("5", "35"), ("2", "32"), ("0", "29"),
               ("4", "34"), ("2", "31"), ("6", "36"), ("3", "33"), ("1", "30"), ("5", "35"),
               ("3", "32"), ("0", "30"), ("0", "27"), ("4", "34"), ("1", "31"), ("6", "35"),
               ("3", "33"), ("1", "30"), ("2", "32"), ("0", "29"), ("4", "34"), ("2", "31"),
               ("6", "36"), ("5", "33"), ("2", "32"), ("6", "36"), ("4", "33"), ("1", "31"),
               ("6", "35"), ("3", "33"), ("0", "30"), ("5", "34"), ("2", "32"), ("0", "29"),
               ("4", "34"), ("4", "31"), ("1", "31"), ("5", "35"), ("3", "32")] # Outubro 2023 > Novembro 2018
    
    def ocr_imagem():
        # Localizar o elemento da imagem pelo ID 
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
    driver.maximize_window()
    time.sleep(3)
    
    # Configurar o webdriver com o suporte ao selenium-wire
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
    # numero_empresa = "123235669"
    numero_empresa = num_empresa
    input_empresa.send_keys(numero_empresa) 
    time.sleep(1)
    # Encontrar o elemento CPF Socio
    input_socio = driver.find_element(By.NAME, 'form1:j_id13')
    # cpf_socio = "96051868372"
    cpf_socio = num_socio
    input_socio.send_keys(cpf_socio) 
    time.sleep(1)
    # Encontrar o elemento Protocolo DIEF
    input_dief = driver.find_element(By.NAME, 'form1:j_id15')
    # protocolo_dief = "9550787"
    protocolo_dief = num_dief
    input_dief.send_keys(protocolo_dief) 
    time.sleep(1)
    
    # Aguardar até que o elemento de rádio esteja visível e interagível
    botao_tipo_notas = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'form1:j_id25:0'))
    )
    # Verificar se o rádio não está marcado
    if not botao_tipo_notas.is_selected():
        # Clicar no rádio para marcá-lo
        botao_tipo_notas.click()
    time.sleep(2)

    for data in dataset:

        # Mudar forma para voltar o mes, clicar no nome do mes > selecionar mes desejado > ano desejado
        # Se o botao < for clicado uma vez nao tem como clicar uma segunda vez
        # Encontrar o elemento do calendario pop up (data inicial)
        element = driver.find_element(By.ID, 'form1:dtIniPopupButton')
        # Executa as ações
        element.click()
        time.sleep(1)

        
        # Interagir com o calendário inicial
        # botao_anterior_ini = WebDriverWait(driver, 15).until(
        # EC.element_to_be_clickable((By.XPATH, "//div[text()='<']"))
        # )
        # botao_anterior_ini.click()
        # time.sleep(1)
        # Encontrar o elemento do botão
        xpath_botao_anterior_ini = "//td[@id='form1:dtIniHeader']//div[text()='<']"
        botao_anterior_ini = driver.find_element(By.XPATH, xpath_botao_anterior_ini)
        botao_anterior_ini.click()
        time.sleep(1)
        # driver.execute_script("arguments[0].click();", botao_anterior_ini)

        botao_calendario_ini = driver.find_element(By.ID, f'form1:dtIniDayCell{data[0]}')
        botao_calendario_ini.click()
        time.sleep(1)

        # Interagir com o calendário final
        element = driver.find_element(By.ID, 'form1:dtFinPopupButton')
        element.click()
        time.sleep(1)

        # botao_anterior_fin = WebDriverWait(driver, 15).until(
        # EC.element_to_be_clickable((By.XPATH, "//div[text()='<']"))
        # )
        # botao_anterior_fin.click()
        # time.sleep(1)

        # Encontrar o elemento do botão
        xpath_botao_anterior_fin = "//td[@id='form1:dtFinHeader']//div[text()='<']"
        botao_anterior_fin = driver.find_element(By.XPATH, xpath_botao_anterior_fin)
        # driver.execute_script("arguments[0].click();", botao_anterior_fin)
        botao_anterior_fin.click()
        time.sleep(1)

        botao_calendario_fin = driver.find_element(By.ID, f'form1:dtFinDayCell{data[1]}')
        botao_calendario_fin.click()
        time.sleep(1)


        texto_extraido = ocr_imagem()

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

                    texto_extraido = ocr_imagem()
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
        # <span class="ui-messages-warn-detail">A consulta foi realizada com sucesso porém não foram encontradas notas.</span>
        # <span class="ui-messages-warn-detail">Código da imagem está inválido.</span>
        # <span class="ui-messages-warn-detail">Todos os campos com (*) devem ser informados.</span>
        
    # Fechar o navegador
    driver.quit()
    
        
# Função para iniciar a automação quando o botão for pressionado
def iniciar_automacao():
    num_empresa = empresa_entry.get()
    num_socio = socio_entry.get()
    num_dief = dief_entry.get()
    automatizar_sefaz(num_empresa, num_socio, num_dief)

# Configurações da janela do tkinter
window = tk.Tk()
window.title("Automatização Sefaz-MA")
window.geometry("350x150")

# Criar três variáveis para armazenar os valores inseridos pelo usuário
empresa_var = tk.StringVar()
socio_var = tk.StringVar()
dief_var = tk.StringVar()

# Criar três caixas de entrada (Entry) para que o usuário possa digitar os valores
empresa_label = tk.Label(window, text="Número da Empresa:")
empresa_entry = tk.Entry(window, textvariable=empresa_var)

socio_label = tk.Label(window, text="CPF do Sócio:")
socio_entry = tk.Entry(window, textvariable=socio_var)

dief_label = tk.Label(window, text="Protocolo DIEF:")
dief_entry = tk.Entry(window, textvariable=dief_var)

iniciar_button = tk.Button(window, text="Iniciar Automação", command=iniciar_automacao)

# Posicionar os elementos na janela
empresa_label.grid(row=0, column=0, pady=5, padx=25)
empresa_entry.grid(row=0, column=1, pady=5, padx=25)

socio_label.grid(row=1, column=0, pady=5, padx=25)
socio_entry.grid(row=1, column=1, pady=5, padx=25)

dief_label.grid(row=2, column=0, pady=5, padx=25)
dief_entry.grid(row=2, column=1, pady=5, padx=25)

iniciar_button.grid(row=3, column=0, columnspan=2, pady=10, padx=25)

# Iniciar o loop principal do tkinter
window.mainloop()