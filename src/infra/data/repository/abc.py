from abc import ABC, abstractmethod

from src.domain.models.author import Author
from src.domain.models.system_status import DatabaseStatus


class Repository(ABC):
	@abstractmethod
	async def get_database_status(self) -> DatabaseStatus:
		"""
		Returns database status information, such as version and connection stats.
		"""
		pass

	@abstractmethod
	async def create_author(self, author: Author) -> Author:
		"""
		Creates a new author in the database.
		"""
		pass
