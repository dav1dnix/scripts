from sqlite3 import connect

# Database
def db(name):
    try:
        conn_obj = connect(name)
        return conn_obj
    except Error as e:
        print("There was an error connecting to database.\n", e)
