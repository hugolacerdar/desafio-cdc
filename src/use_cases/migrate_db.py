# type: ignore

from yoyo import get_backend, read_migrations


class MigrateDB:
	def __init__(self, db_url: str, migrations_path: str) -> None:
		self.backend = get_backend(db_url)
		self.migrations = read_migrations(migrations_path)

	def execute(self) -> None:
		with self.backend.lock():
			self.backend.apply_migrations(self.migrations)
