
import json
try:
    import psycopg2
except Exception as e:
    print('please install psycopg2')
    sys.exit()

with open('config.json') as f:
    config=json.load(f)
database_name,user,password,host,port=config['database'],config['user'],config['password'],config['host'],config['port']

def connect_database():
    try:
        conn = psycopg2.connect(database=database_name, user=user,password=password, host=host, port=port)
        return conn
    except Exception as e:
        if str(e).find("does not exist")!=-1:
            print(database_name+"does not exist,please run 'python initializer.py initializer'")
        else:
            raise e

def create_databases():
    
connect_database()
