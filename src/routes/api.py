from fastapi import APIRouter, HTTPException
from src.schemas.response import SuccessResponse
from src.exceptions.api_exception import NotFoundException
from src.service.interface_service import Service
from src.service.user_service import UserService
from src.service.subset_service import SubsetService
from src.service.article_service import ArticleService


api_router = APIRouter(tags=["apis"])
page_size: int = 10


@api_router.get("/user", response_model=SuccessResponse, status_code=200)
async def user():
    try:
        service: Service = UserService()
        return SuccessResponse(
            data=service.query_all(),
            meta={
                "info": "success",
                "count": service.count(),
                "pages": service.pages(page_size),
                "page_size": page_size,
            },
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get("/user/{user_id}", response_model=SuccessResponse, status_code=200)
async def user_item(user_id: int):
    try:
        service: Service = UserService()
        return SuccessResponse(
            data=service.query_one(user_id), meta={"info": "success"}
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get("/subset", response_model=SuccessResponse, status_code=200)
async def subset():
    try:
        service: Service = SubsetService()
        return SuccessResponse(
            data=service.query_all(),
            meta={
                "info": "success",
                "count": service.count(),
                "pages": service.pages(page_size),
                "page_size": page_size,
            },
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get("/subset/{subset_id}", response_model=SuccessResponse, status_code=200)
async def subset_item(subset_id: int):
    try:
        service: Service = SubsetService()
        return SuccessResponse(
            data=service.query_one(subset_id), meta={"info": "success"}
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get("/article", response_model=SuccessResponse, status_code=200)
async def article():
    try:
        service: Service = ArticleService()
        return SuccessResponse(
            data=service.query_all(),
            meta={
                "info": "success",
                "count": service.count(),
                "pages": service.pages(page_size),
                "page_size": page_size,
            },
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get(
    "/article/{article_id}", response_model=SuccessResponse, status_code=200
)
async def subset_item(article_id: int):
    try:
        service: Service = ArticleService()
        return SuccessResponse(
            data=service.query_one(article_id), meta={"info": "success"}
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())
