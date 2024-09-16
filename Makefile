install:
	pip install --upgrade pip && pip install -r requirements.txt

test: 
	python -m pytest -cov=main test_MG_main.py

format:
	black *.py

lint:
	ruff check test_*.py && ruff check *.py

check: 
	python main.py 
	git config --local user.email "action@github.com"; \
	git config --local user.name "GitHub Action"; \
	git add . 
	git commit -m "test"
	git push 

all: install format lint test check
