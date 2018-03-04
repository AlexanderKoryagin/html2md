#!/usr/bin/env bash
set -x

# code checks
pylint converter.py converter/ tests/

# unit tests
pytest -vv tests/
