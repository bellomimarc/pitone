
.PHONY: test
test:
	python3 -m unittest discover -s . -p "*_test.py" -v