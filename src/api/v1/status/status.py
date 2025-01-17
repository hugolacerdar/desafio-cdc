from fastapi import Depends

from src.api.dependencies import resolve_get_system_status_use_case
from src.api.v1.status.status_response import DatabaseStatus, Dependencies, StatusResponse
from src.domain.models.system_status import SystemStatus
from src.use_cases.get_system_status import GetSystemStatus

from . import router


@router.get('', response_model=StatusResponse)
async def get_status(get_system_status_use_case: GetSystemStatus = Depends(resolve_get_system_status_use_case)) -> StatusResponse:
	status: SystemStatus = await get_system_status_use_case.execute()

	return StatusResponse(
		updated_at=status.updated_at, dependencies=Dependencies(database=DatabaseStatus(**status.dependencies.database.model_dump()))
	)
