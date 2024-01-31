SHELL:=bash
all:
	echo "No default recipe."

release:
	poetry build
	poetry publish -u __token__ -p ${QUANTINUUM_SCHEMAS_PYPI_TOKEN}