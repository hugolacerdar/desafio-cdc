import pytest_asyncio
from orchestrator import clean_database, wait_for_web_server


@pytest_asyncio.fixture(autouse=True)  # type: ignore
async def setup_services():
	"""Async fixture to ensure all services are ready before tests run."""
	await wait_for_web_server()
	await clean_database()
	yield
	# Optional teardown if necessary
	await clean_database()
