import requests
from PIL import Image
from io import BytesIO

url = 'https://vtrina.sfo2.digitaloceanspaces.com/HUB_62cc31771c009c00017acaf3/01VISUPCDC_20240422110512810887.jpg'

def extrairCodigoProduto(url):
  parteCodigo = url.split('/')[-1]
  codigoProduto = parteCodigo.split('_')[0]
  return codigoProduto

response = requests.get(url)

if response.status_code == 200:
  img = Image.open(BytesIO(response.content))
  novaLargura, novaAltura = 1005, 1005
  imgRedimensionada = img.resize((novaLargura, novaAltura))

  codigoProduto = extrairCodigoProduto(url)

  imgRedimensionada.save(f'{codigoProduto}.jpg') # verificar nome da imagem salva
  print('Imagem redimensionada com sucesso!')
else:
  print('Falha ao redimensionar a imagem. Código de status: {response.status_code}}')