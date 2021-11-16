from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text
from sqlalchemy import create_engine

#-------------------------------------------------------------------------------------------#
app = Flask(__name__, template_folder = 'templates/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hashirama@localhost/pythonassignment4'
db = SQLAlchemy(app)
#-------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------#
engine = create_engine('postgresql://postgres:hashirama@localhost/pythonassignment4')
#-------------------------------------------------------------------------------------------#


#-------------------------------------------------------------------------------------------#
class Usser(db.Model):
    __tablename__ = 'usser'
    usserid = db.Column('usserid', db.Integer, primary_key=True)
    login = db.Column('login', db.Unicode)
    password = db.Column('password', db.Unicode)


    def __init__(self,usserid,login,password):
        self.usserid = usserid
        self.login = login
        self.password = password


    loginn = ''
    passwordd = ''

    def tablefunc(id):
        with engine.connect() as connection:
            result = connection.execute(text("select login, password from usser where usser.usserid = "+str(id)))
            for row in result:
                global loginn, passwordd
                loginn = row['login']
                passwordd = row['password']
        connection.close()
#----------------------------------------------------------------------------------------------#



#----------------------------------------------------------------------------------------------#
class Articles(db.Model):
    __tablename__ = 'articles'
    idcoin = db.Column('coin_id', db.Integer, primary_key = True)
    coin_name = db.Column('coin_name', db.Unicode)
    article1 = db.Column('article1', db.Unicode)
    article2 = db.Column('article2', db.Unicode)
    article3 = db.Column('article3', db.Unicode)
    article4 = db.Column('article4', db.Unicode)
    article5 = db.Column('article5', db.Unicode)
    article6 = db.Column('article6', db.Unicode)
    article7 = db.Column('article7', db.Unicode)
    article8 = db.Column('article8', db.Unicode)
    article9 = db.Column('article9', db.Unicode)
    article10 = db.Column('article10', db.Unicode)


    def __init__(self, idcoin, coin_name, article1, article2, article3,article4,article5,article6,article7,article8,article9,article10):
        self.idcoin = idcoin
        self.coin_name = coin_name
        self.article1 = article1
        self.article2 = article2
        self.article3 = article3
        self.article4 = article4
        self.article5 = article5
        self.article6 = article6
        self.article7 = article7
        self.article8 = article8
        self.article9 = article9
        self.article10 = article10
#-----------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------#
#db.create_all()

#new_inf = Usser(1,'harakiriboy','mypassword') 
#db.session.add(new_inf)
#db.session.commit()
#-----------------------------------------------------------------------------------------#