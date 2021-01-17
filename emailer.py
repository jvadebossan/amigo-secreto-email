#from Sorteador import part
import smtplib
from Sorteador import emails, nomes
from email.message import EmailMessage

infos = {'data':'', 'mensagem_extra':''}

def main(email, amigo):
    print(f'Enviando e-mails...\n Tempo estimado: {len(nomes) * 3} segundos')
    msg = EmailMessage()
    msg.set_content(f'''
        AMIGO SECRETO
        
        Seu amigo secreto é: {amigo}.

        O evento acontecerá dia: {infos['data']}.

        {infos['mensagem_extra']}
    ''')

    msg['Subject'] = 'Amigo Secreto'
    msg['From'] = 'emaildetestesdojv@gmail.com'
    msg['To'] = email

    smtp = "smtp.gmail.com"
    server = smtplib.SMTP(smtp, 587)
    server.starttls()

    server.login(msg['From'], 'senhadoemaildetestes')

    server.send_message(msg)
    server.quit()
print('Todos os emails foram enviados!\nObrigado por usar nosso app ;)')
