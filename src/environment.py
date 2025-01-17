import os

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	if os.environ.get('ENVIRONMENT') != 'production':
		load_dotenv('.env.development')

	db_user: str = Field(default=..., alias='DB_USER')
	db_password: str = Field(default=..., alias='DB_PASSWORD')
	db_host: str = Field(default=..., alias='DB_HOST')
	db_port: int = Field(default=..., alias='DB_PORT')
	db_name: str = Field(default=..., alias='DB_NAME')


settings = Settings()
