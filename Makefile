install:
	pip install --upgrade pip && pip install -r requirements.txt

test: 
	python -m pytest -cov=main test_MG_main.py

format:
	black *.py

lint:
	ruff check test_*.py && ruff check *.py
	nbqa ruff *.ipynb

all: install format lint test
