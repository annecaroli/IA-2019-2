def heuristica(pAtual, pProx):
	# distancia de manhattan
    (x1, y1) = pAtual
    (x2, y2) = pProx
    return abs(x1 - x2) + abs(y1 - y2)
	
def funcaoHeuristica(pAtual, pFim):
	# definimos o custo como igual a 10 tendo em vista velocidade
	# de processamento
	g = 10 # custo do movimento
	
	h = heuristica(pAtual, pFim) * custo
	
	return h + g
	

def astar(mapa, ini, fim)
	# cria a "lista aberta" e a "lista fechada"
	listaAberta = []
	listaFechada = []
	
	# adiciona o no inicial a lista aberta
	listaAberta.append(ini)
	
	# percorre o mapa ate encontrar o fim
	while len(listaAberta) > 0:
		# pega o no atual
		noAtual = listaAberta[0]
		indiceAtual = 0
		
		# percorre a lista aberta e procura pelo menor F
		for index, item in enumerate(listaAberta): 
            if funcaoHeuristica(item, fim) < funcaoHeuristica(noAtual, fim):
                noAtual = item
                indiceAtual = index
				
		# retira o noAtual da lista aberta e adiciona na listaFechada
        listaAberta.pop(indiceAtual)
        listaFechada.append(noAtual)
		
		# se o no objetivo for encontrado 
		if noAtual == fim:
            # lista para guardar os nos percorridos no mapa
			# os elementos sao adicionados do no fim ao no inicial
			caminho = []
			
            current = current_node # nao entendi direito
            while current is not None:
                path.append(current.position)
                current = current.parent
            return caminho[::-1] # o retorno eh a lista so que ao contrario
		
		# percorre os nos adjacentes - lembrando que o movimento é apenas ortogonal
		for pos in [(-1,0), (0,1), (1,0), (0,-1)]:
			#pega um no adjacente
			noAdjacente = (noAtual.position[0] + pos[0], noAtual.position[1] + pos[1])
			
			# determina que o no esteja dentro dos limites do mapa e nao seja um obstaculo
			if (noAdjacente[0] < len(mapa) - 1 or noAdjacente[0] < 0 or
			   noAdjacente[1] < (len(mapa[len(mapa)-1]) - 1) or noAdjacente[1] < 0)
			   and mapa[noAdjacente[0],noAdjacente[1]] != 0:
			   continue
			else:
				if noAdjacente not in listaAberta:
					listaAberta = noAdjacente
				else:
					
	


def main():

	# definição do mapa
	mapa = [[0,0,1,0,0,0,0,0,0,0],
			[0,0,1,0,0,0,0,0,0,0],
			[0,0,1,0,0,0,0,0,0,0],
			[0,0,1,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,1,1,1],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,1,0,0,0,0,0],
			[0,0,0,0,1,0,0,1,1,1],
			[0,0,0,0,1,0,0,0,0,0],
			[0,0,1,0,0,0,0,0,0,0]]
			
	# definição dos pontos de inicio e fim
	ini = (0,0)
	fim = (8,0)
	
	# chamada da funcao astar
	caminho = astar(mapa, ini, fim)
	
	# imprime o caminho percorrido
	print(caminho)
	
	# depois fazer um print do caminho percorrido no mapa
	# que nem o exemplo que o profe mandou
	
	# na versão 2 do algoritmo, fazer a leitura de arquivo

if __name__=='__main__':
	main()