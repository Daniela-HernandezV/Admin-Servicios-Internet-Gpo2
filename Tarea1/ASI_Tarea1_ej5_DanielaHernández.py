# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Administración de serviios de internet Gpo:2
# Hernández Vázquez Daniela - Mar,2025
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Programa que permite enviar un correo electrónico desde una cuenta Gmail/Outlook utilizando el protocolo SMTP a un destinatario específico
# ------------------------------------------------------------------------------------------------------------------------------------------------------
import smtplib
import ssl
import getpass      #Para contraseña segura
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "danycoronel4@gmail.com"     #Este es un correo al cual debes modificar para que acepte el ingreso de Python - Para ingresarlo manual usar la funcion input 
    password = getpass.getpass("Ingrese su contraseña: ")   #Esta contraseña solo se da una vez que se otorga acceso en el correo, asegurate de anotarla correctamente
    receiver_email = "angel.brito@fi.unam.edu"  #Destinatario a específico - Para ingresarlo manual usar la funcion input 

    subject = "Prueba de envío con SMTP"
    body = "Esta es una prueba de envio SMTP"
        
# -------------------------------------------------------
# Armar el mensaje
# -------------------------------------------------------
    message = MIMEMultipart("alternativo")      #estandar
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))    #texto plano

# -------------------------------------------------------    
# Configurar conexión SMTP segura por SSL
# -------------------------------------------------------
    context = ssl.create_default_context()  #conexion segura
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        print("Inició sesión!")
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Mensaje enviado exitosamente")    
    
# -------------------------------------------------------
# Llamar a la función
# -------------------------------------------------------
send_email()
