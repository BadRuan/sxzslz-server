from pydantic import BaseModel
from datetime import datetime
from typing import Tuple


class DatabaseConfig(BaseModel):
    url: str
    port: int
    user: str
    password: str
    database: str


class QueryCondition(BaseModel):
    page: int
    limit: int
    onther: Tuple | None


class User(BaseModel):
    user_id: int
    user_name: str
    nick_name: str
    password: str
    avatar_src: str
    create_time: datetime


class Subset(BaseModel):
    subset_id: int
    subset_name: str
    create_time: datetime


class Article(BaseModel):
    article_id: int
    user_id: int
    subset_id: int
    user_name: str | None
    subset_name: str | None
    title: str
    content: str | None
    state: bool
    create_time: datetime
    read_count: int


class Pagination(BaseModel):
    total_count: int
    total_pages: int
    current_page: int
    limit_count: int
