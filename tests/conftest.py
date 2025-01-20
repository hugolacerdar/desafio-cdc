import pytest
import pytest_asyncio
from orchestrator import reset_database, wait_for_web_server

from src.environment import settings
from src.infra.data.database.pg_database import PostgresDatabase


@pytest_asyncio.fixture(autouse=True)  # type: ignore
async def setup_services():
	"""Async fixture to ensure all services are ready before tests run."""
	await wait_for_web_server()
	await reset_database()


@pytest.fixture
def db() -> PostgresDatabase:
	"""Async fixture to provide a database connection."""
	return PostgresDatabase(
		user=settings.db_user,
		password=settings.db_password,
		host=settings.db_host,
		port=settings.db_port,
		database=settings.db_name,
	)
