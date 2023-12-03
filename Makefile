PWD = $(shell pwd)

check:
	flake8
	ruff check -q .
	black --check .
	pytest -q


clean:
	rm -rf $(PWD)/build $(PWD)/dist $(PWD)/mvt.egg-info

dist:
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload dist/*

test-upload:
	python3 -m twine upload --repository testpypi dist/*

pylint:
	pylint --rcfile=setup.cfg mvt
