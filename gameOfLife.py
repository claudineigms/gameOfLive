from time import sleep
from os import supports_dir_fd, system
from random import randint
'''
Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração

REGRAS A PROGRAMAR
- INTERFAÇE: CONCLUÍDO
- OBJETOS
- GERAÇÃO ALEATÓRIA

STATUS
VIVO/MORTO (TRUE/FALSE)
'''

#vizinhos=[supesq,sup,supdir,esq,dir,infesq,inf,infdir]
listaVizinhos=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
sociedade=[]
#config

altura=5
largura=5
individuos=15
tempo=2

def novo(altura, largura):
    """for individuo in sociedade:
        if individuo["coordenadaA"] == altura and individuo["coordenadaL"]== largura:
            novo(randint(0,altura), randint(0,largura))
            print("Já existe um individuo com essas corrdenadas")"""
    sociedade.append({
        "coordenadaA":altura,
        "coordenadaL":largura,
        "identificador": "+",
        "vida":False
        })

def nome():
    return str(len(sociedade)+1)

def aleatorio(quantidade):
    for i in range(0,quantidade):
        novo(randint(0,altura-1),randint(0,largura-1))

def vizinhos(altura,largura):#AQUI SERÁ MAPEADO TODOS OS 8 VIZINHOS DO BLOCO PARA VERIFICAR SE ESTÁ EM ESTADO DE VIVO OU MORTO
    vizinhos = 0       #1CLAUDINEI, CE TA FAZENDO MERDA AQUI
    IndividuoNaSociedade = None
    for individuo in sociedade:
        if (individuo["coordenadaA"] == altura and 
                individuo["coordenadaL"] == largura):
                IndividuoNaSociedade = individuo
        for vizinho in listaVizinhos:
            vizinhoAltura = altura + vizinho[0]
            vizinhoLargura = largura + vizinho[1]
            if (individuo["coordenadaA"] == vizinhoAltura and 
                individuo["coordenadaL"] == vizinhoLargura and
                individuo["vida"] == True):
                vizinhos += 1
        #3DICA, JOGA ESSA PORRADA DE IF PARA TRÁS, E CRIA UMA NOVA VARIAVEL VIZINHO, ESPERO QUE LEMBRE DISSO AMANHA
    if vizinhos == 3 and IndividuoNaSociedade == None:
        novo(altura,largura)
    elif IndividuoNaSociedade != None:
        if IndividuoNaSociedade["identificador"] == "+": #2PERCEBE QUE... VOCÊ TA TENTANDO ALTERAR CADA INDIVIDUO DA SOCIEDADE (VOCÊ PRECISA SÓ VERIFICAR OS VIZINHOS, E COM O TOTAL DELES SABER O QUE VAI FAZER)
            IndividuoNaSociedade['identificador'] = "O"
            IndividuoNaSociedade["vida"] = True
        elif ((vizinhos < 2) or (vizinhos > 3)) and IndividuoNaSociedade["vida"] == True: #morreu
            IndividuoNaSociedade["vida"] = False
            IndividuoNaSociedade["identificador"] = "•"
        elif IndividuoNaSociedade["identificador"] == "•": #morreu
            print(sociedade.index(IndividuoNaSociedade))
            sociedade.pop(sociedade.index(IndividuoNaSociedade))       
        elif IndividuoNaSociedade["identificador"] == "+" and IndividuoNaSociedade["vida"]==True and vizinho == 2 or vizinho == 3: #permanece vivo
            IndividuoNaSociedade["identificador"] = "O"

def novaGeracao():
    for i in range(altura):
        for j in range(largura):
            vizinhos(i,j)

def individuo(altura,largura):
    for i in sociedade:
        if i["coordenadaA"] == altura and i["coordenadaL"] == largura:
            return (" "+i["identificador"]+" ")
    return " . "
        

def main():
    system("cls") or None
    while range(0,3,+1):
        for i in range(altura):
            for j in range(largura):
                objeto = individuo(i,j) #retornando se é um espaço ou indivíduo
                print(objeto,end=" ")
            print()
        novaGeracao()    
        sleep(tempo)
        system("cls") or None

aleatorio(individuos)
main()