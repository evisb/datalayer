#!/usr/bin/env bash

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

./node_modules/.bin/uglifyjs dist/@datalayer/datalayer.js -o dist/@datalayer/datalayer.min.js -c -m

TARGET_FOLDER="ui"
# rm -fr $TARGET_FOLDER
# yarn install
# yarn build:dist
rm -fr $TARGET_FOLDER
mkdir $TARGET_FOLDER
cp index.min.html $TARGET_FOLDER/index.html
mkdir -p $TARGET_FOLDER/dist/@datalayer
# cp dist/explorer.js $TARGET_FOLDER/dist
cp dist/@datalayer/datalayer.min.js $TARGET_FOLDER/dist/@datalayer
cp -r css $TARGET_FOLDER
cp -r fonts $TARGET_FOLDER
cp -r img $TARGET_FOLDER
cp -r resources $TARGET_FOLDER
# cp dev/server.sh $TARGET_FOLDER
