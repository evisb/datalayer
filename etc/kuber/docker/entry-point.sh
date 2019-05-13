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

start_with_k8s() {

  ./kuber \
    server \
    --apiserver-host="$APISERVER_HOST" \
    --google-api-key="$GOOGLE_API_KEY" \
    --google-client-id="$GOOGLE_CLIENT_ID" \
    --google-redirect="$GOOGLE_REDIRECT" \
    --google-secret="$GOOGLE_SECRET" \
    --google-scope="$GOOGLE_SCOPE" \
    --hdfs="$HDFS" \
    --insecure-bind-address="$KUBER_INSECURE_BIND_ADDRESS" \
    --insecure-port="$KUBER_INSECURE_PORT" \
    --datalayer-ui="$DATALAYER_UI" \
    --datalayer-rest="$DATALAYER_API_REST" \
    --datalayer-ws="$DATALAYER_API_WS" \
    --microsoft-application-id="$MICROSOFT_APPLICATION_ID" \
    --microsoft-redirect="$MICROSOFT_REDIRECT" \
    --microsoft-secret="$MICROSOFT_SECRET" \
    --microsoft-scope="$MICROSOFT_SCOPE" \
    --zeppelin-rest="$ZEPPELIN_REST" \
    --zeppelin-ws="$ZEPPELIN_WS" \
    --twitter-consumer-key="$TWITTER_CONSUMER_KEY" \
    --twitter-consumer-secret="$TWITTER_CONSUMER_SECRET" \
    --twitter-redirect="$TWITTER_REDIRECT"

}

start_without_k8s() {

  ./kuber \
    server \
    --insecure-bind-address 0.0.0.0 \
    --apiserver-host http://localhost:8001

}

cd /dla
start_without_k8s
