from fastapi import APIRouter, Response
from config.dbConnection import conn
from models.Users import users
from schemas.user import User
from cryptography.fernet import Fernet
from config.configKey import fernet
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

user = APIRouter()

@user.get("/users")
def getUsers():
    result = conn.execute(users.select()).fetchall()

    users_list = [dict(row._mapping) for row in result]

    return users_list


@user.get("/users/{id}")
def getUserbyId(id: str):
        
        user = conn.execute(users.select().where(users.c.id == id)).first()
        if user:
            user = dict(user._mapping)
            
            # Convertir a bytes antes de desencriptar
            encrypted_password = user['password']
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode("utf-8")
            user['password'] = decrypted_password 
            
            return user
        else:
            return {"message": "User not found"}

@user.post("/users")
def createUser(user:User):
    
    newUser = {
         "username": user.username, 
         "email": user.email, 
         "password": fernet.encrypt(user.password.encode("utf-8"))
         }
    
    result = conn.execute(users.insert().values(newUser))
    
    user = conn.execute(users.select().where(users.c.id == result.lastrowid)).first()
    
    if user:
        user = dict(user._mapping)
        user['password'] = fernet.decrypt(user['password'].encode("utf-8")).decode("utf-8")
    
    conn.commit() 
    
    return {"message": "User created successfully", "user": user}


@user.put("/users/{id}")
def updateUser(user:User):
    conn.execute(users.update().where(users.c.id == user.id).values(
        username=user.username, 
        email=user.email, 
        password=fernet.encrypt(user.password.encode("utf-8"))
    ))

    return {"message": user}

@user.delete("/users/{id}")
def deleteUser(id: str):
    result = conn.execute(users.delete().where(users.c.id == id))
    conn.commit() 
    return {"message": "User deleted successfully", "status_code": HTTP_204_NO_CONTENT}