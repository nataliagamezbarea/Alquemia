
from flask_mail import Mail, Message


# Instancia de Flask-Mail global
mail = Mail()

# Función para enviar_correos porque luego la vamos a utilizar
def enviar_correo(app, asunto, destinatario, cuerpo):
   mail.init_app(app) 
   # Pones el asunto y el destinatario que lo pasas como parámetro
   msg = Message(asunto, recipients=[destinatario])
   # El cuerpo del correo es el m ensaje
   msg.body = cuerpo
   # Finalmente mandas el mensaje
   mail.send(msg)