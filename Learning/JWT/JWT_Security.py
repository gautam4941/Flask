from User_Class import User

users = [ User( 1, 'Gautam', '1234' ) ]

username_mapping = { user.username : user for user in users }
userid_mapping = { user.id : user for user in users }

def authenticate( username, password ):
    print( "Inside Authentication" )
    userdetail = username_mapping.get( username, None )
    print( f"userdetail.password = { userdetail.password }, password = { password } and userdetail.password == password = { userdetail.password == password }" )

    if(userdetail != None ):
        if( userdetail.password == password ):
            return userdetail
        else:
            return { "Message" : "Wrong Password, Try Again" }
    else:
        return { "Message" : "User doesn't exist" }

def identity( payload ):
    print( "Inside Identity Function" )
    user_id = payload['indentity']
    return userid_mapping.get( user_id, None )