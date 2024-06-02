from typing import List

class Localidade :
    def __init__ (self,id, dsLocalidade, adjacentes) : 
        self._id : int = id
        self._dsLocalidade : str = dsLocalidade
        self._listAdjacencias : List[int] = adjacentes

    @property
    def dsLocalidade(self) :
        return self._dsLocalidade

    @property
    def id(self) :
        return self._id
    
    @property
    def listAdjacencias(self) :
        return self._listAdjacencias


    @dsLocalidade.setter
    def dsLocalidade(self, dsLocalidade) :
        self._dsLocalidade = dsLocalidade