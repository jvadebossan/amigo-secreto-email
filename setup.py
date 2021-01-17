from Sorteador import emails, nomes, main
from emailer import infos

quant = int(input('Quantas pessoas irão participar do amigo secreto? '))

for i in range(1, quant + 1):
    nome = input(f'Informe o nome do {i}º participante: ')
    email = input(f'Informe o email do {i}º participante: ')
    print('\n')
    nomes.append(nome)
    emails.append(email)

data = input('quando irá acontecer o evento?')
infos['data'] = data

msg = input('Digite uma mensagem extra para ser enviada no email: ')
infos['mensagem_extra'] = msg

print('\n\nPré visualização da mensagem que será enviada: \n')

print(f'''
    AMIGO SECRETO
    
    Seu amigo secreto é: (amigo).

    O evento acontecerá dia: {infos['data']}.

    {infos['mensagem_extra']}
''')
main()