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

.PHONY: clean build dist dev

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

yarn-css:
	@exec yarn build:scss

yarn-uglify:
	@exec yarn uglify

yarn-start:
	yarn start

static-to-s3:
	@exec ./dev/static-to-s3.sh

py-clean:
	rm -fr build
	rm -fr dist
	rm -fr *.egg-info
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +

py-install:
	python setup.py install --record files.txt

py-build:
	python setup.py sdist bdist_egg bdist_wheel

py-start:
	python datalayer_ui/main.py

py-publish:
	python setup.py sdist bdist_egg bdist_wheel upload

py-repl:
	PYTHONPATH=./dist/datalayer_ui-0.0.1-py3-none-any.whl python

dist: build
	@exec ./dev/dist.sh

watch:
	@exec yarn watch

dev:
	@exec yarn dev
