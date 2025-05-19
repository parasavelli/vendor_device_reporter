# Makefile for vendor_device_reporter

PYTHON := python3

help:
	@echo "make install        - install all requirements"
	@echo "make run-report     - run CLI to generate hostnames.csv"
	@echo "make test           - run unit tests"
	@echo "make lint           - run linters (ruff, isort, black)"
	@echo "make check          - run pre-commit hooks"

install:
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install -r requirements-dev.txt

run-report:
	PYTHONPATH=. $(PYTHON) scripts/run_report.py --output hostnames.csv

test:
	pytest tests/ --cov=src --cov-report=term-missing

lint:
	ruff check src/ tests/ --fix
	isort src/ tests/ --check-only
	black src/ tests/ --check
	mypy src/

check:
	pre-commit run --all-files --show-diff-on-failure