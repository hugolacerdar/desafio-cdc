from datetime import datetime

from pydantic import BaseModel


class DatabaseStatus(BaseModel):
	version: str
	max_connections: int
	active_connections: int


class Dependencies(BaseModel):
	database: DatabaseStatus


class StatusResponse(BaseModel):
	updated_at: datetime
	dependencies: Dependencies
