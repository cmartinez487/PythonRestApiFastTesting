from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.dbConnection import meta, engine

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(25)),
    Column("email", String(255)),
    Column("password", String(255)),    
)

meta.create_all(engine)
