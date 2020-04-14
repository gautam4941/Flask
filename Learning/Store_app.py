from flask import  Flask, jsonify, request

app = Flask( __name__ )

store_list = [
    {
        'name' : 'Store1'
        ,'items' : [
                    {
                        'item_name' : 'Item 1'
                        ,'price' : 15.99
                    }
                    ]
    }
]

@app.route( '/', methods = ['GET'] )
def home():
    return jsonify( { 'Available Options\n' :
                          """1. /see_stores, 2. /see_store/<string:name>
    ,3. /see_item/<string:name>/items, 4. /create_new_store
    ,5. /create_new_item/<string:name>/item""" } )

# GET /store
@app.route( '/see_stores', methods = [ 'GET' ] )
def get_stores():
    return jsonify( { 'stores' : store_list } )

# POST /store
@app.route('/create_new_store', methods = [ 'POST' ] )
def post_store():
    request_data = request.get_json()
    new_store_name = request_data['name']

    new_store = {
                    'name' : new_store_name
                    ,'items' : []
                }
    store_name_already_exist = False

    for i in store_list:
        if( i['name'].lower() == new_store_name.lower() ):
            store_name_already_exist = True

    if( store_name_already_exist == False ):

        store_list.append( new_store )
        return jsonify( { 'Message' : f'Successfully new store has been inserted \n{ store_list[ len( store_list ) - 1 ] }' } )
    else:
        available_store_names = []
        for i in store_list:
            available_store_names.append( i['name'] )

        return jsonify( { 'Message' : f"Given Store Name : { new_store_name } already exist. Available stores are \n{ available_store_names }" } )


# GET /store/< string : name >
@app.route( '/see_store/<string:name>', methods = [ 'GET' ] )
def get_store( name ):
    for i in store_list:

        if( i['name'] == name ):
            return jsonify( { 'store_info' : i } )

    return jsonify( { 'Message' : f'There no store of name = { name }' } )

# POST /store/<string : name >/item { name : price }
@app.route( '/create_new_item/<string:store_name>/item', methods = [ 'POST' ] )
def post_store_item( store_name ):
   request_data = request.get_json()

   print( f"store_name = { store_name }" )

   found_index = -1
   store_name_existance = False
   for i in range( len( store_list ) ):
       if( store_list[i]['name'].lower() == store_name.lower() ):
           store_name_existance = True
           new_item = request_data['item_name']
           break

   if( store_name_existance ):

       for item in store_list[found_index]['items']:
           if( item['item_name'] == new_item ):
               old_price = item['price']
               item['price'] = request_data['price']

               return jsonify( {'Message' : f'Price of Item : { new_item } has been updated from { old_price } to { item["price"] }'} )

       store_list[found_index]['items'].append( {
           'item_name' : new_item
           ,'price' : request_data['price']
       } )
       return jsonify( { 'Message' : f'Successfully items has been inserted in store : {store_name} and changed store is : \n{ store_list[found_index] } ' } )

   else:
       return jsonify( { 'Message' : f'Item has not been inserted in the store List : \n{ store_name } as it doesn;t exist' } )


# GET /store/<string:name>/item
@app.route( '/see_item/<string:name>/items', methods = [ 'GET' ] )
def get_store_item( name ):

    for i in store_list:
        if( i['name'] == name ):
            return jsonify( { 'Items Details' : i['items'] } )

app.run( port=12345 )