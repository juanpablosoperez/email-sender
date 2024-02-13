# ir a nuestra cuenta de correo electrónico y configure la autenticación de 2 factores
# generar contrasena app
# crear funcion que envie el email
import smtplib


def enviar_correo(destinatario, asunto, mensaje):
    # Configurar los detalles del servidor SMTP
    servidor_smtp = 'smtp.gmail.com'
    puerto_smtp = 587
    remitente = 'juansopesabalero2014@gmail.com'
    contrasena = 'pkul aaxp fhkm mnrw'

    # Crear una conexión segura al servidor SMTP
    servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
    servidor.starttls()
    servidor.login(remitente, contrasena)

    # Crear el mensaje de correo electrónico
    mensaje_correo = f'Subject: {asunto}\n\n{mensaje}'

    # Enviar el correo electrónico
    servidor.sendmail(remitente, destinatario, mensaje_correo)

    # Cerrar la conexión con el servidor SMTP
    servidor.quit()


# Ejemplo de uso
destinatario = 'juanpsoperez@gmail.com'
asunto = 'Hola'
mensaje = 'Hola, esto es un correo de prueba.'

enviar_correo(destinatario, asunto, mensaje)

