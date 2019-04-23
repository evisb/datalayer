#!make

# Licensed to Datalayer (https://datalayer.io) under one or more
# contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. Datalayer licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

.DEFAULT_GOAL=build

.PHONY: clean build push start connect stop rm volumes check-files pull build_image build

help: ## display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

default: all ## default target is all.

all: clean install build ## make clean install build.

clean: ## clean.

# network:
#	@docker network inspect $(DLA_DOCKER_NETWORK) >/dev/null 2>&1 || docker network create $(DLA_DOCKER_NETWORK)

volumes:
	@docker volume inspect $(DATA_VOLUME_HOST) >/dev/null 2>&1 || docker volume create --name $(DATA_VOLUME_HOST)
	@docker volume inspect $(DB_VOLUME_HOST) >/dev/null 2>&1 || docker volume create --name $(DB_VOLUME_HOST)

userlist:
	@echo "Add usernames, one per line, to ./userlist, such as:"
	@echo "    zoe admin"
	@echo "    wash"
	@exit 1

check-files: userlist

# build: check-files volumes pull
#	docker-compose -f jupyterhub.yml build
build:
	@exec docker build \
		-t datalayer/jupyterhub:0.0.1 \
		.

start:
	echo open http://localhost:8000
	@exec docker-compose -f jupyterhub.yml up -d

pull:
	@exec docker pull $(DLA_JUPYTERHUB_NOTEBOOK_IMAGE)

push:
	@exec docker push datalayer/jupyterhub:0.0.1

logs: ## show container logs
	@exec docker logs jupyterhub -f

connect: ## connect to the container.
	@exec docker exec -it jupyterhub bash

stop: ## stop the container.
#	@exec docker stop jupyterhub
	@exec docker-compose -f jupyterhub.yml down

rm: ## remove the container.
	@exec docker rm -f jupyterhub jupyterhub-db

start-nodocker:
	@exec jupyterhub -f jupyterhub_config.py

start-dev:
	@exec jupyterhub -f jupyterhub_config_dev.py
