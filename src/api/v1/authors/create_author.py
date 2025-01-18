from src.domain.models.create_author_cmd import CreateAuthorCmd
from . import router 

@router.post(
    ''
)
async def create_author(
    cmd: CreateAuthorCmd
):
    pass