from fastapi import APIRouter, HTTPException
from src.schemas.response import SuccessResponse
from src.exceptions.api_exception import NotFoundException
from src.model import Pagination
from src.service.interface_service import Service
from src.service.user_service import UserService
from src.service.subset_service import SubsetService
from src.service.article_service import ArticleService


api_router = APIRouter(tags=["apis"])


def handle_out_of_range_num(num: int) -> HTTPException:
    if num <= 0:
        raise HTTPException(
            status_code=416,
            detail=f"参数异常。",
        )


@api_router.get("/user", response_model=SuccessResponse, status_code=200)
async def user(page: int = 1, limit: int = 15):
    handle_out_of_range_num(page)
    handle_out_of_range_num(limit)
    try:
        service: Service = UserService()
        totalPages: int = service.pages(limit)
        if page > totalPages:
            page = totalPages
        count: int = service.count()
        return SuccessResponse(
            data=service.query_by_page(page, limit),
            meta={
                "info": "success",
                "pagination": Pagination(
                    total_count=count,
                    total_pages=totalPages,
                    current_page=page,
                    limit_count=limit,
                ),
            },
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get("/user/{user_id}", response_model=SuccessResponse, status_code=200)
async def user_item(user_id: int):
    handle_out_of_range_num(user_id)
    try:
        service: Service = UserService()
        query_result = service.query_one(user_id)
        if None == query_result:
            raise HTTPException(
                status_code=404, detail=f"查找的user_id:{user_id} 数据不存在"
            )
        else:
            return SuccessResponse(
                data=service.query_one(user_id), meta={"info": "success"}
            )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get("/subset", response_model=SuccessResponse, status_code=200)
async def subset(page: int = 1, limit: int = 15):
    handle_out_of_range_num(page)
    handle_out_of_range_num(limit)
    try:
        service: Service = SubsetService()
        totalPages: int = service.pages(limit)
        if page > totalPages:
            page = totalPages
        count: int = service.count()
        return SuccessResponse(
            data=service.query_by_page(page, limit),
            meta={
                "info": "success",
                "pagination": Pagination(
                    total_count=count,
                    total_pages=totalPages,
                    current_page=page,
                    limit_count=limit,
                ),
            },
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get("/subset/{subset_id}", response_model=SuccessResponse, status_code=200)
async def subset_item(subset_id: int):
    handle_out_of_range_num(subset_id)
    try:
        service: Service = SubsetService()
        query_result = service.query_one(subset_id)
        if None == query_result:
            raise HTTPException(status_code=404, detail="查找的数据不存在")
        else:
            return SuccessResponse(data=query_result, meta={"info": "success"})

    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get("/article", response_model=SuccessResponse, status_code=200)
async def article(page: int = 1, limit: int = 15):
    handle_out_of_range_num(page)
    handle_out_of_range_num(limit)
    try:
        service: Service = ArticleService()
        totalPages: int = service.pages(limit)
        if page > totalPages:
            page = totalPages
        count: int = service.count()
        return SuccessResponse(
            data=service.query_by_page(page, limit),
            meta={
                "info": "success",
                "pagination": Pagination(
                    total_count=count,
                    total_pages=totalPages,
                    current_page=page,
                    limit_count=limit,
                ),
            },
        )
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())


@api_router.get(
    "/article/{article_id}", response_model=SuccessResponse, status_code=200
)
async def subset_item(article_id: int):
    handle_out_of_range_num(article_id)
    try:
        service: Service = SubsetService()
        query_result = service.query_one(article_id)
        if None == query_result:
            raise HTTPException(status_code=404, detail="查找的数据不存在")
        else:
            return SuccessResponse(data=query_result, meta={"info": "success"})
    except NotFoundException as e:
        raise HTTPException(status_code=404, detail=e.json())
