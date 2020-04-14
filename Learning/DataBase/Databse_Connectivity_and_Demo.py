import sqlite3

conn = sqlite3.connect( "database.db" )
cursor = conn.cursor()

#Drop Command
drop_table_query = """DROP TABLE USER_TABLE"""
cursor.execute( drop_table_query )

#Table Creation
create_table_query = """CREATE TABLE USER_TABLE( id int
                                        , username text
                                        , password text)"""
cursor.execute( create_table_query )


#Insert Command
insert_table_query = """INSERT INTO USER_TABLE VALUES ( ?, ?, ? )"""
user = ( 1, 'Gautam', 'G1' )
cursor.execute( insert_table_query, user )

users = [ (2, 'Mamta', 'M1')
        , (3, 'Jaya', 'J1')
        , (4, 'Nitu', 'N1') ]

cursor.executemany( insert_table_query, users )


#Select Command
select_table_query = "SELECT * FROM USER_TABLE"
select_table_query_output = cursor.execute( select_table_query )

for row in select_table_query_output:
    print( row )


#Delete Command
deletable_id = 1
delete_table_query = f"""DELETE FROM USER_TABLE WHERE id = { deletable_id }"""

cursor.execute( delete_table_query )
print()

select_table_query = "SELECT * FROM USER_TABLE"
select_table_query_output = cursor.execute( select_table_query )

for row in select_table_query_output:
    print( row )


#To Commit
conn.commit()

#To close
conn.close()