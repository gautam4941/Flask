from flask import  Flask, request
from flask_restful import Resource, Api

app = Flask( __name__ )
print( f"app = { app }" )
api = Api( app )
print( f"api = { api }" )

Item_list = []

class Item( Resource ):
    def get(self, name):
        print( f"Inside GeT -> Item_name = { name }" )
        for i in Item_list:
            if( i['name'] == name ):

                return { 'Item_Detail' : i }

        return { "Message" : f"{ name } Item is not present in the list" }, 404

    def post(self, name):
        print(f"Inside Post -> Item_name = {name}")
        Item_list.append( { 'name' : name, 'price' : 12 } )
        return { 'Message' : f'{ name } Item inserted in the Item_list' }, 201

    def delete(self, name):
        print(f"Inside Delete -> Item_name = {name}")

        global Item_list
        len_before_delete = len(Item_list)
        Item_list = list( filter( ( lambda x : x['name'] != name ), Item_list ) )

        if( len_before_delete == len(Item_list) ):
            return { "Message" : f"{ name } Item doesn't exist in the Item List"}

        return { "Message" : f"{ name } Item Deleted from the Item List"}

    def put(self, name):
        print(f"Inside Put -> Item_name = {name}")
        request_data = request.get_json()

        index = -1
        item_found = False

        for item in Item_list:
            index = index + 1

            if( item['name'] == name ):
                item_found = True
                break

        if( item_found ):
            Item_list[index]['price'] = request_data['price']
            return {'Message': f"{name} Item's price has been update in the list"}
        else:
            Item_list.append({'name': name, 'price': request_data['price']})
            return {'Message': f'{name} Item has been added to the list at it was not present before update'}

class Items(Resource):
    def get(self):
        if( len( Item_list ) > 0 ):
            return { "Following is the Details of Items present in Item_List\n" : Item_list }

        return "No Item Data is present in the Item List"

api.add_resource( Item, '/Item/<string:name>' )
api.add_resource( Items, '/Items' )

app.run( port=12345, debug = True )