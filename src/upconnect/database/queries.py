from dbconfig import engine
from models import Users
from sqlalchemy.orm import sessionmaker
from datetime import datetime

'''
    Documentacion de sqlalchemy...
    #! sessionmaker
    #? https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.sessionmaker

    #! Session
    #? https://docs.sqlalchemy.org/en/14/orm/session_basics.html#id1
'''

Session = sessionmaker(bind=engine) 
session = Session()

def insertar_usuario(email, password, role_id):
    with Session() as session:
        try:
            fecha_registro = datetime.now()
            nuevo_usuario = Users(
                email=email,
                password=password,
                fecha_registro=fecha_registro,
                role_id=role_id
            )
            session.add(nuevo_usuario)
            session.commit()
            print("Usuario insertado correctamente.")
        except Exception as e:
            session.rollback()
            print(e)

# Llamada de ejemplo a la función para insertar un usuario
# insertar_usuario('angel.cruz02@up.ac.pa', '1234', 1)

def prueba():
    with Session() as session:
        try: 
            consulta = session.query(Users).all()
            for i in consulta:
                print(i)
        except Exception as e:
            print(e)
prueba()
