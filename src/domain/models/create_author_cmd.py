# type: ignore

from pydantic import BaseModel, EmailStr, Field, constr


class CreateAuthorCmd(BaseModel):
	name: constr(strip_whitespace=True, max_length=255, min_length=1) = Field(
		default=..., description='Name must be non-empty and less than or equal to 255 characters'
	)
	email: EmailStr = Field(default=..., description='Must be a valid email address')
	description: constr(strip_whitespace=True, max_length=400, min_length=1) = Field(
		default=..., description='Description must be non-empty and less than or equal to 400 characters'
	)
