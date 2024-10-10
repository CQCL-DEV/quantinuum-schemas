SHELL:=bash
all:
	echo "No default recipe."

release:
	poetry build
	poetry publish -u __token__ -p $$QUANTINUUM_SCHEMAS_PYPI_TOKEN

format:
	poetry run black .
	poetry run isort --profile black --dont-follow-links .

check:
	poetry run pylint quantinuum_schemas tests
	poetry run mypy quantinuum_schemas tests