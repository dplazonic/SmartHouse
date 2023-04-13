from dbmanager.db_manager import *

def save_data(name, data):

    name = name.lower()
    
    db_file = f"{name}.db"

    delete_table_sql = f"DROP TABLE IF EXISTS {name}"
    sql_connection = create_connection(db_file)
    success = delete_table(sql_connection, delete_table_sql)

    create_table_sql = f"CREATE TABLE IF NOT EXISTS {name} (id INTEGER PRIMARY KEY, value INTEGER NOT NULL);"

    insert_into_table_sql = f"INSERT INTO {name} (value) VALUES (?);"
    
    sql_connection = create_connection(db_file)
    success = create_table(sql_connection, create_table_sql)
        
    if success:
        print("Uspjesno smo napravili tablicu")
    else:
        print("Nismo napravili tablicu")

    data_to_insert = (data,)

    success = insert_into_table(sql_connection, insert_into_table_sql, data_to_insert)
    if success:
        print("Uspjesno smo dodali podatke u tablicu")
    else:
        print("Nismo dodali podatke u tablicu")

    sql_connection.close()

def get_data(name):
     
    name = name.lower()
    db_file = f"{name}.db"
    sql_connection = create_connection(db_file)

    select_data = f"SELECT value FROM {name}"
    
    value = select_from_table(sql_connection, select_data)

    return value

