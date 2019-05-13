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

echo -e "\x1b[34m\x1b[43mCopying static assets to AWS S3\x1b[0m"

aws s3 cp $DLAHOME/apps/ui/build/static s3://datalayer/static --recursive
aws s3 cp $DLAHOME/apps/ui/build/img s3://datalayer/img --recursive

sed -e "s|/static/|https://d1klwlf7zy9tdr.cloudfront.net/static/|g" $DLAHOME/apps/ui/build/index.html > /tmp/index1.html
sed -e "s|a.src=s.p+\"static/js/\"|a.src=\"https://d1klwlf7zy9tdr.cloudfront.net/static/js/\"|g" /tmp/index1.html > /tmp/index2.html
cp /tmp/index2.html $DLAHOME/apps/ui/build/index.html
