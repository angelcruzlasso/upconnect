from sqlalchemy import create_engine

'''
    Documentacion de sqlalchemy...
    #! Engine
    #? https://docs.sqlalchemy.org/en/14/tutorial/engine.html#tutorial-engine
'''

db_path = "/home/angel/Documents/databaseupconnect"
engine = create_engine(f"sqlite:///{db_path}", echo=True)     



