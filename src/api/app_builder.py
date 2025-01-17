from fastapi import FastAPI

from src.api import router as api_router


class AppBuilder:
	@staticmethod
	def build_app() -> FastAPI:
		app = FastAPI()

		app.include_router(api_router)

		return app
