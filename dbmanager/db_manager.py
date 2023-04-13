import sqlite3

def create_connection(db_file: str):
    sql_connection = None

    try:
        sql_connection = sqlite3.connect(db_file)
        return sql_connection

    except sqlite3.Error as error:
        print(f"Greška kod kreiranja baze - {error}")
        return sql_connection
    
def create_table(sql_connection: sqlite3.Connection, create_table_sql: str):
    try:
        cursor = sql_connection.cursor()
        cursor.execute(create_table_sql)
        sql_connection.commit()
        cursor.close()
        return True
    
    except sqlite3.Error as error:
        print(f"Greška kod kreiranja tablice - {error}")
        return False
    
def insert_into_table(
    sql_connection: sqlite3.Connection, 
    insert_sql: str,
    data: list
):
    try:
        cursor = sql_connection.cursor()
        for item in data:
            cursor.execute(insert_sql, (item,))
        sql_connection.commit()
        cursor.close()
        return True
    
    except sqlite3.Error as error:
        print(f"Greška kod umetanja u tablicu - {error}")
        return False

def check_if_value_exists(
    sql_connection: sqlite3.Connection, 
    search_sql: str,
    data: list
):
    try:
        cursor = sql_connection.cursor()
        for item in data:
            cursor.execute(search_sql, item)
        result = cursor.fetchone()
        cursor.close()
        if result:
            return True
        else:
            return False
    
    except sqlite3.Error as error:
        print(f"Greška kod pretrazivanja tablice - {error}")
        return False

def delete_table(sql_connection: sqlite3.Connection, delete_table_sql: str):
    try:
        cursor = sql_connection.cursor()
        cursor.execute(delete_table_sql)
        sql_connection.commit()
        cursor.close()
        return True
    
    except sqlite3.Error as error:
        print(f"Greška kod brisanja tablice - {error}")
        return False
    
def select_from_table(sql_connection: sqlite3.Connection, select_table_sql: str):
    try:
        cursor = sql_connection.cursor()
        cursor.execute(select_table_sql)
        result = cursor.fetchone()
        sql_connection.commit()
        cursor.close()
        return result
    
    except sqlite3.Error as error:
        print(f"Greška kod dohvaćanja tablice - {error}")
        return False