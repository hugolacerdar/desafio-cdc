from datetime import datetime
from uuid import UUID

import httpx
import pytest
from asyncpg.pool import Pool  # type: ignore
from pydantic import ValidationError

from src.api.v1.authors.create_author_response import CreateAuthorResponse
from src.infra.data.database.pg_database import PostgresDatabase


@pytest.mark.asyncio
async def test_anonymous_user_creating_author(db: PostgresDatabase) -> None:
	# Arrange: Set up test inputs and dependencies
	payload = {
		'name': 'John Doe',
		'email': 'email@example.com',
		'description': 'Description',
	}
	url = 'http://localhost:8000/api/v1/authors'
	pool: Pool = await db.get_pool()  # type: ignore

	# Act: Make the API call
	response = httpx.post(url, json=payload)

	# Assert: Validate the API response
	assert response.status_code == 200
	assert response.headers['content-type'] == 'application/json'

	try:
		create_author_response = CreateAuthorResponse.model_validate(response.json())
	except ValidationError as e:
		raise AssertionError(f'Response validation failed: {e}') from e

	assert isinstance(create_author_response.id, UUID)
	assert isinstance(create_author_response.created_at, datetime)

	# Assert: Verify the database entry
	async with pool.acquire() as conn:  # type: ignore
		author = await conn.fetchrow('SELECT * FROM author WHERE id = $1;', str(create_author_response.id))  # type: ignore

	assert author is not None, 'Author not found in database'
	assert author['name'] == payload['name']
	assert author['email'] == payload['email']
	assert author['description'] == payload['description']
	assert author['created_at'] == create_author_response.created_at
	assert author['updated_at'] is None
