from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=int,required=True,help='this field cannot be left blank')

    parser.add_argument('store_id', type=int, required=True, help='every item needs a store id')

    @jwt_required()
    def get(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'}



    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message':'the item already exists'}

        data=Item.parser.parse_args()
        item=ItemModel(name,**data)
        item.save_to_db()
        return item.json()




    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message':'item deleted'}
        return {'message':'item not found'}


    def put(self,name):
        data=Item.parser.parse_args()
        item=ItemModel.find_by_name(name)

        if item:
            item.price=data['price']
        else:
            item=ItemModel(name,**data)
        item.save_to_db()
        return item.json()



class Itemlist(Resource):
    def get(self):
        return {'items':list(map(lambda x:x.json(),ItemModel.query.all()))}