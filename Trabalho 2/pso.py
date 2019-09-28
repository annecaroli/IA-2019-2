#############################################
# Otimização por Enxame de Partículas
# Anne Caroline Silva
# Mellyssa Stephanny de Jesus Mendes
# Inteligência Artificial - 2019/2
# ###########################################

import random
import math


# funcao a ser otimizada (minimizada)
def Eggholder(x,y):
    return (- (y+47) * math.sin(math.sqrt(abs(x/2)+(y+47))) - (x*math.sin(math.sqrt(abs(x-(y+47))))))


# definicao das particulas que serao tratadas como uma classe
class Particula:
    def __init__(self, posicao, velocidade, pBest):
        self.posicao = [random.uniform(-512,512), random.uniform(-512,512)]           # localizacao individual
        self.velocidade = [random.uniform(-77,77), random.uniform(-77,77)]            # velocidade individual
        self.pBest = pBest               # melhor posicao individual
        

                    
# atualiza a velocidade da particula
def atualizaVelocidade(self,pos_best_g):
    w=0.5       # ponderacao de inercia
    c1=1        # constante congnitiva
    c2=2        # constante social

    for i in range(0,2):
        r1=random.random()
        r2=random.random()

        vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
        vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
        self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

# atualiza a posicao da particula
def atualizaPosicao(self):
    front = [-512, 512]

    for i in range(0 , 2):
        self.posicao[i] = self.posicao[i] + self.velocidade[i]

        # ajuste caso a particula extrapole as fronteiras
        if self.posicao[i] > front[1]:
            self.posicao[i] = front[1]
        if self.posicao[i] < front[0]:
            self.posicao[i] = front[0]


def main():
    # definicao das variaveis
    numParticulas = 20
    numExec = 10
    numPopulacao = [20, 50, 100]

    # cria e inicializa as particulas
    enxame = []
    for i in range(0,20):
        enxame.append(Particula(0,0,0))
    
    # teste
    for aux in range(len(enxame)):
        print("pos", enxame[aux].posicao)
        print("vel", enxame[aux].velocidade)
        print()
   

    # processamento do pso
    i = 0
    while i < numExec:

        i+=1

if __name__ == "__main__":
    main()