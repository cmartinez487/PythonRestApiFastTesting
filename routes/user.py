from fastapi import APIRouter
from config.dbConnection import conn
from models.Users import users
from schemas.user import User

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user:User):

    print(user)
    return {user.username, user.email, user.password}


@user.put("/users")
def hello_world():
    return {"message": "Hello, World!"}

@user.delete("/users")
def hello_world():
    return {"message": "Hello, World!"}