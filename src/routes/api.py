from fastapi import APIRouter, HTTPException
from src.schemas.response import SuccessResponse
from src.exceptions.api_exception import NotFoundException
from src.dao.interface_dao import Dao
from src.dao.user_dao import UserDao
from src.dao.subset_dao import SubsetDao


api_router = APIRouter(tags=["apis"])


@api_router.get("/users", response_model=SuccessResponse, status_code=200)
async def users():
    try:
        dao: Dao = UserDao()
        return SuccessResponse(data=dao.query_all(), meta={"info": "success"})
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get("/subsets", response_model=SuccessResponse, status_code=200)
async def subsets():
    try:
        dao: Dao = SubsetDao()
        return SuccessResponse(data=dao.query_all(), meta={"info": "success"})
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())
