from pydantic import BaseModel


class DatabaseConfig(BaseModel):
    url: str
    port: int
    user: str
    password: str
    database: str


class UserModel(BaseModel):
    user_id: int
    user_name: str
    nick_name: str
    password: str
    avatar_src: str
    create_time: str
