from fastapi import APIRouter

from src.api.v1.status import router as status_router

router = APIRouter(
	prefix='/v1',
)

router.include_router(status_router)
