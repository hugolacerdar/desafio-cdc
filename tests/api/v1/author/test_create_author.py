import httpx
from pydantic import ValidationError

from src.api.v1.authors.create_author_response import CreateAuthorResponse


def test_anonymous_user_creating_author():
    response = httpx.post('http://localhost:8000/api/v1/authors')

    assert response.status_code == 200
    assert response.headers['content-type'] == 'application/json'

    try:
        author = CreateAuthorResponse.model_validate(response.json())
    except ValidationError as e:
        raise AssertionError(f'Response validation failed: {e}') from e

    assert isinstance(author.id, UUID)
    assert isinstance(author.created_at, datetime)