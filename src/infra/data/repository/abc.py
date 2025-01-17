from abc import ABC, abstractmethod

from src.domain.models.system_status import DatabaseStatus


class Repository(ABC):
	@abstractmethod
	async def get_database_status(self) -> DatabaseStatus:
		"""
		Returns database status information, such as version and connection stats.
		"""
		pass
