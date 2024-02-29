psql.up:
	docker run -d --name daily_drf \
		-p 5430:5432 \
		-e POSTGRES_PASSWORD=password \
		-e POSTGRES_USER=daily_drf \
		-e POSTGRES_DB=daily_drf \
		postgres:latest
