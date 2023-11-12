from PIL import Image
import pytesseract

# Caminho para o executável do Tesseract (altere conforme necessário)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Função para ler o texto em uma imagem
def ler_texto_em_imagem(caminho_da_imagem):
    imagem = Image.open(caminho_da_imagem)
    texto = pytesseract.image_to_string(imagem)
    return texto

# Exemplo de uso
# caminho_imagem = '/home/advintegra/Área de trabalho/wesley/automatizacao-sefaz-maranhao/captcha3.png'
caminho_imagem = 'C:/Users/uesley/Documents/GitHubRepositorios/sefaz-ma/captcha.png'
texto_extraido = ler_texto_em_imagem(caminho_imagem)

# Exibindo o texto extraído
print("Texto extraído:")
print(texto_extraido)
