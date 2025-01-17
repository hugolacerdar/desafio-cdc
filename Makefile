dev:
	poetry run python scripts/manage_dev_env.py

services-up:
	docker compose -f src/infra/compose.yaml up -d
	
services-stop:
	docker compose -f src/infra/compose.yaml stop

services-wait-db:
	python scripts/wait_for_postgres.py
	
test: services-up
	npx concurrently -n fastapi,pytest --hide fastapi -k -s command-pytest "poetry run python main.py" "poetry run pytest --verbose"

lint-ruff-check: 
	poetry run ruff check

lint-ruff-fix: 
	poetry run ruff check --fix

format-ruff-check: 
	poetry run ruff format --check
	
format-ruff-fix:
	poetry run ruff format

sec-detect-secrets-hook:
	git diff --staged --name-only -z | xargs -0 poetry run detect-secrets-hook --baseline .secrets.baseline

sec-detect-secrets-scan:
	poetry run detect-secrets scan > .secrets.baseline

sec-detect-secrets-audit:
	poetry run detect-secrets audit .secrets.baseline

sec-detect-secrets-worflow: sec-detect-secrets-scan
	make sec-detect-secrets-audit

typecheck-pyright:
	poetry run pyright

commit:
	cz commit


