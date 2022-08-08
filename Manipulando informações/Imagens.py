with open('datasets/dados_topico1/texto_utf8.txt', 'r', encoding="utf-8") as file:
    linhas = file.readlines()
    
print(linhas)

#Nas imagens a questão dos encodings recebe outro nome: codecs. Os codecs podem 
# se referenciar tanto para imagem, quanto para áudio digital e vídeo. Em geral 
# os codecs estão associados a extensão do arquivo (ex: .png, .jpg, .ogg, .mp3, .mp4, etc).
#Os codecs não só codificam a imagem em bytes mas também servem para adicionar 
# uma camada de inteligência a essa codificação, permitindo a compressão de dados

from IPython.display import display  # Para mostrar imagens no Jupyter inline
from PIL import Image                # Para carregar imagens no python

imagem = Image.open('dados_topico1/lena.png') # Carregando imagem usando o PIL

print(type(imagem)) # O objeto 'imagem' criado pela classe Image do PIL foi identificado como .png 
print(imagem) # Ao printar o objeto já vemos que a imagem tem 512x512 pixels é do tipo RBG
# Além disso, perceba que sabemos qual é a posição da memória RAM onde o objeto está instanciado.

imagem.show() # Esse comando é nativo do PIL e não abre a imagem inline no Jupyter

display(imagem) # Agora printando a imagen inline usando o IPython

width, height = imagem.size # O objeto imagem do PIL tem um atributo size em pixels
print(width, height)

imagem.filename # O objeto também tem um atributo nome (caminho) do arquivo da imagem carregada

imagem.format # Printa o formato da imagem

imagem.mode

imagem.getbands()

imagem.getpixel((200,250)) # Pega o valor do pixel em uma posicao da imagem
#(0,0) é o canto superior esquerdo

# Podemos converter para canal monocromatico
img_grey = imagem.convert("L")
print(img_grey)
img_grey

img_grey.getpixel((200,250))

raw_imagem = imagem.tobytes() # Pegando a imagem em bytes usando o método tobytes

print(raw_imagem)

#O formato PNG adiciona uma série de informações que não permite identificarmos de maneira clara 
# onde está cada pixel da matriz da imagem quando olhamos para o código binário.
#Isso acontece pois o PNG adiciona um cabeçalho (header) com uma série de chunks 
# (fragmentos de informação sequenciais) para representar a imagem. Para entendermos 
# exatamente o que o código binário significa, precisariamos olhar a documentação do PNG

import numpy as np  # Numpy é uma biblioteca para trabalhar com números

# Matplotlib trabalha com gráficos
import matplotlib.pyplot as plt

im_array = np.array(imagem) # Carregando o objeto imagem (classe PIL Image) como um objeto numpy array

im_array

len(im_array)

im_array.size

imgplot = plt.imshow(im_array)
