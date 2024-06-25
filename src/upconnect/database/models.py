
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base() # declaramos la base de datos para que sqlalchemy pueda trabajar con ella

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    fecha_registro = Column(DateTime, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.role_id')) # Relacion entre las tablas users y roles por medio de la columna role_id

    roles = relationship('Roles', uselist = True, back_populates='users') # Relacion entre las tablas users y roles por medio de la columna

    def __repr__(self):
        return f'''<user_id=(user_id = {self.user_id}
                , email = {self.email}
                , password = {self.password}
                , fecha_registro = {self.fecha_registro})>''' # Representacion de la clase

class Roles(Base):
    __tablename__ = 'roles'
    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(50), nullable=False)

    users = relationship('Users', uselist = True, back_populates='roles') # Relacion entre las tablas users y roles por medio de la columna role_id

    def __repr__(self):
        return f'''<role_id=(role_id = {self.role_id}
                , role_name = {self.role_name})>'''