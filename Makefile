install:
	python setup.py install

test:
	black --check .
	pytest --cov 'rshanker779_common' --cov-fail-under 70

extras:
	pip install .[snakeviz]

