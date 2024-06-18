
.PHONY: test
test:
	python3 -m unittest discover -s . -p "*_test.py" -v

.PHONY: freeze
freeze:
	python3 -m pip freeze > requirements.txt 

.PHONY: install
install:
	python3 -m pip install -r requirements.txt

.PHONY: lint
lint:
	ruff check

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf coverage.xml
	rm -rf htmlcov
	rm -rf .pytest