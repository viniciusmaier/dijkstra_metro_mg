from typing import List

class Grafo:
    def __init__(self, vert : int) -> None:
        self._grafo = [[0 for _ in range(vert)]for _ in range(vert)]        
    
    @property
    def grafo(self) :
        return self._grafo

    def adicionaAresta(self, u, v, peso) :
        self._grafo[u - 1][v - 1] = peso

