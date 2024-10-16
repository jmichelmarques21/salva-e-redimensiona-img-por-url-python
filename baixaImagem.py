import requests
from PIL import Image
from io import BytesIO
import pandas as pd
import os

# Função para extrair o código do produto da URL
def extrair_codigo_produto(url):
    parte_codigo = url.split('/')[-1]
    codigo_produto = parte_codigo.split('_')[0]
    return codigo_produto

# Função para salvar a imagem com sequenciamento no nome
def salvar_imagem_com_sequencia(codigo_produto, img):
    # Verifica se o arquivo já existe
    contador = 1
    nome_arquivo = f'{codigo_produto}.jpg'
    
    while os.path.exists(nome_arquivo):
        contador += 1
        nome_arquivo = f'{codigo_produto}-{contador}.jpg'
    
    img.save(nome_arquivo)
    print(f"Imagem salva como: {nome_arquivo}")

# Lê a planilha Excel
planilha = pd.read_excel('exp-produtos.xlsx')
print(planilha.columns)

# Supondo que a coluna com as URLs esteja nomeada como 'url'
for url in planilha['url']:
    # Baixa o conteúdo da imagem
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Abre a imagem em um objeto Image
        img = Image.open(BytesIO(response.content))

        # Define as novas dimensões (ex: 300x300)
        nova_largura, nova_altura = 300, 300
        img_redimensionada = img.resize((nova_largura, nova_altura))

        # Extrai o código do produto
        codigo_produto = extrair_codigo_produto(url)

        # Salva a imagem com o nome do código e sequência se necessário
        salvar_imagem_com_sequencia(codigo_produto, img_redimensionada)
        print(f"Imagem baixada e redimensionada com sucesso!")
    else:
        print(f"Falha ao baixar a imagem. Código de status: {response.status_code}")
