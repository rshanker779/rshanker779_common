install: clean
	python setup.py sdist bdist_wheel
	pip install dist/*.whl

test:
	black --check .
	pytest --cov 'rshanker779_common' --cov-fail-under 95

format:
	black .

doc:
	pip install .[docs]
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
	pytest --cov 'rshanker779_common'
	coverage html

version:
	bump2version --config-file .bumpversion.cfg $(BUMP)

all: install format coverage

