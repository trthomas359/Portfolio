import imaplib
import email
import os
import base64

#conectando servidor do gmail com IMAP

objCon = imaplib.IMAP4_SSL("imap.gmail.com")
login = "email"
senha = "senha"

objCon.login(login,senha)

#ir em configuracoes no gmail pop/imap - enable IMAP
#ir em seguranca - acesso a app menos seguro

objCon.list()
objCon.select(mailbox='inbox', readonly=True)

resposta,idDosEmails = objCon.search(None,'All')

#colocando em loop cada id do email
for num in idDosEmails[0].split():
    print(num)
#decodifica o email jogando as partes em uma variavel

    resultado, dados = objCon.fetch(num,'(RFC822)')
    texto_do_email = dados[0][1]
    texto_do_email = texto_do_email.decode('utf-8')
    texto_do_email = email.message_from_string(texto_do_email)
    # print(texto_do_email) corpo do e-mail
    #loop as partes do email
    for part in texto_do_email.walk():
        #se tiver anexo pegar o nome do anexo
        if part.get_content_maintype()  == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

#pegando o nome do arquivo em anexo, criando arquivo na pasta local, colocando o binario no arquivo criado
        fileName = part.get_filename()
        print(fileName)
        arquivo = open(fileName,'wb')
        arquivo.write(part.get_payload(decode=True))
        arquivo.close()
