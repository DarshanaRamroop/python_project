#import the flask module
from flask import Flask
import os


from flask_mail import Mail, Message
mail = Mail()
#create an instance of the flask class and name it app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'darshanasramroop@gmail.com'
    app.config['MAIL_PASSWORD'] = 'jtsoypzfiqfxcoea'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)
    
   
    
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app