with open('dados_topico1/texto_ansi.txt', 'r', encoding='cp1252') as file:  #file = nome da variável
    print(file)   # Printando o que foi carregado na variável file ao abrir o arquivo
    print(type(file)) # Printando o tipo de dado (estrutura) da variavel file
    linhas = file.readlines() # Readlines é um método da classe _io.TextIOWrapper que lê as linhas do arquivo

print(linhas) 
print(type(linhas)) # As linhas são armazenadas em uma lista (vetor) de strings

print(linhas[-1])

for linha in linhas:  #printando as linhas
    print(linha)

#Forçar a decodificação dos carateres usando um encoding 
# posteriormente ao carregamento do arquivo em formato binário:
for linha in linhas:
    #print(linha.decode('utf-8'))
    print(linha.decode('ansi'))

with open('dados_topico1/texto_utf8.txt', 'r', encoding="utf-8") as file:
    linhas = file.readlines()
    
print(linhas)  