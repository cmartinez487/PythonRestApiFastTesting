from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str]
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True  # Allows compatibility with ORM models
        allow_population_by_field_name = True  # Allows population by field names