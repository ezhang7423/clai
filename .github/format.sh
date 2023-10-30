#!/bin/bash
set -euxo pipefail

poetry run isort ezclai/ tests/
poetry run black ezclai/ tests/
