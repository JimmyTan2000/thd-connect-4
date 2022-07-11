prod: build-prod
	docker-compose run --rm connect-four

prod-tty: build-prod
	docker-compose run --rm -it connect-four bash

build-prod:
	docker-compose build