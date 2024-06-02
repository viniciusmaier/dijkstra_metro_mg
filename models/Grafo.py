from typing import List

from HeapMin import HeapMin

class Grafo:
    def __init__(self, vert : int) -> None:
        self._grafo = [[0 for _ in range(vert)]for _ in range(vert)]        
    
    @property
    def grafo(self) :
        return self._grafo

    def adicionaAresta(self, u, v, peso) :
        self._grafo[u - 1][v - 1] = peso

    def dijsktra(self, origem : int) :
        custo_vem = [[-1, 0] for _ in range(len(self._grafo))]
        custo_vem[origem - 1] = [0,origem]
        h = HeapMin()
        h.adiciona_no(0, origem)
        while h.tamanho() > 0 : 
            dist, v = h.remove_no()
            for i in range(len(self._grafo)):
                if self._grafo[v-1][i] != 0:
                    if custo_vem[i][0] == -1 or custo_vem[i][0] > dist + self._grafo[v-1][i]:
                        custo_vem[i] = [dist + self._grafo[v-1][i], v]
                        h.adiciona_no(dist + self._grafo[v-1][i], i+1)
        return custo_vem