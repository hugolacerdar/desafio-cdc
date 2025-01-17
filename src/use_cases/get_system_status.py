from datetime import datetime

from src.domain.models.system_status import DatabaseStatus, Dependencies, SystemStatus
from src.infra.data.repository.abc import Repository


class GetSystemStatus:
	def __init__(self, repository: Repository) -> None:
		self.repository = repository

	async def execute(self) -> SystemStatus:
		database_status: DatabaseStatus = await self.repository.get_database_status()
		updated_at: datetime = datetime.now()
		system_status = SystemStatus(updated_at=updated_at, dependencies=Dependencies(database=database_status))

		return system_status
