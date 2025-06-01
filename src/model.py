from enum import Enum
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


class SubsetType(Enum):
    ARTICLE = 0  # 文章
    PHOTO = 1  # 图片
    FILE = 2  # 文件


class SubsetModel(BaseModel):
    subset_id: int
    subset_name: str
    subset_type: SubsetType
    create_time: str
