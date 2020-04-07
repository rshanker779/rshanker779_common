install:
	python setup.py install

test:
	black --check .
	pytest --cov 'rshanker779_common' --cov-fail-under 95

extras:
	pip install .[snakeviz]

format:
	black .

doc:
	sphinx-apidoc -f -o docsrc/source rshanker779_common
	make -C docsrc github

clean:
	rm -rf build
	rm -rf dist
	rm -rf rshanker779_common.egg-info
	find . -name *.pyc -delete
	find . -name __pycache__ -delete

coverage:
	coverage erase
	make test
	coverage html

all: clean install format coverage

