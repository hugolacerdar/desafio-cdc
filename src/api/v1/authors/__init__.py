from fastapi import APIRouter

router: APIRouter = APIRouter(
	prefix='/authors',
	tags=['Authors'],
)

from . import create_author  # noqa: E402, F401 # type: ignore