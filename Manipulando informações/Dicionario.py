#No Python um dicionário é uma estrutura de dados onde há um valor e uma chave (key). 
# Ele permite indexação rápida e é bem útil para diversas situações.
#Em memória, os dicionários podem ser serializados como arquivos JSON. 
# O padrão JSON também pe onipresente em aplicações web. 
# Várias APIs Rest usam ele como padrão de comunicação.
#No Python a serialização de objeto é feita por arquivos Pickle 
# (como os objetos são guardadados em memória). 
# Ver https://en.wikipedia.org/wiki/Serialization

meu_dicionario= {
    'chave1': 1234,       # Armazenando um inteiro
    'chave2': [1,2,3,4],  # Armazenando uma lista de inteiros
    'chave3': 'Oi mundo', # Armazenando uma string
    'chave4': 1.234,      # Armazenando um float
    '1': 'vamos ver se vai dar erro'
}

meu_dicionario['1']

meu_dicionario

type(meu_dicionario) # Dicionário nativo do Python é objeto dict

meu_dicionario['chave3'] # Acessando o valor armazenado na chave1

type(meu_dicionario['chave1'])

type(meu_dicionario['chave3'])

meu_dicionario.keys() # Para saber quais são as chaves contidas no dicionario

list(meu_dicionario.keys())[-1]

type(meu_dicionario.keys())

# Percorrendo todo o dicionario
for chave in meu_dicionario.keys():
    print(meu_dicionario[chave])

meu_dicionario['nova_chave'] = 'oi mundo 2'

meu_dicionario

meu_dicionario.pop('chave1', None) # Removendo uma entrada do dicionário

meu_dicionario

zoologico = {
    'jaula1':{'animal':'macaco', 'quantidade':2, 'tamanho':10},
    'jaula2':{'animal':'girafa', 'quantidade':3, 'tamanho':50},
    'banheiro1':{},
    'veterinario':{}
}

#Para salvar um dicionário mantendo a estrutura dele 
# (não criar um arquivo de texto puro) podemos usar a biblioteca do JSON.
import json

with open('dict_data.json', 'w') as f:
    json.dump(meu_dicionario, f)

#abrir o arquivo
with open('dict_data.json', 'r') as file:
    lines = file.readlines()

type(lines), len(lines)

lines[0]

len(lines), type(lines[0]) # Carregou tudo como uma única grande string

with open('dict_data.json', 'r') as file:
    lines = json.load(file)

type(lines)

lines

len(lines), type(lines)

