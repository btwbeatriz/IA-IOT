'''
Utilizando ferramentas de Data Science para carregar dados, gerar estatísticas e gráficos'''

import pandas as pd  #Pandas = Biblioteca para trabalhar com tabelas

dados = pd.read_csv('gaf_esp.csv', sep=';') # Estamos carregando o arquivo csv usando o ; como separador

'''
Os dados carregados no pandas estão em uma estrutura de dados chamada DataFrame. 
Este é o objeto que o pandas cria para representar os dados da tabela. Como todo objeto em POO 
(programação orientada à objeto), ele possui métodos que podem ser chamados.
'''

dados.head()

dados.head(10)

dados.tail()

'''
No pandas podemos acessar as colunas através do nome, de forma parecida com um dicionário:
'''

dados['Espécie']

'''
Tipos da estruturas de dados de uma Tabela Pandas e de uma Coluna Pandas:
'''

type(dados) # As tabelas dos pandas são objetos chamados de dataframes

type(dados['Espécie']) # Já as colunas são objetos chamados de séries

'''
Para transformar uma série em uma lista nativa do Python:
'''

list(dados['Espécie'])

'''
Contar quantos exemplos (entradas) temos de cada espécie:
'''

list(dados['Espécie']).count('Gafanhoto')

list(dados['Espécie']).count('Esperança')

novo_dataframe = {
    'alturas': [14,20,10],
    'localidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
    'latitude': [35,37,40],
    'logitute': [-70, -68, -71]
}

df = pd.DataFrame(data=novo_dataframe)

df.head()

############################################################################
'''
Calcular algumas estatísticas
'''

import statistics

media_cab = statistics.mean(dados['Comprimento do Abdômen']) # Média do Comp. Abdômen
media_can = statistics.mean(dados['Comprimento das Antenas']) # Média do Comp. Antena
std_cab = statistics.stdev(dados['Comprimento do Abdômen']) # Desvio Padrão Amostral do Comp. Abdômen
std_can = statistics.stdev(dados['Comprimento das Antenas']) # Desvio Padrão Amostra do Com. Antena

print('Média Comp. Abdômen: ', media_cab)
print('Média Comp. Antena: ', media_can)
print('Desvio Padrão Amostral do Comp. Abdômen: ', std_cab)
print('Desvio Padrão Amostral do Comp. Antena: ', std_can)

'''
Recalcular para cada uma das espécies.

Para isso, vamos separar os dados em dois dataframes:
'''

dados_gaf = dados[dados['Espécie']=='Gafanhoto'] # Aqui estamos criando um dataframe só com gafanhotos

dados_gaf.head()

len(dados_gaf)

dados_esp = dados[dados['Espécie']=='Esperança'] # E aqui um dataframe só com esperanças

dados_esp.head()

len(dados_esp)

media_cab_gaf = statistics.mean(dados_gaf['Comprimento do Abdômen']) # Média do Comp. Abdômen
media_can_gaf = statistics.mean(dados_gaf['Comprimento das Antenas']) # Média do Comp. Antena
std_cab_gaf = statistics.stdev(dados_gaf['Comprimento do Abdômen']) # Desvio Padrão Amostral do Comp. Abdômen
std_can_gaf = statistics.stdev(dados_gaf['Comprimento das Antenas']) # Desvio Padrão Amostra do Com. Antena

print('Média Comp. Abdômen: ', media_cab_gaf)
print('Média Comp. Antena: ', media_can_gaf)
print('Desvio Padrão Amostral do Comp. Abdômen: ', std_cab_gaf)
print('Desvio Padrão Amostral do Comp. Antena: ', std_can_gaf)

media_cab_esp = statistics.mean(dados_esp['Comprimento do Abdômen']) # Média do Comp. Abdômen
media_can_esp = statistics.mean(dados_esp['Comprimento das Antenas']) # Média do Comp. Antena
std_cab_esp = statistics.stdev(dados_esp['Comprimento do Abdômen']) # Desvio Padrão Amostral do Comp. Abdômen
std_can_esp = statistics.stdev(dados_esp['Comprimento das Antenas']) # Desvio Padrão Amostra do Com. Antena

print('Média Comp. Abdômen: ', media_cab_esp)
print('Média Comp. Antena: ', media_can_esp)
print('Desvio Padrão Amostral do Comp. Abdômen: ', std_cab_esp)
print('Desvio Padrão Amostral do Comp. Antena: ', std_can_esp)

############################################################################

'''
Gráficos - plotando os histogramas usando o Seaborn e o Matplotlib:
'''
import matplotlib.pyplot as plt  
import seaborn as sns

fig, axes = plt.subplots(1,2, figsize=(14, 4), dpi=80)
fig.suptitle('Todos os Dados')


sns.histplot(ax=axes[0], #Local da figura onde o gráfico será plotado
            data=dados,  # Perceba que estamos passando a coluna do dataframe completo
            kde=True, #Linha estimada da densidade de probabilidade
            bins=10,  #Número de barras
            x= 'Comprimento do Abdômen',
            hue='Espécie'
            #linewidth=0.7, #Largura das linhas das barras
            )

sns.histplot(ax=axes[1],
            data=dados,
            kde=True,
            bins=10,
            x='Comprimento das Antenas',
            hue='Espécie'
            #linewidth=0.7,
            )

axes[0].set(xlabel='Comprimento do Abdômen', ylabel='Contagem')
axes[1].set(xlabel='Comprimento das Antenas', ylabel='Contagem')

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle('Dados dos Gafanhotos')


sns.histplot(ax=axes[0],
            data=dados_gaf['Comprimento do Abdômen'], # Agora a coluna do dataframe só com gafanhotos
            kde=True,
            bins=10,
            linewidth=0.7,
            color='green'
            )

sns.histplot(ax=axes[1],
            data=dados_gaf['Comprimento das Antenas'],
            kde=True,
            bins=10,
            linewidth=0.7,
            color='green'
            )

axes[0].set(xlabel='Comprimento do Abdômen', ylabel='Contagem')
axes[1].set(xlabel='Comprimento das Antenas', ylabel='Contagem')

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle('Dados das Esperanças')


sns.histplot(ax=axes[0],
            data=dados_esp['Comprimento do Abdômen'],
            kde=True,
            bins=10,
            linewidth=0.7,
            color = 'red'
            )

sns.histplot(ax=axes[1],
            data=dados_esp['Comprimento das Antenas'],
            kde=True,
            bins=10,
            linewidth=0.7,
            color = 'red'
            )

axes[0].set(xlabel='Comprimento do Abdômen', ylabel='Contagem')
axes[1].set(xlabel='Comprimento das Antenas', ylabel='Contagem')

'''
Boxplot:
'''
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle('Dados das Esperanças')

sns.boxplot(x="Espécie", y="Comprimento do Abdômen",
            palette=["b", "r"],
            linewidth=0.7,
            ax=axes[0],
            data=dados
           )

sns.boxplot(x="Espécie", y="Comprimento das Antenas",
            palette=["b", "r"],
            linewidth=0.7,
            ax=axes[1],
            data=dados
           )

############################################################################

'''
Gráfico de dispersão do Comprimento das Antenas em função do Comprimento do Abdômen. 
Adicionar os histogramas de cada variável na lateral do eixo correspondente. Indicar para 
o método do Seaborn que existem duas espécies.
'''
sns.jointplot(data=dados,
              x="Comprimento do Abdômen", y="Comprimento das Antenas",
              height=5, 
              ratio=2,
              marginal_ticks=True,
              hue = 'Espécie'
             )

'''
Botânica: Íris Dataset
Esse dataset contém medidas da largura e comprimento da pétala e da sépala de 150 amostras de flores, 
assim como a espécie de cada uma (versicolor, setosa, virginica). 
Mais informações: https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html.
Dentro da biblioteca Scikit Learn há bases da dados prontas utilizadas para exemplos e testes.
'''     
from sklearn import datasets

# Carregando os dados
iris = datasets.load_iris()

print(iris)

type(iris) # Entretanto, para saber qual a 'estrutura de dados' da variável iris corretamente

iris.keys() # Para saber as 'chaves'

iris['feature_names'] # Acessar como em um dicionário

iris.feature_names # Acessar como atributo de um objeto

'''
Para facilitar a visualização dos dados, vamos usar o pandas.

Para isso, vamos criar um dataframe pandas que recebe como dados os atributos do objeto iris que criamos acima.
'''
import pandas as pd

dados = pd.DataFrame(data=iris.data,  # Estamos dizendo que o dados do dataframe são o atributo data do objeto iris
                     columns = iris.feature_names) # Já o nome das colunas do dataframe serão o atrib feature_names

dados.head() # Para vermos as linhas do dataframe (o número passado no head será o número de linhas printadas)

'''
Vamos adicionar a essa tabela, os correspondentes nomes das flores
'''

iris.target

dados['flower'] = iris.target 

dados.head()

'''
Neste dataset, cada número corresponde a uma classe de flor. Vamos transformar para aparecer o nome de cada uma. 
Para isso faremos uma função que irá mapear os nomes de acordo com os números. Vamos aplicar a função sobre uma 
coluna inteira do nosso dataframe.
'''

iris.target_names  # Aqui estamos vendo os nomes que vem junto com o dataset

# Aqui estamos criando uma funcao que recebe o número da classe e retorna o nome correspondente
def mapear_nomes(numero_classe):
    flower_map = {
        0:iris.target_names[0],
        1:iris.target_names[1],
        2:iris.target_names[2]
    }
    return(flower_map[numero_classe])

mapear_nomes(0)

# O pandas permite que nos apliquemos uma função para todas as entradas de uma coluna
# Observe que prático é aplicar a função mapear_nomes sobre todos os valores na células da coluna 'flower'
# O resultado está sendo passado para uma nova coluna, chamada 'flower_name'

dados['flower_name'] = dados['flower'].apply(mapear_nomes)

dados.head(3)

'''
Vamos jogar fora a coluna flower uma vez que agora temos o nome da classe em outra coluna.
'''
dados = dados.drop(columns=['flower'])

dados.head(3)

'''
Informações técnicas sobre os dados
O método .info() do pandas nos diz quais são os tipos de dados que temos em cada coluna, 
a quantidade de linhas não nulas e quanto espaço na memória do computador (RAM) nosso dataframe está ocupando:
'''
dados.info()

'''
O método .describe() do pandas nos gera estatísticas básicas de todas as colunas do dataframe:
'''

dados.describe()

'''
Contando ocorrências de dados categóricos
'''

dados.flower_name.value_counts()

'''
O métodos .hist() do pandas nos gera os histogramas de todas as colunas com dados numéricos.
Olhar aqui https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.hist.html 
para saber como passar parâmetros neste método de forma a controlar o design do gráfico
'''

dados.hist()

'''
Já o método .boxplot() gera diagramas de caixa dos dados numéricos:
'''

dados.boxplot()

'''
O método .plot.scatter() gera gráficos de dispersão. Como os gráficos de dispersão são 2D, isto é, 
tem dois eixos, um x e outro y, precisamos especificar qual coluna do nosso dataframe será o x e qual coluna será o y.
'''

dados.plot.scatter(x='sepal length (cm)',
                   y='sepal width (cm)'
                  )

# Podemos repetir o procedimento para cada dispersão que queremos ver
dados.plot.scatter(x='petal length (cm)', y='petal width (cm)')

'''
Também podemos fazer os mesmos gráficos que fizemos utilizando métodos nativos do pandas usando métodos do seaborn
'''

import seaborn as sns

#Histogramas
sns.histplot(data=dados)

#Boxplot
sns.boxplot(data=dados)

'''
O Seaborn tem um método bastante interessante que plota todas as dispersões e todas as distribuições.
O parâmetro hue recebe o nome da coluna de classe. Ele irá pintar cada ponto de acordo com o tipo de flor.
'''

sns.pairplot(dados, hue='flower_name')

############################################################################

'''
Exercício - Íris Data set
Nas estatísticas e plots que realizamos no exemplo 2, os dados foram considerados sobre todos os tipos de flores. 
Considere agora separar os dados em 3 dataframes diferentes, cada um com um tipo de flor. Refaça as estatísticas 
e plote novos gráficos para cada um dos dataframes.
Você é capaz de propor um método de classificação das flores a partir da análise dos dados?
'''

dados.groupby('flower_name').mean()

dados.groupby('flower_name').std()
