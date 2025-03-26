install:
	uv pip install -r pyproject.toml

run-server:
	fastapi dev server/src/main.py

create-venv:
	uv venv

activate-venv:
	source .venv/bin/activate
	direnv allow