.DEFAULT_GOAL := help

## GENERAL ##
OWNER 			= utp
SERVICE_NAME 	= flash-ia
PATH_PREFIX 	= "/v1"
PROJECT_ID      = flash-utp-dev
ENV 			?= dev

## RESULT_VARS ##
PROJECT_NAME	= $(OWNER)-$(ENV)-$(SERVICE_NAME)
export CONTAINER_NAME 	= $(PROJECT_NAME)_backend
export IMAGE_DEV		= $(PROJECT_NAME):dev
## Target Commons ##

install: ## build image to dev: make build
	@make build
	wget https://storage.googleapis.com/flash-storage-pre/pepe/sys/model-ia/vgg16.npy
	mv vgg16.npy app/sdk/model

build: ## build image to dev: make build
	cp app/requirements.txt docker/dev/resources/requirements.txt
	docker build -f docker/dev/Dockerfile -t $(IMAGE_DEV) docker/dev/
	rm -f docker/dev/resources/requirements.txt

run: ## build image to raml: make build-raml
	docker run --rm -v $(PWD)/app:/notebooks $(IMAGE_TF) python demo.py

up: ## up docker containers: make up
	docker-compose up -d
	@make status
	open http://localhost:8787/v1/ia/image

start: ## up docker containers: make up
	make up

down: ## Stops and removes the docker containers: make down
	docker-compose down

status: ## Show containers status: make status
	docker-compose ps

stop: ## Stops and removes the docker containers, use me with: make down
	docker-compose stop

restart: ## Restart all containers, use me with: make restart
	make down
	make start
	make status

ssh: ## Connect to container for ssh protocol : make ssh
	docker exec -it $(CONTAINER_NAME) bash

set-config-local: ## copia el archivo config/env.local al config : make set-config-local
	cp app/config/config.env.local app/config/config.env
	mkdir -p app/files && chmod 777 app/files

log: ## Show container logs make : make log
	docker-compose logs -f

log-backend: ## Show container logs make : make log
	docker-compose logs -f backend

## Target Help ##

help:
	@printf "\033[31m%-16s %-59s %s\033[0m\n" "Target" "Help" "Usage"; \
	printf "\033[31m%-16s %-59s %s\033[0m\n" "------" "----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-16s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'
