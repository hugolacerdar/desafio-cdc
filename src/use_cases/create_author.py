from src.domain.models.author import Author
from src.domain.models.create_author_cmd import CreateAuthorCmd
from src.infra.data.repository.abc import Repository


class CreateAuthor:
	def __init__(self, repository: Repository) -> None:
		self.repository = repository

	async def execute(self, cmd: CreateAuthorCmd) -> Author:
		author: Author = Author(name=cmd.name, email=cmd.email, description=cmd.description)  # type: ignore

		persisted_author: Author = await self.repository.create_author(author)

		return persisted_author
