from random import choice, randint
from emailer import main as enviar

emails = [
]

nomes = [
]

sorteados = []

amigos_sorteadas = []

def main():
    while (len(sorteados) <= len(nomes)):
        index = randint(0, len(nomes) -1)
        pessoa = emails[index]
        #nome_pessoa = nomes[index]
        if (pessoa not in sorteados):
            index2 = randint(0, len(nomes) - 1)
            amigo = emails[index2]
            nome_amigo = nomes[index2]
            if (amigo != pessoa and amigo not in amigos_sorteadas):
                amigos_sorteadas.append(amigo)
                sorteados.append(pessoa)
                #print("O amigo secreto de", nome_pessoa, "é o ", nome_amigo)
                enviar(pessoa, nome_amigo)
