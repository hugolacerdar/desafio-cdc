from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CreateAuthorResponse(BaseModel):
	id: UUID
	created_at: datetime
