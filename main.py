import sys
from pymongo import MongoClient

def get_agent():
    conn=MongoClient('127.0.0.1',27017)
    db=conn.user_agent
    result=[i for i in db.col.find()]
    print(result)



__author__='thouger'
if __name__ == '__main__':
    if(len(sys.argv)==1):
        print("input 'python main.py initializer' to initializer")
        print("input 'python mian.py main' to run")
    else:
        command=sys.argv[1]
        if(command=='initializer'):
            initializer()
        if(command=='get'):
            get_agent()
