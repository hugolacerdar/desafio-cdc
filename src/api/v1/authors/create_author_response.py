from pydantic import BaseModel

from datetime import datetime
from uuid import UUID


class CreateAuthorResponse(BaseModel):
    id: UUID
    created_at: datetime
