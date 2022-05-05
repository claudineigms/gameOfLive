from time import sleep
from os import system
from random import randint

'''
Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração
'''

#vizinhos=[supesq,sup,supdir,esq,dir,infesq,inf,infdir]
listaVizinhos=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
sociedade=[]

#config
altura=15
largura=30
individuos=175
tempo=1

def novo(thisAltura, ThisLargura):
    individuoExistente=False
    for individuo in sociedade:
        if individuo["coordenadaA"] == thisAltura and individuo["coordenadaL"]== ThisLargura:
            novo(randint(0,altura-1), randint(0,largura-1))
            individuoExistente=True
    if individuoExistente == False:
        sociedade.append({
            "coordenadaA":thisAltura,
            "coordenadaL":ThisLargura,
            "identificador": "\033[1;32m+",
            "vida":True,
            "proxIdentificador": "\033[1;32m+",
            "proxVida": True 
            })

def aleatorio(quantidade):
    for i in range(0,quantidade):
        novo(randint(0,altura-1),randint(0,largura-1))

def vizinhos(thisAltura,thisLargura):#AQUI SERÁ MAPEADO TODOS OS 8 VIZINHOS DO BLOCO PARA VERIFICAR SE ESTÁ EM ESTADO DE VIVO OU MORTO
    vizinhos = 0       
    IndividuoNaSociedade = None
    for individuo in sociedade:
        if (individuo["coordenadaA"] == thisAltura and 
            individuo["coordenadaL"] == thisLargura):
                IndividuoNaSociedade = individuo
        for vizinho in listaVizinhos:
            vizinhoAltura = thisAltura + vizinho[0]
            if vizinhoAltura < 0:
                vizinhoAltura = altura-1
            elif vizinhoAltura >= altura:
                vizinhoAltura = 0

            vizinhoLargura = thisLargura + vizinho[1]
            if vizinhoLargura < 0:
                vizinhoLargura = largura-1
            elif vizinhoLargura >= largura:
                vizinhoLargura = 0

            if (individuo["coordenadaA"] == vizinhoAltura and 
                individuo["coordenadaL"] == vizinhoLargura and
                individuo["vida"] == True):
                vizinhos += 1
    
    if vizinhos == 3 and IndividuoNaSociedade == None:
        novo(thisAltura,largura)
    elif IndividuoNaSociedade != None:
        if IndividuoNaSociedade["identificador"] == "\033[1;32m+": #nasce
            IndividuoNaSociedade["proxIdentificador"] = "\033[1;97mO"
            IndividuoNaSociedade["proxVida"] = True
            pass
        elif ((vizinhos < 2) or (vizinhos > 3)) and IndividuoNaSociedade["vida"] == True: #morreu
            IndividuoNaSociedade["proxVida"] = False
            IndividuoNaSociedade["proxIdentificador"] = "\033[1;31m•"
            pass
        elif IndividuoNaSociedade["identificador"] == "\033[1;31m•" and vizinho !=3: #apaga da sociedade
            sociedade.pop(sociedade.index(IndividuoNaSociedade))       
            pass
        elif IndividuoNaSociedade["identificador"] == "\033[1;31m•" and vizinho == 3: #Renasce
            IndividuoNaSociedade['proxIdentificador'] = "\033[1;32m+"
            IndividuoNaSociedade["proxVida"] = True
            pass
        elif IndividuoNaSociedade["vida"]==True and ((vizinho == 2) or (vizinho == 3)): #permanece vivo
            None
            pass

def novaDefinicao():
    for individuo in sociedade:
        individuo["identificador"] = individuo["proxIdentificador"]
        individuo["vida"] = individuo["proxVida"]

def novaGeracao():
    for i in range(altura):
        for j in range(largura):
            vizinhos(i,j)
    novaDefinicao()

def corpoIndividuo(posicaoAltura,posicaoLargura):
    for i in sociedade:
        if i["coordenadaA"] == posicaoAltura and i["coordenadaL"] == posicaoLargura:
            return (" "+i["identificador"]+" ")
    return "\033[1;90m . "
        
def main():
    aleatorio(individuos)
    system("cls") or None
    while range(0,3,+1):
        for mapaAltura in range(altura):
            for mapaLargura in range(largura):
                objeto = corpoIndividuo(mapaAltura,mapaLargura) #retornando se é um espaço ou indivíduo
                print(objeto,end=" ")
            print()
        print("\033[1;32m+\033[1;97m: Nasceu \n\033[1;97mO\033[1;97m: Vivo \n\033[1;31m•\033[1;97m: Morto\nDesafio feito é desafio completo @mrioqueiroz\nPrograma codado e finalizado por @claudineigms")
        novaGeracao()    
        sleep(tempo)
        system("cls") or None

main()
