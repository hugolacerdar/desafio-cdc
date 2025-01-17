from abc import ABC, abstractmethod
from typing import Any


class Database(ABC):
	@abstractmethod
	async def get_pool(self) -> Any:  # noqa: ANN401
		"""
		Returns the database connection or pool.
		"""
		pass
