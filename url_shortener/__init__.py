from flask import Flask #Basic flask dependecies
from flask_sqlalchemy import SQLAlchemy #Database connection and ORM
from flask_bcrypt import Bcrypt #Hashing and CSRF token
from flask_login import LoginManager #Login Manager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C7p8HXmViPghCJSEJpkSZKMZiJrPcPHp2DjSgnL57z4ubgm8pP'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/url_shortener'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# Uncomment the two lines below to implement default login page
# login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'

from url_shortener import routes #import routes to be used with the web page
