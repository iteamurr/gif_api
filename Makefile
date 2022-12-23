APPLICATION_NAME = gif_api


.PHONY: run
run: # Run the service.
		poetry run python -m $(APPLICATION_NAME) $(ARGS)

.PHONY: test
test: # Run project tests.
		pytest --cov-report term-missing --cov=$(APPLICATION_NAME) -v tests/

.PHONY: up
up: # Create and launch service containers.
		docker compose up -d

.PHONY: psql
psql: # Log in to the service database.
		docker compose exec db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

.PHONY: revision
revision: # Create a file with migrations.
		cd $(APPLICATION_NAME)/db/ && poetry run alembic revision --autogenerate

.PHONY: migrate
migrate: # Apply the latest migrations.
		cd $(APPLICATION_NAME)/db/ && poetry run alembic upgrade head

.PHONY: clean
clean: # Clear the directory of unnecessary files.
		poetry run pyclean -v $(APPLICATION_NAME)/ tests/

.PHONY: nice
nice: # Format the code.
		isort $(APPLICATION_NAME)/ tests/ && black $(APPLICATION_NAME)/ tests/

.PHONY: help
help: # Show help for each of the Makefile recipes.
		@grep -E '^[a-zA-Z0-9 -]+:.*#' Makefile | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done