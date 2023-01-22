install:
	poetry install

test:
	poetry run black --check .
	poetry run pytest --cov 'rshanker779_common' --cov-fail-under 95

format:
	poetry run black .

doc:
	poetry install --with docs
	poetry run sphinx-apidoc -f -o docsrc/source src/rshanker779_common
	make -C docsrc github

clean:
	rm -rf build
	rm -rf dist
	rm -rf rshanker779_common.egg-info
	find . -name *.pyc -delete
	find . -name __pycache__ -delete

coverage:
	coverage erase
	pytest --cov 'rshanker779_common'
	coverage html

version:
	bump2version --config-file .bumpversion.cfg $(BUMP)

all: install format coverage

