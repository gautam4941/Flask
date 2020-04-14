from flask import Flask
from flask_restful import Resource, Api

#We are importing there 2 functions which will be user as login gateway
from flask_jwt import JWT, jwt_required
from JWT_Security import authenticate, identity

app = Flask( __name__ )
api = Api( app )                                #Adding Flask( __name__ )/app object to Api object i.e., api
jwt = JWT( app, authenticate, identity )        #Adding Flask( __name__ )/app object to JWT object i.e., jwt

print( f"app = { app }" )
print( f"api = { api }" )

Item_list = []

class Item( Resource ):

    @jwt_required()
    def get(self, name):
        print( f"Inside GeT -> Item_name = { name }" )
        for i in Item_list:
            if( i['name'] == name ):
                return { 'Item_Detail' : i }, 200

        return { "Message" : f"{ name } Item is not present in the list" }, 404

    def post(self, name):
        print(f"Inside Post -> Item_name = {name}")

        for item in Item_list:
            if( item['name'].lower() == name.lower() ):
                return { 'Message' : f'{ name } Item already exist in the Item_list' }, 400

        Item_list.append( { 'name' : name, 'price' : 12 } )
        return { 'Message' : f'{ name } Item inserted in the Item_list' }, 201

class Items(Resource):
    def get(self):
        if( len( Item_list ) > 0 ):
            return { "Following is the Details of Items present in Item_List\n" : Item_list }

        return "No Item Data is present in the Item List"

api.add_resource( Item, '/Item/<string:name>' )
api.add_resource( Items, '/Items' )

app.run( port=12345, debug = True )