from typing import List
from models.Grafo import Grafo
from models.Localidade import Localidade




## GERANDO O GRAFO

localidades : List[Localidade] = [
            Localidade(1, "UNICV", [5,6,7,2]), Localidade(2, "FEITEP",[1,16,21]),Localidade(3, "UNINGA",[10,17]),Localidade(4,"UNICESUMAR",[7,11,19,23]),Localidade(5,"UEM",[10,9,1]),
            Localidade(6,"BURACAO", [8,1]), Localidade(7,"PREFEITURA DE MARINGÁ", [1,4,23]), Localidade(8,"CENTRO COMUNITARIO",[6,13]), Localidade(9,"JARDIM CANADÁ",[5,14,17,18]),
            Localidade(10,"JARDIM LICCE",[3,5,13,17]), Localidade(11,"PARQUE RESIDENCIAL AEROPORTO",[4,12]), Localidade(12,"JARDIM DA GLÓRIA",[11,13]), Localidade(13,"JARDIM PIATA",[8,10,12,23]),
            Localidade(14,"JARDIM SÃO DOMINGOS",[9,15,21]), Localidade(15,"JARDIM OURO COLA",[14]), Localidade(16,"PARQUE DO JAPÃO",[2,19,20]), Localidade(17,"JARDIM MUNICH",[3,9,10,18]),
            Localidade(18,"JARDIM OLIMPICO",[9,17,21,23]), Localidade(19,"JARDIM PARAISO",[4,16]), Localidade(20,"AEROPORTO REGIONAR DE MRG",[16,21,22]), Localidade(21,"PARQUE INDUSTRIAL",[2,14,18,20]),
            Localidade(22,"DISTRITO INDUSTRIAL 2",[20]), Localidade(23,"JARDIM NOVO HORIZONTE",[4,7,13,18])
            ]



g = Grafo(len(localidades))


## INSERINDO OS PESOS

# ID 1 (UNICV)
g.adicionaAresta(localidades[0].id, localidades[0].listAdjacencias[0], 0.85)
g.adicionaAresta(localidades[0].id, localidades[0].listAdjacencias[1], 2.3)
g.adicionaAresta(localidades[0].id, localidades[0].listAdjacencias[2], 0.7)
g.adicionaAresta(localidades[0].id, localidades[0].listAdjacencias[3], 3.35)

#ID 2 (FEITEP)
g.adicionaAresta(localidades[1].id, localidades[1].listAdjacencias[0], 3.35)
g.adicionaAresta(localidades[1].id, localidades[1].listAdjacencias[1], 2.7)
g.adicionaAresta(localidades[1].id, localidades[1].listAdjacencias[2], 4)

# #ID 3 (UNINGA)
g.adicionaAresta(localidades[2].id, localidades[2].listAdjacencias[0], 2.9)
g.adicionaAresta(localidades[2].id, localidades[2].listAdjacencias[1], 9.35)

# # #ID 4 (UNICESUMAR)
g.adicionaAresta(localidades[3].id, localidades[3].listAdjacencias[0], 2.85)
g.adicionaAresta(localidades[3].id, localidades[3].listAdjacencias[1], 2.3)
g.adicionaAresta(localidades[3].id, localidades[3].listAdjacencias[2], 3)
g.adicionaAresta(localidades[3].id, localidades[3].listAdjacencias[3], 1.75)

# # #ID 5 (UEM)
g.adicionaAresta(localidades[4].id, localidades[4].listAdjacencias[0], 3.5)
g.adicionaAresta(localidades[4].id, localidades[4].listAdjacencias[1], 1.9)
g.adicionaAresta(localidades[4].id, localidades[4].listAdjacencias[2], 0.83)

# # #ID 6 (BURACAO)
g.adicionaAresta(localidades[5].id, localidades[5].listAdjacencias[0], 1.8)
g.adicionaAresta(localidades[5].id, localidades[5].listAdjacencias[1], 2.3)

# # #ID 7 (PREFEITURA DE MARINGÁ)
g.adicionaAresta(localidades[6].id, localidades[6].listAdjacencias[0], 0.7)
g.adicionaAresta(localidades[6].id, localidades[6].listAdjacencias[1], 2.85)
g.adicionaAresta(localidades[6].id, localidades[6].listAdjacencias[2], 2.65)

# # #ID 8 (CENTRO COMUNITARIO)
g.adicionaAresta(localidades[7].id, localidades[7].listAdjacencias[0], 1.8)
g.adicionaAresta(localidades[7].id, localidades[7].listAdjacencias[1], 3.55)

# # #ID 9 (JARDIM CANADÁ)
g.adicionaAresta(localidades[8].id, localidades[8].listAdjacencias[0], 1.9)
g.adicionaAresta(localidades[8].id, localidades[8].listAdjacencias[1], 7.7)
g.adicionaAresta(localidades[8].id, localidades[8].listAdjacencias[2], 3.4)
g.adicionaAresta(localidades[8].id, localidades[8].listAdjacencias[3], 2.5)


# # #ID 10 (JARDIM LICCE)
g.adicionaAresta(localidades[9].id, localidades[9].listAdjacencias[0], 2.9)
g.adicionaAresta(localidades[9].id, localidades[9].listAdjacencias[1], 3.5)
g.adicionaAresta(localidades[9].id, localidades[9].listAdjacencias[2], 4.65)
g.adicionaAresta(localidades[9].id, localidades[9].listAdjacencias[3], 4.3)

# # #ID 11 (PARQUE RESIDENCIAL AEROPORTO)
g.adicionaAresta(localidades[10].id, localidades[10].listAdjacencias[0], 2.3)
g.adicionaAresta(localidades[10].id, localidades[10].listAdjacencias[1], 3.25)

# # #ID 12 (JARDIM DA GLÓRIA)
g.adicionaAresta(localidades[11].id, localidades[11].listAdjacencias[0], 3.25)
g.adicionaAresta(localidades[11].id, localidades[11].listAdjacencias[1], 1.6)

# # #ID 13 (JARDIM PIATA)
g.adicionaAresta(localidades[12].id, localidades[12].listAdjacencias[0], 3.55)
g.adicionaAresta(localidades[12].id, localidades[12].listAdjacencias[1], 4.65)
g.adicionaAresta(localidades[12].id, localidades[12].listAdjacencias[2], 1.6)
g.adicionaAresta(localidades[12].id, localidades[12].listAdjacencias[3], 7.1)

# # #ID 14 (JARDIM SÃO DOMINGOS)
g.adicionaAresta(localidades[13].id, localidades[13].listAdjacencias[0], 7.7)
g.adicionaAresta(localidades[13].id, localidades[13].listAdjacencias[1], 3.9)
g.adicionaAresta(localidades[13].id, localidades[13].listAdjacencias[2], 7.65)


# # #ID 15 (JARDIM OURO COLA)
g.adicionaAresta(localidades[14].id, localidades[14].listAdjacencias[0], 3.9)

# # #ID 16 (PARQUE DO JAPÃO)
g.adicionaAresta(localidades[15].id, localidades[15].listAdjacencias[0], 2.7)
g.adicionaAresta(localidades[15].id, localidades[15].listAdjacencias[1], 6.75)
g.adicionaAresta(localidades[15].id, localidades[15].listAdjacencias[2], 5.2)

# # #ID 17 (JARDIM MUNICH)
g.adicionaAresta(localidades[16].id, localidades[16].listAdjacencias[0], 9.35)
g.adicionaAresta(localidades[16].id, localidades[16].listAdjacencias[1], 3.4)
g.adicionaAresta(localidades[16].id, localidades[16].listAdjacencias[2], 4.3)
g.adicionaAresta(localidades[16].id, localidades[16].listAdjacencias[3], 4.15)

# # #ID 18 (JARDIM OLIMPICO)
g.adicionaAresta(localidades[17].id, localidades[17].listAdjacencias[0], 2.5)
g.adicionaAresta(localidades[17].id, localidades[17].listAdjacencias[1], 4.15)
g.adicionaAresta(localidades[17].id, localidades[17].listAdjacencias[2], 2.5)
g.adicionaAresta(localidades[17].id, localidades[17].listAdjacencias[3], 6.4)

# # #ID 19 (JARDIM PARAISO)
g.adicionaAresta(localidades[18].id, localidades[18].listAdjacencias[0], 3)
g.adicionaAresta(localidades[18].id, localidades[18].listAdjacencias[1], 6.75)

# # #ID 20 (AEROPORTO REGIONAR DE MRG)
g.adicionaAresta(localidades[19].id, localidades[19].listAdjacencias[0], 5.2)
g.adicionaAresta(localidades[19].id, localidades[19].listAdjacencias[1], 3.55)
g.adicionaAresta(localidades[19].id, localidades[19].listAdjacencias[2], 6.54)

# # #ID 21 (PARQUE INDUSTRIAL)
g.adicionaAresta(localidades[20].id, localidades[20].listAdjacencias[0], 4)
g.adicionaAresta(localidades[20].id, localidades[20].listAdjacencias[1], 7.65)
g.adicionaAresta(localidades[20].id, localidades[20].listAdjacencias[2], 2.5)
g.adicionaAresta(localidades[20].id, localidades[20].listAdjacencias[3], 3.55)

# # #ID 22 (DISTRITO INDUSTRIAL 2)
g.adicionaAresta(localidades[21].id, localidades[21].listAdjacencias[0], 6.54)


# # #ID 23 (JARDIM NOVO HORIZONTE)
g.adicionaAresta(localidades[22].id, localidades[22].listAdjacencias[0], 1.75)
g.adicionaAresta(localidades[22].id, localidades[22].listAdjacencias[1], 2.65)
g.adicionaAresta(localidades[22].id, localidades[22].listAdjacencias[2], 7.1)
g.adicionaAresta(localidades[22].id, localidades[22].listAdjacencias[3], 6.4)


result = g.dijsktra(0)

print(result)



# 