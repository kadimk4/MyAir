DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
TESTS_FILE = docker_compose/tests.yaml
EXEC = docker exec -it
DB_CONTAINER = postgres
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app
MANAGE_PY = python manage.py


.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} down

.PHONY: postgres
postgres:
	${EXEC} ${DB_CONTAINER} psql

.PHONY: storages-logs
storages-logs:
	${LOGS} ${DB_CONTAINER} -f

.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} down

.PHONY: app-migrate
app-migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate

.PHONY: app-migrations
app-migrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: superuser
superuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: tests
tests:
	${DC} -f ${TESTS_FILE} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: tests-logs
tests-logs:
	${LOGS} tests -f

.PHONY: migrate
migrate:
	cd src && ${MANAGE_PY} migrate

.PHONY: migrations
migrations:
	cd src && ${MANAGE_PY} makemigrations