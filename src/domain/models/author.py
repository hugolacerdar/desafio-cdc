# type: ignore

import uuid
from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr, Field


class Author(BaseModel):
	id: UUID4 = Field(default_factory=uuid.uuid4)
	name: str
	email: EmailStr
	description: str
	created_at: datetime = datetime.now()
	updated_at: datetime | None = None
