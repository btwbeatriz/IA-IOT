'''
Regressão
Focaremos nos algoritmos utilizados para regressão, que é a tarefa de predizer valores de saída 
(dados numéricos) para conjuntos de dados de entrada (numéricos ou transformados em numéricos).

Existem muitos algoritmos para se realizar essa tarefa, entre eles:

Regressão Linear
Redes Neurais
Árvores de Decisão
RandomForest
Support Vector Regression (SVR)
Cada uma dessas técnicas tem uma forte base matemática e conceitual. 
Os algoritmos foram propostos ao longo de diversas décadas e possuem diferentes cenários de aplicações.
'''

'''
Preço de Casas

Foram medidos os preços de casas vendidas entre Maio de 2014 e Maio de 2015 em Seattle. Foram anotados 
21 atributos descritivos destas casas, como número de quartos e número de banheiros, entre outros.

Os dados estão diponíveis em: https://www.openml.org/d/42731

Será que é possível usar as características das casas para predizer qual deveria ser o seu valor de venda?
'''

# Para trabalhar com dados em tabelas
import pandas as pd

# Para trabalhar com dados do OpenML
from sklearn.datasets import fetch_openml

# Para trabalhar com gráficos
import seaborn as sns
import matplotlib.pyplot as plt

dados = fetch_openml(data_id=42731)

print(dados)

df_casas = pd.DataFrame(data = dados.data, columns=dados.feature_names) # Transformando em dataframe

df_casas['price'] = dados.target # Colocando a coluna de preços

df_casas.head()

df_casas.info() # Observe que não temos nenhum dado faltando para as colunas de informação

sns.heatmap(df_casas.corr())

############################################################################

'''
Separar os dados
Precisamos ter claro quais são os atributos (colunas) preditivas, isto é, aquelas que usaremos para 
predizer um atributo alvo (coluna alvo).

Quando se trabalhar com Aprendizado de Máquina Supervisionado, além disso precisamos separar nossos 
dados em dois conjuntos: um conjunto de treinamento e um conjunto de teste. Fazemos isso para evitar 
overfitting do algoritmo.

Existem várias estratégias para se separar dados. Vamos aplicar as principais:

(a) Escolher o tamanho dos conjuntos - 80% para treinamento e 20% para teste;

(b) Selecionar aleatoriamente os dados que irão compor o conjunto de treinamento e teste 
(usando um seed para garantir reprodutibilidade);
'''

from sklearn.model_selection import train_test_split

len(df_casas)

# Escolhendo as colunas preditivas e alvo
x = df_casas.drop(columns=['zipcode', 'price', 'date_year', 'date_month', 'date_day'])
y = df_casas['price']                

# Dividindo conjunto de treinamento e conjunto de teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

len(x_train), len(x_test), len(y_train), len(y_test)

############################################################################

'''
Treinar o algoritmo
Vamos usar o conjunto de treinamento para treinar o algoritmo escolhido.

Existem vários algoritmos possíveis. Cada algoritmo tem seus hiperparâmetros 
(parâmetros que devem ser escolhidos para melhorar a performance do algoritmo). 
Para entender os hiperparâmetros de cada algoritmo é necessário entender a fundo 
como aquele algoritmo funciona.

Aqui vamos usar um dos algoritmos mais simples existentes, a Regressão Linear:
'''

from sklearn.linear_model import LinearRegression

lr = LinearRegression()  # Criamos o objeto do regressor (não mudamos nenhum hiperpârametro)

lr.fit(x_train,y_train) # Treinamos o regressor passando apenas o conjunto de dados de treinamento

############################################################################

'''
Testar e avaliar
Usando agora o conjunto de teste, iremos testar o classificador criado e treinando no passo anterior.

Uma vez que realizamos um teste, precisamos avaliar o desempenho do nosso método. Diferentes hiperparâmetros 
e diferentes algoritmos podem ter um desempenho diferente.
A primeira coisa a definir são as métricas de desempenho que podem ser comparadas entre diferentes algoritmos.

Existem várias métricas para se medir o desempenho de um regressor: métricas de performance, 
métricas de tempo consumido, métricas de memória consumida, etc. Vamos calcular algumas delas:

MAE
MSE
Correlação de Pearson
R2
'''
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy.stats import pearsonr

# Perceba que estamos passando apenas o x de teste, afinal o algoritmo é que nos dira qual é o y 
y_predicoes = lr.predict(x_test) 

MAE = mean_absolute_error(y_true = y_test,      # Gabarito
                          y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('MAE: ', MAE)

MSE = mean_squared_error(y_true = y_test,      # Gabarito
                         y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('MSE: ', MSE)
print('raiz MSE: ', MSE**0.5)

'''
A MAE e a MSE são formas bem simples de avaliar o erro. O problema é como saber se um determinado 
valor de MAE ou MSE é muito grande? Intuitivamente sabemos que quanto maior esse valor, pior. 
Entretanto, o valor calculado se refere a escala dos dados, e por isso, pode ser de dificil avaliação. 
Em geral, devemos comparar duas MAEs ou duas MSEs para dois modelos de regressão diferentes, 
usando os mesmos dados. Aqueles que tiverem uma MAE ou MSE menores, serão, portanto, melhores.

Neste exemplo, uma MAE de 128157 significa que em média, estamos errando o reço de caça em $128 mil 
para mais ou para menos.

A escala R², por outro lado, não tem esse problema de comparação. Esse valor já está em uma escala, 
de forma que sabemos que quanto mais próximo de 1, melhor! Dificilmente um modelo terá R²=1. Então se 
você obter isso, provavelmente seu modelo está sofrendo de overfitting (ele é muito bom para seus dados, 
mas não será tão bom para novas entradas). Sempre que você obtiver um valor de R²=1, verifique se não 
cometeu nenhum erro nos passos anteriores.
'''

R2 = r2_score(y_true = y_test,      # Gabarito
              y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('R2: ', R2)  # Quanto mais próximos de 1 melhor

''''
O coeficiente de correlação de Pearson  ρ  também é mais fácil de interepretar o resultado já que eles 
está em uma escala de -1 a 1. Quando estamos avaliando o desempenho do modelo, queremos  ρ=1 .
'''

rho = pearsonr(y_test, y_predicoes)
print('\u03C1:', rho[0]) # Quanto mais próximo de 1, melhor (OBS: apneas neste caso de utilização)

'''
O modelo obtido
Nos modelos de Regressão Linear, temos uma função linear de múltiplos coeficientes. Essa função é 
exatamente o modelo encontrado pelo algoritmo. Para obter os coeficientes, basta fazer:
'''

a_modelo = lr.coef_      # Coeficientes angulares do modelo (cada um mede a influência de cada coluna)
b_modelo = lr.intercept_ # Coeficiente linear do model

print(a_modelo, b_modelo)

'''
Durante a etapa de treinamento, métricas de desempenho também são calculadas com o objetivo de se minimizar o erro. 
Perceba que o R² de treinamento e de teste são diferentes, o que é esperado e desejado. Podemos obter o R² de 
treinamento, fazendo:
'''

R2_treinamento = lr.score(x_train, y_train)
print(R2_treinamento)

'''
Se o R² de treinamento der muito próximo e 1 e o R² de teste der muito abaixo (0.7, por exemplo), então o modelo 
está com overfitting.
'''

y_pred_linear = y_predicoes # Salvando as informações do Modelo Reg Linear para comparar depois

############################################################################

'''
Rede Neural Perceptron Multicamada
Redes Neurais Artificiais como o MLP (Multilayer Perceptron) podem ser altamente sensiveis a escala dos dados 
(assim como as SVM e o KNN).

Vamos primeiro realizar o passo de transformação dos dados:
'''

from sklearn.preprocessing import StandardScaler # Importando o Escalonador de Normalização

# 3 - Escalonamento
scaler = StandardScaler() # Criando o objeto de escalonamento
scaler.fit(x_train) # Passando os dados de treinamento para encontrar a escala

x_train_escalonado = scaler.transform(x_train)
x_test_escalonado = scaler.transform(x_test)

'''
Criar a rede neural e treinando ela:
'''

from sklearn.neural_network import MLPRegressor # Importando a Rede Neural MLP para Regressão

# 4 - Treino
# Instanciando o objeto
ml_perceptron = MLPRegressor(solver='lbfgs', # otimizador por métodos quasi-Newton
                             tol=1e-5, # Limiar para a otimização (treinamento)
                             max_iter=1500, # Limite de iterações durante a otimização (treinamento)
                             random_state=42, # (seed) pesos da rede são inicializados aleatoriamente
                             hidden_layer_sizes=(10,4), # Quantidade de neuronios por camada oculta #(12,7,3)
                             activation='relu') # Função de ativação dos neuronios

ml_perceptron.fit(x_train_escalonado, y_train)  # Treinando (perceba que estamos passando o x_train escalonado)

# 5 - Teste
y_predicoes = ml_perceptron.predict(x_test_escalonado) # Perceba que estamos passando o x_test escalonado

R2 = r2_score(y_true = y_test,      # Gabarito
              y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('R2: ', R2)  # Quanto mais próximos de 1 melhor

rho = pearsonr(y_test, y_predicoes)
print('\u03C1:', rho[0]) # Quanto mais próximo de 1, melhor (OBS: apneas neste caso de utilização)

MAE = mean_absolute_error(y_true = y_test,      # Gabarito
                          y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('MAE: ', MAE)

MSE = mean_squared_error(y_true = y_test,      # Gabarito
                         y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('MSE: ', MSE)

y_predicoes_mlp = y_predicoes

############################################################################

'''
Gráfico de acerto
Podemos visualizar nossos acertos através de um gráfico de dispersão entre y_test e y_pred. Perceba que 
se nosso modelo acerta tudo, y_test=y_pred. Dessa forma, teriamos uma reta perfeita com ângulo de inclinação 
de 45°. Entretanto, se nosso modelo não acertar tudo, então teremos uma outra reta, com outro ângulo de inclinação.
'''

import seaborn as sns

ax = sns.regplot(x=y_test,y=y_pred_linear,
                 color="b", scatter_kws={'alpha':0.3}, label='RegLinear') # Regressão Linear
ax = sns.regplot(x=y_test,y=y_predicoes_mlp,
                 color="g", scatter_kws={'alpha':0.3}, label='MLP') # Rede Neural
ax.plot(y_test, y_test, 'r--', linewidth = 2, label='Correto') # Reta 100% correto
ax.set(xlabel='y_test (gabarito)', ylabel='y_pred (respostas do teste)') 
ax.legend()
#ax.set_xscale('log'), ax.set_yscale('log')

############################################################################

'''
Fifa 2019
https://www.kaggle.com/karangadiya/fifa19
Queremos prever a performance total do jogador dada pela coluna Overall, usando a idade do jogador (coluna Age), 
o valor do jogador (coluna Value) e o seu salário (coluna Wage).

Primeiro passo: carregar os dados e fazer a análise exploratória
'''
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
dados_fifa = pd.read_csv('data_fifa2019.csv', index_col = 0)

dados_fifa.head(3)

dados_fifa.info()

'''
Converter as colunas Value e Wage que estão em strings para valores numéricos em Euros:
'''

dados_fifa['Value'][0]

def convert_currency(valor):
    valor = valor.replace('€','')
    
    if 'K' in valor:
        valor = 1000*float(valor.replace('K',''))
    elif 'M' in valor:
        valor = 1000000*float(valor.replace('M',''))
    else:
        valor = float(valor)
        
    return valor

dados_fifa['Value'] = dados_fifa['Value'].apply(convert_currency)
dados_fifa['Wage'] = dados_fifa['Wage'].apply(convert_currency)

dados_fifa['Value'][0]

'''
Segundo passo: separar os dados
'''
from sklearn.model_selection import train_test_split

# Escolhendo as colunas preditivas e alvo
x = dados_fifa[['Age','Value','Wage']] # Selecionando 3 colunas (perceba o uso de dois colchetes)
y = dados_fifa['Overall']                # Valor alvo

# Dividindo conjunto de treinamento e conjunto de teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

x.describe()

'''
Terceiro passo: transformar os dados
'''

from sklearn.preprocessing import StandardScaler # Importando o Escalonador de Normalização

# Passo 3 - Escalonamento
scaler = StandardScaler() # Criando o objeto de escalonamento
scaler.fit(x_train) # Passando os dados de treinamento para encontrar a escala

x_train_escalonado = scaler.transform(x_train)
x_test_escalonado = scaler.transform(x_test)

'''
Quarto passo: treinar o modelo
Vamos Escalonar os dados antes de usá-los, realizando assim o passo intermediário de transformação.
'''
from sklearn.linear_model import LinearRegression

lr = LinearRegression()  # Criamos o objeto do regressor (não mudamos nenhum hiperpârametro)

lr.fit(x_train_escalonado,y_train) # Treinamos o regressor passando apenas o conjunto de dados de treinamento 

'''
Quinto passo: testar e avaliar
'''
from sklearn.metrics import r2_score

y_predicoes = lr.predict(x_test_escalonado) 

R2 = r2_score(y_true = y_test,      # Gabarito
              y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('R2: ', R2)  # Quanto mais próximos de 1 melhor

MAE = mean_absolute_error(y_true = y_test,      # Gabarito
                          y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('MAE: ', MAE)

MSE = mean_squared_error(y_true = y_test,      # Gabarito
                         y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('MSE: ', MSE)
print('raiz MSE: ', MSE**0.5)

'''
Voltando para a análise exploratória
Vamos tentar ver como nossos dados se relacionam plotando gráficos de dispersão entre as colunas 
descritivas e colunas alvo:
'''

fig, ax = plt.subplots(1,3, figsize=(12, 4))

# Plot de dispersão (scatter)
sns.scatterplot(ax = ax[0], data = dados_fifa, x = 'Age',   y='Overall', color='b', alpha=0.5)
sns.scatterplot(ax = ax[1], data = dados_fifa, x = 'Value', y='Overall', color='g', alpha=0.5)
sns.scatterplot(ax = ax[2], data = dados_fifa, x = 'Wage',  y='Overall', color='r', alpha=0.5)

# Aqui estamos explicitamente dando nome aos eixos do gráfico
ax[0].set_xlabel('Age'), ax[0].set_ylabel('Overall')
ax[1].set_xlabel('Value'), ax[1].set_ylabel('Overall')
ax[2].set_xlabel('Wage'), ax[2].set_ylabel('Overall')

# Colocando grid
ax[0].grid(), ax[1].grid(), ax[2].grid()

#ax[1].set_xscale('log')
#ax[2].set_xscale('log')

# Vamos aumentar a separação entre os gráficos
plt.subplots_adjust(wspace = 0.3)

# Aumentando o tamanho da fonte (letra)
plt.rcParams.update({'font.size': 12})

'''
O Numpy tem várias funções matemáticas prontas (https://numpy.org/doc/stable/reference/routines.math.html), 
entre elas o log10, que tira o logaritmo na base 10 do valor passado. Vamos usar essa função para transformar 
nossos dados.
'''

import numpy as np # O numpy tem funções matemáticas variadas prontas dentro dele
from sklearn.preprocessing import FunctionTransformer  # Módulo para transformar dados por funções

# Criando nosso transformador
transformador = FunctionTransformer(np.log10)

x1 = dados_fifa['Age']
x2 = transformador.transform(dados_fifa['Value'])
x3 = transformador.transform(dados_fifa['Wage'])

dados_modelo_log = {'Age':x1,
               'log_Value':x2,
               'log_Wage':x3,
               'Overall':dados_fifa['Overall']
            }

dados_modelo_log = pd.DataFrame(data=dados_modelo_log)

dados_modelo_log.describe()

dados_modelo_log.info()

'''
O problema de usar a função logaritmica é que ela não é definida para o zero e valores negativos. 
Dessa forma ela gera valores -inf quando não consegue calcular. Vamos substituir todos os valores -inf por 0.
'''
dados_modelo_log.replace([np.inf, -np.inf], 0, inplace=True)

dados_modelo_log.describe()

fig, ax = plt.subplots(1,3, figsize=(12, 4))

# Plot de dispersão (scatter)
sns.scatterplot(ax = ax[0], data = dados_modelo_log, x = 'Age',   y='Overall', color='b', alpha=0.5)
sns.scatterplot(ax = ax[1], data = dados_modelo_log, x = 'log_Value', y='Overall', color='g', alpha=0.5)
sns.scatterplot(ax = ax[2], data = dados_modelo_log, x = 'log_Wage',  y='Overall', color='r', alpha=0.5)

# Aqui estamos explicitamente dando nome aos eixos do gráfico
ax[0].set_xlabel('Age'), ax[0].set_ylabel('Overall')
ax[1].set_xlabel('Value'), ax[1].set_ylabel('Overall')
ax[2].set_xlabel('Wage'), ax[2].set_ylabel('Overall')

# Colocando grid
ax[0].grid(), ax[1].grid(), ax[2].grid()

# Vamos aumentar a separação entre os gráficos
plt.subplots_adjust(wspace = 0.3)

# Aumentando o tamanho da fonte (letra)
plt.rcParams.update({'font.size': 12})

# Removendo os zeros
dados_modelo_log2  = dados_modelo_log[dados_modelo_log['log_Value']>0]
dados_modelo_log3  = dados_modelo_log2[dados_modelo_log2['log_Wage']>0]

'''
Treinando um algoritmo de Regressão Linear para prever o overall:
'''

# Passo 2 - Separando dados
x = dados_modelo_log3.drop(columns=['Overall']) # Selecionando 3 colunas
y = dados_modelo_log3['Overall']                # Valor alvo
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# Passo 3 - Escalonamento
scaler = StandardScaler() # Criando o objeto de escalonamento
scaler.fit(x_train) # Passando os dados de treinamento para encontrar a escala

x_train_escalonado = scaler.transform(x_train)
x_test_escalonado = scaler.transform(x_test)

# Passo 4 - Treinar
lr = LinearRegression()  # Criamos o objeto do regressor (não mudamos nenhum hiperpârametro)
lr.fit(x_train_escalonado,y_train) # Treinamos o regressor passando apenas o conjunto de dados de treinamento 

# Passo 5 - Avaliar
y_predicoes = lr.predict(x_test_escalonado) 

R2 = r2_score(y_true = y_test,      # Gabarito
              y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('R2: ', R2)  # Quanto mais próximos de 1 melhor

MAE = mean_absolute_error(y_true = y_test,      # Gabarito
                          y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('MAE: ', MAE)

MSE = mean_squared_error(y_true = y_test,      # Gabarito
                         y_pred = y_predicoes) # Respostas do algoritmo ao teste realizado
print('MSE: ', MSE)
print('raiz MSE: ', MSE**0.5)

