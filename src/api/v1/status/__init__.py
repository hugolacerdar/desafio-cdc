from fastapi import APIRouter

router = APIRouter(
	prefix='/status',
	tags=['System Status'],
)

from src.api.v1.status.status import get_status  # noqa: E402, F401 # type: ignore
