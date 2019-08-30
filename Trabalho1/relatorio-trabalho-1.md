# Relatório de Implementação do Algoritmo A* (A Estrela)<br>

## Integrantes<br>
- Anne Caroline Silva: carolinesilva4@hotmail.com
- Mellyssa Stephanny de Jesus Mendes: mellyssah.mendes@gmail.com

## 1. Introdução<br>
Neste relatório, vamos explicar como foi feita a implementação do Algoritmo A* (lê-se A-Estrela) para traçar o melhor caminho (utilizando heurísticas), 
partindo de um ponto inicial até o ponto final, onde o mesmo somente se movimenta em linha reta e rotaciona 90 graus, desviando de alguns obstáculos no caminho.

## 2. Explicação Teórica do Algoritmo<br>
A* ("A-star") é um dos métodos mais populares para encontrar o caminho mais curto entre dois locais em uma área mapeada. 
A* foi desenvolvido em 1968 para combinar abordagens heurísticas como Best-First-Search (Busca em Largura) e abordagens formais como o algoritmo de Dijsktra.
 
O algoritmo A* avalia os nós através da combinação de g(n) que é o custo para alcançar cada nó com a função h(n) que é o menor custo partindo da origem para 
se chegar ao destino, matematicamente dado na equação:
> **F(n) = G(n) + H(n)**

onde,
* G(n): custo do caminho do nó inicial para n;
* H(n): função heurística que estima o custo do caminho mais barato de n para a meta;
* F(n): n é o próximo nó no caminho.

As características definidoras do algoritmo A* são a construção de uma "lista fechada" para registrar áreas já avaliadas, uma lista aberta para registrar 
áreas adjacentes àquelas já avaliadas e o cálculo das distâncias percorridas desde o "ponto inicial" com distâncias estimadas até o "ponto objetivo".
 
A lista aberta, é uma lista de todos os locais imediatamente adjacentes a áreas que já foram exploradas e avaliadas (a lista fechada). A lista fechada é 
um registro de todos os locais que foram explorados e avaliados pelo algoritmo.

## 3. Problema Proposto
Implementar o algoritmo A* para resolver o seguinte problema:
 
> Dado um mapa com obstáculos, o algoritmo deve traçar o caminho menos custoso, do ponto inicial até o ponto final.

Nosso mapa vem em um arquivo .txt, composto de 0’s e 1’s, onde 0 representa o caminho livre e 1 representa o obstáculo. Além disso, temos ponto de partida e 
chegada, que chamamos, respectivamente, de ponto inicial e ponto final. Nossa implementação devia obedecer algumas restrições:
* Leitura do mapa através de arquivo;
* Uso de diferentes mapas;
* Uso de heurística para reconhecer o caminho de menor custo;
* Locomover-se somente em linha reta ou em 90º;
* Ao final, mostrar um mapa com o caminho percorrido, juntamente com uma lista contendo as  coordenadas utilizadas.

Como heurística, escolhemos heurística de Manhattan, que  tem esse nome pois define a menor distância entre quarteirões numa malha urbana reticulada 
ortogonal, como na própria zona da Cidade de Manhattan, EUA.

![Legenda](url da img)

Figura 1: Representação da menor distância possível que um carro é capaz de percorrer numa malha urbana reticulada ortogonal

Na figura abaixo, temos a representação de um mapa, onde cada quadrado representa uma coordenada. O quadrado vermelho representa o ponto de partida, o verde o 
destino e os pretos são os obstáculos.

![Legenda](url da img)

Figura 2: Exemplo de caminho a ser percorrido pelo algoritmo

## 4. Implementação<br>

Esse é um algoritmo guloso, em cada iteração ele faz a escolha que parece ser a melhor possível de acordo com algum critério (Best-First Search).
Para ser eficiente, o algoritmo armazena um conjunto de estados não explorados chamado de franja (do inglês, fringe). Inicialmente, a franja possui 
apenas o estado inicial. Na iteração seguinte, o estado inicial já foi explorado e a partir daí a franja armazena os estados sucessores do estado 
inicial. Com isso, o algoritmo vai montando um caminho passo-a-passo que permite escolher qual estado está mais próximo da meta.
A linguagem escolhida para a implementação do algoritmo é Python, ela tem ganho popularidade, e é a linguagem que estamos familiarizadas no curso.

### Trechos mais importantes do código<br>