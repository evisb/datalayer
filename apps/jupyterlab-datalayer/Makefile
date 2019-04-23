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
	@exec make yarn-help

all: clean install build dist ## Clean Install and Build

clean: yarn-clean py-clean

install: yarn-install py-install

build: yarn-build py-build

yarn-help:
	@exec ./dev/yarn-help.sh

yarn-uglify:
	@exec yarn uglify

yarn-clean:
	@exec yarn clean
	rm .yarnclean || true
	rm yarn.lock || true
	rm yarn-error.log || true
#	gulp clean
#	rm -fr dist lib node_modules

yarn-install:
	@exec ./dev/yarn-install.sh

yarn-build:
	@exec yarn build

yarn-start:
	@exec yarn start

py-clean:
	rm -fr build
	rm -fr dist
	rm -fr *.egg-info
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +

py-build:
	python setup.py sdist bdist_egg bdist_wheel

py-install:
	python setup.py install --record files.txt

py-publish:
	python setup.py sdist bdist_egg bdist_wheel upload

py-repl:
	PYTHONPATH=./dist/jupyterlab_datalayer-0.0.1-py3-none-any.whl python

server-ext-enable: py-build
	@exec jupyter serverextension enable --py jupyterlab_datalayer --sys-prefix
	@exec jupyter serverextension list

lab-ext-enable: yarn-build
	@exec jupyter labextension link .
	@exec jupyter labextension list

ext-enable: server-ext-enable lab-ext-enable
	
dist: build
	@exec ./dev/make-dist.sh

watch:
	yarn watch
