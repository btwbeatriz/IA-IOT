#Grafos são objetos matemáticos muito presentes em computação. 
# Diversas estruturas de dados são construídas e representadas através de grafos. 
# Vamos utilizar a biblioteca networkx (https://networkx.org/) 
# que define uma classe para implementação de grafos como objetos.

#Grafos são compostos por vértices V e arestas E, sendo denotado por G(V,E).

import networkx as nx # Trabalhar com grafos

grafo1 = nx.Graph() # Cria um objeto grafo

print(type(grafo1))

# Criando um grafo triangular (cluster)
grafo1.add_node(1)
grafo1.add_node(2)
grafo1.add_node(3)

grafo1.add_edge(1, 2)
grafo1.add_edge(2, 3)
grafo1.add_edge(3, 1)

nx.draw(grafo1, with_labels = True)

#criando uma representação de árvore

import matplotlib.pyplot as plt

G = nx.DiGraph()

# Nós
G.add_node("Raiz")
G.add_node("Filho 1")
G.add_node("Filho 2")
G.add_node("Neto 11")
G.add_node("Neto 12")
G.add_node("Neto 13")


G.add_edge("Raiz", "Filho 1")
G.add_edge("Raiz", "Filho 2")

G.add_edge("Filho 1", "Neto 11")
G.add_edge("Filho 1", "Neto 12")
G.add_edge("Filho 1", "Neto 13")

nx.draw(G, with_labels=True, arrows=False)

