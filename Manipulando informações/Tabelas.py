#Normalmente tabelas estão em arquivos de texto do tipo .csv 
# ou em arquivos Microsoft Excel .xlsx.
#A melhor biblioteca para se trabalhar com Tabelas em Python é o Pandas

import pandas as pd

dados = pd.read_csv('dados_topico1/gaf_esp.csv', sep=';') # Estamos carregando o arquivo csv usando o ; como separador

#Os dados carregados no pandas estão em uma estrutura de dados chamada DataFrame.
#Como todo objeto em POO , ele possui métodos que podem ser chamados.
#Para chamar um método de um objeto, basta escrever o nome da variável do objeto e colocar um . (ponto) na frente, 
# evocando na sequência o nome do método seguido de parenteses (arg), 
# onde os argumentos arg podem ou não ser passados, dependendo do método.

#Dois exemplos de head():

dados.head() # o número passado para o método head é o número de linhas que queremos ver (por default 5)

#No pandas podemos acessar as colunas através do nome, de forma parecida com um dicionário:
dados['Espécie']

#Tipos da estruturas de dados de uma Tabela Pandas e de uma Coluna Pandas:

type(dados) # As tabelas dos pandas são objetos chamados de dataframes

type(dados['Espécie']) # Já as colunas são objetos chamados de séries

#Transformar uma série em uma lista nativa do Python:
list(dados['Espécie'])

#Contar quantos exemplos (entradas) temos de cada espécie:
list(dados['Espécie']).count('Gafanhoto')

list(dados['Espécie']).count('Esperança')

#O método .info() do pandas nos diz quais são os tipos de dados que temos em cada coluna, 
# a quantidade de linhas não nulas e quanto espaço na memória do computador (RAM) nosso dataframe está ocupando:

dados.info()

#O método .describe() do pandas nos gera estatísticas básicas de todas as colunas do dataframe:

dados.describe()

