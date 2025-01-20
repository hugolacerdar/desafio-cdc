from fastapi import Depends

from src.api.dependencies import resolve_create_author_use_case
from src.api.v1.authors.create_author_response import CreateAuthorResponse
from src.domain.models.author import Author
from src.domain.models.create_author_cmd import CreateAuthorCmd
from src.use_cases.create_author import CreateAuthor

from . import router


@router.post(
	'',
	response_model=CreateAuthorResponse,
)
async def create_author(
	cmd: CreateAuthorCmd, create_author_use_case: CreateAuthor = Depends(resolve_create_author_use_case)
) -> CreateAuthorResponse:
	author: Author = await create_author_use_case.execute(cmd)

	return CreateAuthorResponse(
		id=author.id,
		created_at=author.created_at,
	)
