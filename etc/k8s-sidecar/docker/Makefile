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

# `make kubectl` will build kubectl.
# `make tag` will suggest a tag.
# `make container` will build a container-- you must supply a tag.
# `make push` will push the container-- you must supply a tag.

.PHONY: clean build push start connect stop rm

GOARCH?=$(shell go env GOARCH)
GOOS?=$(shell go env GOOS)

kubectl:
	make -C ../../ WHAT=cmd/kubectl KUBE_STATIC_OVERRIDES="kubectl"; \
	cp ../../_output/local/bin/$(GOOS)/$(GOARCH)/kubectl .

.tag: 
	./dist/kubectl version --client | grep -o 'GitVersion:"[^"]*"' | sed 's/[^"]*"\([^"+]*\).*/\1/' > .tag

tag: .tag
	@echo "Suggest using TAG=$(shell cat .tag)"
	@echo "$$ make build TAG=$(shell cat .tag)"
	@echo "or"
	@echo "$$ make push TAG=$(shell cat .tag)"

build:
	$(if $(TAG),,$(error TAG is not defined. Use 'make tag' to see a suggestion))
	docker build --pull -t docker.io/datalayer/k8s-sidecar:$(TAG) .

push: build
	$(if $(TAG),,$(error TAG is not defined. Use 'make tag' to see a suggestion))
	docker push docker.io/datalayer/k8s-sidecar:$(TAG)

help: ## display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

default: all ## default target is all.

all: clean install build ## make clean install build.

clean: ## clean.

build: ## build the image.
	@exec docker build \
		-t datalayer/k8s-sidecar:0.0.1 \
		.

push: ## push the image.
	@exec docker push \
	    datalayer/k8s-sidecar:0.0.1

start: ## start the container.
	@exec docker run -it \
		--rm \
		-d \
		--name k8s-sidecar \
		-p 8989:8989 \
		datalayer/k8s-sidecar:0.0.1
	@exec sleep 1s
	@exec open http://localhost:8989/api/doc

connect: ## connect to the container.
	@exec docker exec -it k8s-sidecar bash

logs: ## show container logs
	docker logs k8s-sidecar -f

stop: ## stop the container.
	@exec docker stop k8s-sidecar

rm: ## remove the container.
	@exec docker rm -f k8s-sidecar

clean:
	rm -f kubectl
	rm -f .tag
