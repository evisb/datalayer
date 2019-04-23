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

.PHONY: clean build dist

default: all ## Default target is all.

help: ## display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

all: clean install build ## Clean Install and Build

clean:
	rm ./kuber || true

build: ## Build
	@exec go build
	@exec ls -alp kuber

build-to-docker: ## Build for Linux
	@exec ./build-to-docker.sh

install: build ## Install
	@exec cp ./kuber /usr/local/bin

k8s-proxy:
	@exec echo Launching K8S Proxy - open http://localhost:8001
	@exec kubectl proxy

k8s-proxy-d:
	@exec echo Launching K8S Proxy in background - open http://localhost:8001
	@exec kubectl proxy &

start:
	@exec echo open http://localhost:9091/kuber/about/kuber.html
	@exec go run main.go server --apiserver-host=http://localhost:8001

start-80:
	@exec cd $DLAHOME/apps/kuber && \
	  ./kuber \
		server \
		--insecure-bind-address 0.0.0.0 \
		--insecure-port 80 \
		--apiserver-host http://localhost:8001
