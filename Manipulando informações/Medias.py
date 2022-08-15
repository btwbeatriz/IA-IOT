x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

def media_aritmetica(x):
  soma = 0
  for i in range(0, len(x)):
    soma = soma + x[i]

  media = soma/len(x)
  return media

media_aritmetica(x)
