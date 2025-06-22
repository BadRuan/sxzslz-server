from fastapi import APIRouter, HTTPException
from src.schemas.response import SuccessResponse
from src.exceptions.api_exception import NotFoundException, ValidationError
from src.model import Pagination, QueryCondition
from src.service.service import Service
from src.service.user_service import UserService
from src.service.subset_service import SubsetService
from src.service.article_service import ArticleService


api_router = APIRouter(tags=["apis"])


def handle_out_of_range_num(num: int) -> HTTPException:
    if num <= 0:
        raise ValidationError(
            status_code=400,
            message="请求参数异常",
            detail="参数为负。",
        )


def handle_pagination_request(
    service: Service, page: int, limit: int
) -> SuccessResponse:
    handle_out_of_range_num(page)
    handle_out_of_range_num(limit)
    try:
        totalPages: int = service.get_pages(limit)
        if page > totalPages:
            page = totalPages
        count: int = service.get_counts()
        return SuccessResponse(
            data=service.query_by_page(
                QueryCondition(page=page, limit=limit, onther=None)
            ),
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
        raise NotFoundException(detail=e.json())


def handle_query_one_request(service, id: int) -> SuccessResponse:
    handle_out_of_range_num(id)
    try:
        query_result = service.query_one(id)
        if None == query_result:
            raise NotFoundException(status_code=404, detail=f"查找的id:{id} 数据不存在")
        else:
            return SuccessResponse(data=query_result, meta={"info": "success"})
    except NotFoundException as e:
        raise NotFoundException(detail=e.json())


@api_router.get("/user", response_model=SuccessResponse, status_code=200)
async def user(page: int = 1, limit: int = 15):
    return handle_pagination_request(UserService(), page, limit)


@api_router.get("/subset", response_model=SuccessResponse, status_code=200)
async def subset(page: int = 1, limit: int = 15):
    return handle_pagination_request(SubsetService(), page, limit)


@api_router.get("/article", response_model=SuccessResponse, status_code=200)
async def article(page: int = 1, limit: int = 15):
    return handle_pagination_request(ArticleService(), page, limit)


@api_router.get("/user/{user_id}", response_model=SuccessResponse, status_code=200)
async def user_item(user_id: int):
    return handle_query_one_request(UserService(), user_id)


@api_router.get("/subset/{subset_id}", response_model=SuccessResponse, status_code=200)
async def subset_item(subset_id: int):
    return handle_query_one_request(SubsetService(), subset_id)


@api_router.get(
    "/article/{article_id}", response_model=SuccessResponse, status_code=200
)
async def article_item(article_id: int):
    return handle_query_one_request(ArticleService(), article_id)
