from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item, Itemlist
from resources.store import Store,Storelist

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE_EXCEPTIONS']=True
app.secret_key='abbas'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


jwt=JWT(app,authenticate,identity)


api.add_resource(Store,'/store/<string:name>')
api.add_resource(Storelist,'/stores')
api.add_resource(Item,'/item/<name>')
api.add_resource(Itemlist,'/items')
api.add_resource(UserRegister,'/register')

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run()