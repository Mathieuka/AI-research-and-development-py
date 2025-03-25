install:
	uv pip install -r pyproject.toml

run-server:
	fastapi dev server/src/main.py