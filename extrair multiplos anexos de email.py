import imaplib
import email

server = 'Outlook.office365.com'
user = 'USUARIO'
password = 'SENHA'
outputdir = 'DIRETORIO ONDE QUER OS ARQUIVOS'
subject = 'Data Exports' #BAIXAR DE UM ASSUNTO ESPECIFICO


def connect(server, user, password):
    m = imaplib.IMAP4_SSL(server)
    m.login(user, password)
    m.select()
    return m

def downloaAttachmentsInEmail(m, emailid, outputdir):
    resp, data = m.fetch(emailid, "(BODY.PEEK[])")
    email_body = data[0][1]
    mail = email.message_from_bytes(email_body)
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))

#BAIXAR O ANEXO DE TODOS OS ARQUIVOS COM O ASSUNTO ESPECIFICO

def downloadAttachments(subject):
    m = connect(server, user, password)
    m.select("Inbox")
    typ, msgs = m.search(None, '(SUBJECT "' + subject + '")')
    msgs = msgs[0].split()
    for emailid in msgs:
        downloaAttachmentsInEmail(m, emailid, outputdir)

downloadAttachments(subject)
