import re
import emailer

padrao_email = '\w{2,50}@\w{2,15}\.[a-z]{2,3}'

while True:
    destinatario = input(str('Informe o e-mail que deseja enviar o relatório: '))
    eh_email = re.findall(padrao_email, destinatario)
    
    if not eh_email :
        print(f'Email inválido!! \nPor favor insira um email válido [teste@exemplo.com]')
    else :
        break
    
obj = WebScraping()
obj.iniciar()
emailer.envia_email(destinatario)