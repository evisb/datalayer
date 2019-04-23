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

.PHONY: clean build push start connect stop rm

help: ## display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

default: all ## default target is all.

all: clean install build ## make clean install build.

clean: ## clean.

build: ## build the image.
	@exec docker build \
		-t datalayer/jupyterlab-datalayer:0.0.1 \
		.

push: ## push the image.
	@exec docker push \
	    datalayer/jupyterlab-datalayer:0.0.1

#		-e DLA_GITHUB_TOKEN=${DLA_GITHUB_TOKEN}
start: ## start the container.
	@exec docker run -it \
		-e DLA_TWITTER_CONSUMER_KEY=${DLA_TWITTER_CONSUMER_KEY} \
		-e DLA_TWITTER_CONSUMER_SECRET=${DLA_TWITTER_CONSUMER_SECRET} \
		-e DLA_TWITTER_OAUTH_CALLBACK_URL=${DLA_TWITTER_OAUTH_CALLBACK_URL} \
		--rm \
		-d \
		--name jupyterlab-datalayer \
		-p 8888:8888 \
		datalayer/jupyterlab-datalayer:0.0.1 \
		jupyter lab
	@exec sleep 1s
	make token
	make logs

connect: ## connect to the container.
	@exec docker exec -it jupyterlab-datalayer bash

token: ## get the notebook token(s).
	@exec docker exec -it jupyterlab-datalayer jupyter notebook list

logs: ## show container logs
	docker logs jupyterlab-datalayer -f

stop: ## stop the container.
	@exec docker stop jupyterlab-datalayer

rm: ## remove the container.
	@exec docker rm -f jupyterlab-datalayer
