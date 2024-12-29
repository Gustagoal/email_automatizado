import pandas as pd 
import time
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

internet = pd.read_html("https://pt.wikipedia.org/wiki/Lista_de_campe%C3%B5es_da_Copa_Libertadores_da_Am%C3%A9rica") # read_html esta pegando os dados de um site , nesse caso Wikepedia

tabela = internet[1]["Campeão"] # selecionando apenas a 2 tabela do site , filtrando somente a coluna do "Campeão"

tabela.to_excel("libertadores.xlsx",index=False) # converte para o excel o arquivo armazenado na variavel "tabela"

# variaveis para realizar o envio 
server = "smtp.gmail.com" # email padrão para conectar com o servidor 
porta = 587 # porta padrão de acesso ao gmai 
send_email = "python@gmail.com" # colocar o gmail que vai ralizar o envio 
senha = "#" # colocar a senha do gmail 

# laço de repetição para percorrer cada linha do excel da tabela 
for i in tabela:
    recebimento = "python@gmail.com" # email que vai receber 
    assunto = "Campeão da libertadores"
    descrição = f"Esse time foi campeão da libertadores {i}"
    time.sleep(3)

    # configuração na personalização da mensagem 
    mensagem = MIMEMultipart()
    mensagem["From"] = send_email
    mensagem["To"] = recebimento
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(descrição,"plain")) # "Plain" utilizado para descrição padrão da mensagem
 
    #conexão com o servidor 
    try:
        servidor = smtplib.SMTP(server,porta)
        servidor.starttls() # realiza a conexão com o servidor

        servidor.login(send_email,senha)
        servidor.sendmail(send_email,recebimento,mensagem.as_string()) # "as_string " para converter o objeto para string
        
        print("Email enviado com exito")

    except Exception as e:
        print("Ops houve um erro , tente novamente ")
        print(f"Erro {e}")

    finally:
        servidor.quit()   # termina com o encerramento no servidor 






