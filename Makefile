run:
	flask --app auth_service run --debug

run-no-thread:
	flask --app auth_service run --debug --without-threads

