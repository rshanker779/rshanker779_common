install:
	python setup.py install

test:
	black --check .
	pytest --cov 'rshanker779_common' --cov-fail-under 95

extras:
	pip install .[snakeviz]

format:
	black .

docs:
	ls

coverage:
	coverage erase
	make test
	coverage html

all: install format coverage

