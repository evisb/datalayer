[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

:chart_with_upwards_trend: :bar_chart: Discover, Collaborate and Analyze Data.

This folder contains the `Datalayer UI` source code that allows accessing the `Datalayer Science Platform` in a visual way.

The UI will help you create and manage your K8S cluster and transform it into a powerful solution for your Big Data Science projects.

## Build

Datalayer UI is built on `react.js` and other javascript libraries.

Ensure you fullfill the [requirements](https://docs.datalayer.io/ops/requirements.html).

```bash
# Install the dependencies and build.
cd $DLAHOME/apps/ui && \
  make install && \
  make build
```

## Dependencies

You are expected to have the following running services.

```bash
# A kubernetes cluster, eg with minikube.
dla minikube-start && \
  dla minikube-status && \
  dla minikube-dashboard
```

```bash
# A running kubernetes proxy.
cd $DLAHOME/apps/kuber && \
  open http://localhost:8001 && \
  make k8s-proxy
```

```bash
# A running keycloak server integrated with ldap.
# Create a `datalayer` realm.
# Create and a `datalayer` client with `Root URL` `http://localhost:8080`.
# Define the `Valid Redirect URIs`.
#  http://localhost:9700/*
#  http://localhost:8000/*
# Set the `datalayer` client Access Type to `confidential` and copy the `Secret Credential`.
# Update `~/.datalayer/dlarc` with the copied secret and `source ~/.datalayer/dlarc`.
# Add and configure the `ldap` User Federation.
#   Vendor=`Other`
#   Connection URL: `ldap://ldap`
#   Users DN: `ou=users,dc=datalayer,dc=io`
#   Bind DN: `cn=admin,dc=datalayer,dc=io`
#   Bind Credential: `admin`
#   Cache Policy: `NO_CACHE`
# and `Synchronize all users`.
# Check `eric` user login on http://localhost:8080/auth/realms/datalayer/account (password is `123`).
dla dsp-swarm-up dev && \
  sleep 3s && \
  dla dsp-swarm-up seed-ldap && \
  open http://localhost:8080/auth/admin/master/console # admin / admin
```

## Develop

Run iam, kuber, jupyterhub, library and ui in `dev` mode.

```bash
cd $DLAHOME/apps/ui && \
  make dev
```

If you prefer separated processes, ensure you have iam, kuber, library and jupyterhub running.

```bash
# shell #1: start the ui compiler.
cd $DLAHOME/apps/ui && \
  echo http://localhost:4326?kuberRest=http://localhost:9091 && \
  make yarn-start
# shell #2: start the ui server.
cd $DLAHOME/apps/ui && \
  DLA_UI_INDEX_PAGE=index.html && \
  open http://localhost:9600?kuberRest=http://localhost:9091 && \
  python datalayer_ui/main.py
```

# Get Help

```bash
# print the help.
cd $DLAHOME/apps/ui && \
  make help
```

<!--
"@datalayer/kuber": "file:./../kuber",
"@types/enzyme": "2.7.9",
tests.js
```
var context = require.context('../lib', true, /.+\.test\.js?$/);
context.keys().forEach(context);
module.exports = context;
```
"@types/react-redux-toastr": "7.0.10",
"react-addons-css-transition-group": "15.5.2",
"react-addons-shallow-compare": "15.5.2",
"react-addons-transition-group": "15.5.2"
-->

![Explorer](https://raw.githubusercontent.com/datalayer/datalayer/master/docs/_images/what/explorer.svg?sanitize=true "Explorer")
