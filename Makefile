install:
	python setup.py install

test:
	black --check .
	pytest
