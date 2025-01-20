from asyncpg import Pool  # type: ignore

from src.domain.models.author import Author
from src.domain.models.system_status import DatabaseStatus
from src.infra.data.database.abc import Database
from src.infra.data.database.pg_database import PostgresDatabase
from src.infra.data.repository.abc import Repository


class PostgresRepository(Repository):
	def __init__(self, database: Database) -> None:
		if not isinstance(database, PostgresDatabase):
			raise ValueError(f'Invalid database type. Expected PostgresDatabase, got {type(database)}')

		self.database: PostgresDatabase = database

	async def get_database_status(self) -> DatabaseStatus:
		pool: Pool = await self.database.get_pool()
		async with pool.acquire() as conn:  # type: ignore
			version = await conn.fetchval('SELECT version();')  # type: ignore
			max_connections: int = await conn.fetchval('SHOW max_connections;')  # type: ignore
			active_connections: int = await conn.fetchval('SELECT COUNT(*)::int FROM pg_stat_activity WHERE datname = current_database();')  # type: ignore

		return DatabaseStatus(
			version=version,  # type: ignore
			max_connections=max_connections,  # type: ignore
			active_connections=active_connections,  # type: ignore
		)

	async def create_author(self, author: Author) -> Author:
		pool: Pool = await self.database.get_pool()  # type: ignore
		async with pool.acquire() as conn:  # type: ignore
			query = 'INSERT INTO author (id, name, email, description, created_at, updated_at) VALUES ($1, $2, $3, $4, $5, $6);'

			await conn.execute(  # type: ignore
				query, author.id, author.name, author.email, author.description, author.created_at, author.updated_at
			)

		return author
