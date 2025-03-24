.PHONY: help run migration migrate migrate-rollback seed

# Alembic
ALEMBIC_CONFIG_FILE ?= app/database/migrations/alembic.ini


help:
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make COMMAND\033[36m\033[0m\n\n  A general utility script.\n\n  Provides commands to run the application, database migrations, tests, etc.\n  Next command start up the application:\n\n    \44 make run\n\nCommands:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-14s\033[0m \t%s\n", $$1, $$2 }' $(MAKEFILE_LIST)

# =============================
# ==== DATABASE COMMANDS ======
# =============================
migration:  ## Create a new migration based in new changes from database models
	docker compose exec app uv run alembic -c "${ALEMBIC_CONFIG_FILE}" revision --autogenerate -m '$(msg)'

migrate:  ## Upgrade to a later database migration
	docker compose exec app uv run alembic -c "${ALEMBIC_CONFIG_FILE}" upgrade head

migrate-rollback:  ## Revert to a previous database migration
	docker compose exec app uv run alembic -c "${ALEMBIC_CONFIG_FILE}" downgrade -1

seed:  ## Fill database with fake data
	docker compose exec app uv run python cli.py seed

# ==============================================
# ==== COVERAGE, LINTER AND TEST COMMANDS ======
# ==============================================
test: ## Run tests
	pytest
