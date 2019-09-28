class Node():
    # classe no
    def __init__(self, parent=None, position=None):
        self.g = 0
        self.h = 0
        self.f = 0

        self.parent = parent
        self.position = position

    def __le__(self, other):
        return self.f <= other.f

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        if other is None:
            return False
        return self.position == other.position

def heuristica(pAtual, pProx):
    # distancia de manhattan
    (x1, y1) = pAtual.position
    (x2, y2) = pProx.position
    return abs(x1 - x2) + abs(y1 - y2)


def astar(mapa, ini, fim):
    # instancia o no inicial e final
    noInicial = Node(None, ini)
    noInicial.g = noInicial.h = noInicial.f = 0
    noFinal = Node(None, fim)
    noFinal.g = noFinal.h = noFinal.f = 0

    # cria a "lista aberta" e a "lista fechada"
    listaAberta = []
    listaFechada = []

    # adiciona o no inicial a lista aberta
    listaAberta.append(noInicial)

    # cria uma variavel flag para saber se o alvo foi encontrado
    achou = False
    # lista que guarda o caminho percorrido ate o no final
    path = []

    # percorre o mapa ate encontrar o fim
    while achou == False:
        # pesquisa o no com menor F da lista aberta
        noCorrente = min(listaAberta)
        # remove o no corrente da lista aberta
        index = listaAberta.index(noCorrente)
        listaAberta.pop(index)
        # adiciona o no corrente na lista fechada
        listaFechada.append(noCorrente)

        for pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            # pega as posicoes de todos os nos adjacentes
            posAdj = (noCorrente.position[0] + pos[0], noCorrente.position[1] + pos[1])
            # cria um no com as posicoes adjacentes
            noAdjacente = Node(None, posAdj)

            if posAdj[0] < 0 or posAdj[1] < 0 or posAdj[0] >= len(mapa) or posAdj[1] >= len(mapa[-1]):
                continue
            if mapa[posAdj[0]][posAdj[1]] == 1 or noAdjacente in listaFechada:
                continue
            
            if noAdjacente not in listaAberta:
                # fazendo o no corrente ser o pai do no adjacente
                noAdjacente.parent = noCorrente              
                # calculo dos parametros g h f
                noAdjacente.g = noAdjacente.g + 10
                noAdjacente.h = heuristica(noAdjacente, noFinal)
                noAdjacente.f = noAdjacente.g + noAdjacente.h
                # adicionando na lista aberta
                listaAberta.append(noAdjacente)
            else:
                if (noAdjacente in listaAberta) and (noAdjacente.g < noCorrente.g):
                    # calculo dos parametros g h f
                    noAdjacente.g = noAdjacente.g + 10
                    noAdjacente.f = noAdjacente.g + noAdjacente.h
                    noAdjacente.parent = noCorrente

        # condiçoes de parada
        if len(listaAberta) == 0 or noCorrente == noFinal:
            no = noCorrente
            while no is not None:
                path.append(no.position) 
                no = no.parent # adiciona os pais na lista path
            achou = True
    return path[::-1] # retorna o caminho reverso

def desenhaCaminho(mapa, caminho):
    for item in caminho:
        mapa[item[0]][item[1]] = '*'
    print()
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            print(" ", mapa[i][j], end= "")  
        print()


def main():
    # fazer a leitura de arquivo

    # definição do mapa
    mapa = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    # definição dos pontos de inicio e fim
    ini = (0, 0)
    fim = (9, 8)

    # chamada da funcao astar
    caminho = astar(mapa, ini, fim)

    # imprime as coordenadas dos pontos percorridos
    print("Caminho percorrido: ", caminho)

    # imprime o caminho percorrido
    desenhaCaminho(mapa, caminho)

if __name__ == '__main__':
    main()
