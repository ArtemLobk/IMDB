from db import db
from sqlalchemy import Column, String, Integer


# Column accounts for users
class Users(db.Model):
    
    tablename = "users"   

    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column('login', String(25), nullable=False)
    last_name = Column('last_name', String(25), nullable=False)
    

    email = Column("email", String(25), nullable=False)
    password = Column("password", String, nullable=False)