import asyncpg  # type: ignore
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed

from src.environment import settings


@retry(stop=stop_after_attempt(100), wait=wait_fixed(1))
async def wait_for_web_server():
	"""Wait for the web server to be ready by checking the status endpoint."""
	async with httpx.AsyncClient() as client:
		response = await client.get('http://localhost:8000/api/v1/status')
		if response.status_code != 200:
			raise Exception('Status page not ready')


async def clean_database():
	"""Reset the test database by dropping and recreating the public schema."""
	conn = await asyncpg.connect(  # type: ignore
		database=settings.db_name,
		user=settings.db_user,
		password=settings.db_password,
		host=settings.db_host,
		port=settings.db_port,
	)
	try:
		await conn.execute('DROP SCHEMA public CASCADE; CREATE SCHEMA public;')  # type: ignore
	finally:
		await conn.close()  # type: ignore
