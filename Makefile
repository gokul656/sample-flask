run:
	flask --app auth_service run --debug

run-no-thread:
	flask --app auth_service run --debug --without-threads

venv:
	python -m venv .venv
	chmod +x .venv/bin/*
	source .venv/bin/activate