#!/bin/bash
set -euxo pipefail

poetry run cruft check
poetry run mypy --ignore-missing-imports ezclai/ tests/
poetry run isort --check --diff ezclai/ tests/
poetry run black --check ezclai/ tests/
poetry run flake8 ezclai/ tests/ --darglint-ignore-regex '^test_.*'
poetry run bandit -r --severity medium high ezclai/ tests/
poetry run vulture --min-confidence 100 ezclai/ tests/
echo "Lint successful!"