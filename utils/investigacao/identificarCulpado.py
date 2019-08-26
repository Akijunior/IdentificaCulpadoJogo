import random

from utils.investigacao.opcoes import suspeitos, armas, locais, respostas


def identificarCulpado():
    acertou = False

    assassinoCerto = random.choice(range(len(suspeitos)))
    armaCerta = random.choice(range(len(armas)))
    localCerto = random.choice(range(len(locais)))

    while (not acertou):

        listarOpcoes(suspeitos)

        assassino = int(input('Quem é o assassino?\n'))

        listarOpcoes(armas)

        arma = int(input('Qual foi a arma?\n'))

        listarOpcoes(locais)

        local = int(input('Qual foi o local do crime?\n'))

        print(assassinoCerto, ' - ', armaCerta, ' - ', localCerto)

        acertou = checaResposta(assassino, assassinoCerto, arma, armaCerta, local, localCerto)

    '''
    Se a teoria estiver correta (assassino, local e arma corretos), ela responde 0. 
    Se a teoria está errada, um valor 1, 2 ou 3 é retornado. 
    1 indica que o assassino está incorreto; 
    2 indica que o local está incorreto; 
    3 indica que a arma está incorreta. 
    Se mais de uma suposição está incorreta,
    ela retorna um valor arbitrário entre as que estão incorretos (isso é totalmente aleatório).
    '''

def checaResposta(assassino, assassinoCerto, arma, armaCerta, local, localCerto):

    acertou = False
    if (assassino == assassinoCerto and arma == armaCerta and local == localCerto):
        acertou = True
        print(respostas[0], '\n')

    elif (assassino != assassinoCerto):
        print(respostas[1], '\n')

    elif (arma != armaCerta):
        print(respostas[2], '\n')

    elif (local != localCerto):
        print(respostas[3], '\n')

    else:
        print(respostas[random.choice(1, len(respostas))], '\n')

    return acertou


def listarOpcoes(lista):
    print('\n')
    for i in range(len(lista)):
        print("%d - %s" % (i + 1, lista[i]))
    print('\n')

def listarOpcoesView(lista):
    listaAdaptada = []
    for i in range(len(lista)):
        listaAdaptada.append("%d - %s" % (i + 1, lista[i]))
    return listaAdaptada

# identificarCulpado()
