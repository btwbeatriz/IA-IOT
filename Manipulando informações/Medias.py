x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

def media_aritmetica(x):
  n = len(x)
  soma = 0
  for i in range(0, n):
    soma = soma + x[i]

  media = soma/n
  return (media)

media_aritmetica(x)


def media_geometrica(x):
  n = len(x)
  soma = 1
  for i in range(0, n):
    soma = soma *x[i]

  media = soma**(1/n)
  return (media)

media_geometrica(x)


def media_harmonica(x):
  n = len(x)
  soma = 0
  for i in range(0, n):
    soma = soma + (1/x[i])

  media = n / soma
  return (media)

media_harmonica(x)


w = [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]

def media_ponderada(x,w):
  soma_emcima = 0
  soma_embaixo = 0
  for i in range(0, len(x)):
    soma_emcima = soma_emcima + x[i]*w[i]
    soma_embaixo = soma_embaixo + w[i]
  media = soma_emcima/soma_embaixo
  return(media)


def mediana(x):
  x.sort()
  n = len(x)
  if n%2!=0:  #lista par
    a = int(n/2)
    mediana = x[a]
  else:
    a = int(n/2)  
    b = a-1
    mediana = 0.5*(x[a] + x[b])
    return (mediana)


#--> Estatísticas
x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

#Variância da população

def variancia_populacional(x):
    media = media_aritmetica(x)
    N = len(x)
    soma=0
    for xi in x:
        soma = soma+(xi-media)**2
    variancia = soma/N
    return(variancia)

#Variância amostral
def variancia_amostral(x):
    media = media_aritmetica(x)
    N = len(x)
    soma = 0
    for xi in x:
        soma = soma+(xi-media)**2
    variancia = soma/(N-1)
    return(variancia)

def desvio_padrao_populacional(x):
    desvio_padrao = variancia_populacional(x)**(1/2)
    return(desvio_padrao)

def desvio_padrao_amostral(x):
    desvio_padrao = variancia_amostral(x)**(1/2) # Tirar raiz quadrada é a mesma coisa do que elevar a meio
    return(desvio_padrao)


def incerteza(x):
    media = media_aritmetica(x)
    soma = 0
    n = len(x)
    for i in range(0,n):
        soma = soma + (x[i] -media)**2
    var = (soma/(n*(n -1)))**0.5
    return (var)

#Importando bilbioteca / Fazer média aritmética
import numpy as np

np.mean(x) 

#Media ponderada
np.average(x, weights=w)

#Biblioteca de estatísticas
import statistics

statistics.mean(x)

statistics.geometric_mean(x)

statistics.median(x)

statistics.mode(x)

statistics.multimode(x) #Quando há mais de uma moda

statistics.pvariance(x)

statistics.variance(x)  #Amostral

statistics.pstdev(x)    #Desvio padrão


from scipy import stats  #Biblioteca de funções

stats.hmean(x)

stats.gmean(x)

stats.sem(x) 


int(100*9.99801427e-01)
# Criando um vetor com muitas posicoes
y = [int(yi*100) for yi in np.random.rand(10**3)]

len(y)

%timeit -n 10 media_aritmetica(y)

%timeit -n 10 np.mean(y)

%timeit -n 10 moda(y)

%timeit -n 10 statistics.multimode(y)

%timeit -n 10 stats.mode(y) 

