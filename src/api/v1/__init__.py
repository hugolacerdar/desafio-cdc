from fastapi import APIRouter

from src.api.v1.authors import router as authors_router
from src.api.v1.status import router as status_router

router: APIRouter = APIRouter(
	prefix='/v1',
)

router.include_router(status_router)
router.include_router(authors_router)
