.DEFAULT_GOAL := help

## GENERAL ##
export IMAGE_TF = lacafeta-tf:1.0
## Target Commons ##

build: ## build image to dev: make build
	docker build -t $(IMAGE_TF) .

run: ## build image to raml: make build-raml
	docker run --rm -v $(PWD)/app:/notebooks $(IMAGE_TF) python demo.py

ssh: ## build image to raml: make build-raml
	docker run -it -v $(PWD)/app:/notebooks $(IMAGE_TF) bash

open: ## build image to raml: make build-raml
	docker run -it -p 8888:8888 -v $(PWD)/app:/notebooks $(IMAGE_TF)

## Target Help ##

help:
	@printf "\033[31m%-16s %-59s %s\033[0m\n" "Target" "Help" "Usage"; \
	printf "\033[31m%-16s %-59s %s\033[0m\n" "------" "----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-16s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'
