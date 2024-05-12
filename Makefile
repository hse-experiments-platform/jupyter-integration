include .env

build:
	cd jupyterlab && docker build -t $(DOCKER_JUPYTER_IMAGE) -f Dockerfile .
	docker-compose -f docker-compose.yml build --no-cache
	docker-compose -f docker-compose.yml up --force-recreate