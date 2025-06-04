from enum import Enum, unique
from pydantic import BaseModel
from datetime import datetime


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
    create_time: datetime


@unique
class SubsetType(Enum):
    Article = 0  # 文章
    Photo = 1  # 图片
    File = 2  # 文件


class SubsetModel(BaseModel):
    subset_id: int
    subset_name: str
    subset_type: SubsetType
    create_time: datetime


class ArticleModel(BaseModel):
    article_id: int
    user_id: int
    subset_id: int
    title: str
    content: str
    state: bool
    create_time: datetime
    read_count: int
