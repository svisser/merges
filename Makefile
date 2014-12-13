SHELL := /bin/bash

init:
	python setup.py develop

publish:
	python setup.py sdist upload

test:
	nosetests --with-doctest

clean:
	git clean -Xfd
