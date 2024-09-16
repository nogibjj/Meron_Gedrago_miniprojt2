install:
	pip install --upgrade pip && pip install -r requirements.txt

test: 
	python -m pytest -cov=main test_MG_main.py

format:
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

generate_and_push: 
	python MG_main.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git add . MG_main_output.md
	git commit --force
	git push origin main --force

all: install format lint test generate_and_push
