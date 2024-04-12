install:
	poetry install

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build:
	poetry build

.PHONY: install test lint selfcheck check build

package-install:
	python3 -m pip install --force-reinstall dist/*.whl
