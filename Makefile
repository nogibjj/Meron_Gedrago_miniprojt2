install:
	pip install --upgrade pip && pip install -r requirements.txt

test: 
	python -m pytest -cov=main test_MG_main.py

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

check: 
	python MG_main.py 
	git config --local user.email "action@github.com"; \
	git config --local user.name "GitHub Action"; \
	git add . 
	git commit -m "test"
	git push 

all: install format lint test check
