from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'store not found'}

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message':'a store with name already exists'}
        store=StoreModel(name)
        store.save_to_db()
        return store.json()


    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db
        return {'message':'store deleted'}

class Storelist(Resource):
    def get(self):
        return {'stores':list(map(lambda x:x.json(), StoreModel.query.all()))}