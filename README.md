[# automatizacao-sefaz-maranhao](https://tesseract-ocr.github.io/tessdoc/Installation.html)https://tesseract-ocr.github.io/tessdoc/Installation.html

chrome driver


https://sistemas1.sefaz.ma.gov.br/download-nfe/
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

| :placard: **** |     |
| -------------         | --- |
| :sparkles: Nome       | Automatização Sefaz-MA
| :label: Tecnologias   | Python, Tkinter, Selenium, Tesseract


# Sobre o projeto 📚

<p>
 Automatização do site do [Sefaz-MA](https://sistemas1.sefaz.ma.gov.br/download-nfe/) em Python. <br> 
</p>

## Iniciando o projeto... 📌

### 1. Iniciar um ambiente virtual (venv) e ativa-la. </br>
#### WINDOWS </br>
python -m venv venv  </br>
venv\Scripts\activate </br>
#### LINUX </br>
python3 -m venv venv  </br>
source venv\bin\activate </br>


### 2. Instalar dependencias: </br>
pip install -r requirements.txt </br>
ou instalar as bibliotecas: Tkinter, Selenium e Tesseract </br>

### 3. Para exportar o programa: </br>
pip install cx_Freeze </br>
python setup.py build </br>
ou </br>
cxfreeze auto-click.py --target-dir nome_da_pasta </br>

### 4. Requesitos necessarios para rodas o programa: </br>
É necessário ter instalado: </br>
- [Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html) </br>
- [Baixar versões iguais de ChromeDriver e Chromium](https://chromedriver.chromium.org/downloads)

