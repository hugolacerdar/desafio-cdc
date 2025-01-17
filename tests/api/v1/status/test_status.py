from datetime import datetime

import httpx
from pydantic import ValidationError

from src.api.v1.status.status_response import StatusResponse


def test_anonymous_user_retrieving_status():
	response = httpx.get('http://localhost:8000/api/v1/status')

	assert response.status_code == 200
	assert response.headers['content-type'] == 'application/json'

	try:
		status = StatusResponse.model_validate(response.json())
	except ValidationError as e:
		raise AssertionError(f'Response validation failed: {e}') from e

	assert isinstance(status.updated_at, datetime)
	assert isinstance(status.dependencies.database.version, str)
	assert isinstance(status.dependencies.database.max_connections, int)
	assert isinstance(status.dependencies.database.active_connections, int)
