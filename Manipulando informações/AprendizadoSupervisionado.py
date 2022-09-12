'''
Estudar o uso de algoritmos de Aprendizado de Máquina Supervisionado. 
Focaremos nos algoritmos utilizados para classificação, que é a tarefa de predizer classes 
(rótulos categóricos) para conjuntos de dados (numéricos ou transformados em numéricos).
Existem muitos algoritmos para se realizar essa tarefa, entre eles:

Regressão Logística
Análise de Discriminante Linear (LDA)
Análise de Discriminante Quadrático (QDA)
Naive Bayes
k-vizinhos mais próximos (KNN)
Máquina de Vetor Suporte (SVM)
Árvore de Decisão
RandomForest

Cada uma dessas técnicas tem uma forte base matemática e conceitual. 
Os algoritmos foram propostos ao longo de diversas décadas e possuem diferentes cenários de aplicações. 
Iremos nos focar nos procedimentos básicos para se utilizar esses algoritmos.
'''
'''
Foram medidos o comprimento das antenas e do abdômen de dois tipos de insetos: gafanhotos e esperanças.

Trabalhamos com estes dados na aula 16. Agora iremos aprender a criar classificadores para eles
'''

# Para trabalhar com dados em tabelas
import pandas as pd

# Para trabalhar com gráficos
import matplotlib.pyplot as plt  
import seaborn as sns

dados = pd.read_csv('gaf_esp.csv', sep=';') # Estamos carregando o arquivo csv usando o ; como separador

dados.head()

dados.groupby('Espécie').mean()

sns.boxplot(data=dados, x ='Espécie', y ='Comprimento do Abdômen')

sns.jointplot(data=dados, x = 'Comprimento do Abdômen' , y = 'Comprimento das Antenas', hue = 'Espécie')


############################################################################

'''
Segundo passo: separar os dados
Precisamos ter claro em nossas mentes quais são os atributos (colunas) preditivas, isto é, aquelas que 
usaremos para predizer um atributo alvo (coluna alvo). No nosso caso os atributos preditivos são Comprimento do Abdômen 
e Comprimento das Antenas, e o atributo alvo é a Espécie que será predita.

Quando se trabalhar com Aprendizado de Máquina Supervisionado, além disso precisamos separar nossos dados em dois 
conjuntos: um conjunto de treinamento e um conjunto de teste. Fazemos isso para evitar overfitting do algoritmo.

Existem várias estratégias para se separar dados. Vamos aplicar as principais:

(a) Escolher o tamanho dos conjuntos - 80% para treinamento e 20% para teste;

(b) Selecionar aleatoriamente os dados que irão compor o conjunto de treinamento e teste 
(usando um seed para garantir reprodutibilidade);
'''
from sklearn.model_selection import train_test_split

# Escolhendo as colunas preditivas e alvo
x = dados.drop(columns = 'Espécie') # Somente Comprimento do Abdômen e Comprimento das Antenas
y = dados['Espécie']                # Classe alvo

# Dividindo conjunto de treinamento e conjunto de teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

x_train.head(5)

y_train.head(5)

############################################################################

'''
Terceiro passo: transformar os dados
Dependendo do algoritmo de Aprendizado de Máquina que usamos precisamos modificar os dados para que eles 
se adequem as premissas do algoritmo.

Existem duas transformações de escalonamento muito utilizadas:

1) Nomalização (Normalization) - Também conhecido como escalonamento Min-Max no qual o range de valores da coluna 
irá fica de 0 (min) até 1 (max);

2) Padronização (Standardization) - Modifica a distribuição para que a média seja igual a zero e desvio padrão igual 
a 1 (o método subtrai a média de todas as entradas e dividide pelo desvio padrão);

Quando escolher uma ou outra? Depende dos seus dados, seu problema e o algoritmo que você quer usar. 
Em alguns casos, escalonar ou não os dados não irá mudar a solução do problema!

IMPORTANTE: independentmente do transformador escolhido, ele deve ser fitado apenas sobre os dados de treinamento. 
Isto é, o treinamento do escalonador deve receber apenas os dados de treinamento x_train. Após o treinamento do escalonador, 
ele deverá ser usado para transformar os dados x_test também.
'''
############################################################################

'''
Quarto passo: treinar o algoritmo
Vamos usar o conjunto de treinamento para treinar o algoritmo escolhido.

Existem vários algoritmos possíveis. Cada algoritmo tem seus hiperparâmetros 
(parâmetros que devem ser escolhidos para melhorar a performance do algoritmo). Para entender os hiperparâmetros de cada algoritmo 
é necessário entender a fundo como aquele algoritmo funciona.

Aqui vamos usar um dos algoritmos mais simples existentes, o Descriminador Linear:
'''

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis()  # Criamos o objeto do classificador (não mudamos nenhum hiperpârametro)

lda.fit(x_train,y_train) # Treinamos o classificador passando apenas o conjunto de dados de treinamento 


############################################################################

'''
Quinto passo: testar e avaliar
Usando agora o conjunto de teste, iremos testar o classificador criado e treinando no passo anterior.

Uma vez que realizamos um teste, precisamos avaliar o desempenho do nosso método. Diferentes hiperparâmetros e diferentes algoritmos podem 
ter um desempenho diferente. Apesar de sempre buscarmos o melhor desempenho, devemos levar em consideração outros aspectos para decidir o que 
é um desempenho aceitável. A primeira coisa a definir são as métricas de desempenho que podem ser comparadas entre diferentes algoritmos.

Existem várias métricas para se medir o desempenho de um classificador: métricas de performance, métricas de tempo consumido, métricas de 
memória consumida, etc. Vamos focar em uma métrica de performance muito utilizada no dia a dia de trabalho: a Matriz de Confusão e seus índices 
(Acurácia, Precisão, Recall e F1-score).
'''

# Perceba que estamos passando apenas o x de teste, afinal o algoritmo é que nos dira qual é o y 
y_predicoes = lda.predict(x_test) 

y_predicoes

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, plot_confusion_matrix
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, classification_report

matriz_confusao = confusion_matrix(y_true = y_test,
                                   y_pred = y_predicoes,
                                   labels=['Gafanhoto','Esperança'])

# plotando uma figura com a matriz de confusao
figure = plt.figure(figsize=(15, 5))
disp = ConfusionMatrixDisplay(confusion_matrix = matriz_confusao, display_labels=['Gafanhoto','Esperança'])
disp.plot(values_format='d') 

accuracy_score(y_true = y_test, y_pred = y_predicoes,)

precision_score(y_true = y_test, 
         y_pred = y_predicoes,
         pos_label="Esperança")

recall_score(y_true = y_test, 
         y_pred = y_predicoes,
         pos_label="Esperança")

f1_score(y_true = y_test, 
         y_pred = y_predicoes,
         pos_label="Esperança")   

# Metricas de precisão, revocação, f1-score e acurácia.
print(classification_report(y_test, y_predicoes))

#Desenhar sobre o gráfico de dispersão o modelo matemático encontrado pelo algoritmo de Classificação LDA:
import numpy as np

# São os coeficientes do nosso modelo de ML treinado
c1, c2 = lda.coef_[0]
b = lda.intercept_

# É a equação da reta do LDA
x1 = np.arange(0,10)
x2 = - (c1/c2)* x1 - b/c2

'''
A fronteira de decisão entre as classes em um classificador LDA é uma linha.

Toda linha tem uma função metamática associada.

Podemos ver os coeficientes dessa fronteira (hiperplano ou linhas) na propriedade coef_.

Para um problema de duas dimensões, (como o acima), temos dois coeficientes. Vamos chamar esses coeficientes de  
c1  e  c2 , e os atributos de  x1  e  x2 , e o valor de interceptação no eixo das ordenadas de  b . Dessa maneira, temos 
a equação da fronteira:

c1 x1 + c2 x2 +b = 0 

Agora, resolvedo para  x2 , podemos obter a equação da reta:

x2=−c1c2x1−bc2
'''
plot = sns.jointplot(data=dados, x="Comprimento do Abdômen", y="Comprimento das Antenas", hue = 'Espécie',
              height=5, ratio=2, marginal_ticks=True
             )
plot.ax_joint.plot(x1, x2, 'r-', linewidth = 2)
plot.ax_marg_x.axvline(x=4.5, color='k', linestyle='--')
plot.ax_marg_y.axhline(y=5.3, color='k', linestyle='--')
plot.ax_joint.set_xlim(0,11)
plot.ax_joint.set_ylim(0,11)

############################################################################

'''
Sexto passo: Produção
Se nosso algoritmo está bom e atende os requisitos de negócio, podemos colocar ele em produção. Essa etapa envolve 
conhecimento do tipo de dispositivo em que iremos rodar a solução.

Por exemplo, iremos colocar esse modelo em um site? Precisamos trabalhar com o pessoal de backend. Vamos embarcar em um veículo autônomo? 
Time de engenharia de software e engenharia eletrônica.

Esse passo inteiro transcede o escopo da nossa disciplina, já que envolve outras disciplinas e competências.

Vamos contudo ver como "baixar" nosso modelo pronto para não precisar treina-lo novamente. Afinal, iremos empregar o algoritmo já treinado e 
pronto para uso em produção (a menos que estejamos usando técnicas mais sofisticadas de machine learning como Active Learning e Atualização de Modelo em Execução).

A etapa de "salvar/baixar" o modelo pronto é chamada de Persistência do Modelo. Quando usamos um modelo pronto, é comum dizer que estamos usando um modelo pré-treinado.
'''

import pickle
#Pickle é um formato de arquivo de objeto python serializado na memória permanente. Ele é análogo ao JSON para dicionários ou o CSV para tabelas, 
# mas ele funciona para objetos python, ou seja, é muito mais abrangente!

# vamos salvar em bytes (flag wb) para ser mais cross-platform (acessível a vários sistemas)
with open('meu_modelo_serializado.pickle', 'wb') as f: 
    pickle.dump(lda, f)

with open('meu_modelo_serializado.pickle', 'rb') as f:
    modelo_carregado = pickle.load(f)

modelo_carregado.predict([[1,2]])

#Além do Pickle, o Scikit-Learn tem o método joblib que é mais eficiente para serializar modelos treinados através dessa biblioteca.

from joblib import dump, load

dump(lda, 'meu_modelo_serializado.joblib')

modelo_carregado2 = load('meu_modelo_serializado.joblib')

modelo_carregado2.predict([[1,2]])
