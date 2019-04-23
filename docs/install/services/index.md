---
title: Install Services
---

# Install Services

Datalayer is available with the following services that makes up the `Datalayer Science Platform`.

The services are deployed in the Kubernetes Cluster via [Helm charts](https://github.com/datalayer/datalayer/tree/master/etc/helm).

Ensure you have [Helm](/devops/k8s/helm.md) on your local machine.

```bash
dla helm-install
```

<!--

Add the Datalayer Helm chart repository (for now, we strongly recommend to use the latest and greatest snapshots).

```bash
helm repo add datalayer http://helm-charts.datalayer.io
```

-->

![DSP on Kubernetes](/_images/dsp/dsp-k8s.svg)

In the long run, the mesh will be deployed in [Istio](https://istio.io) or [Linkerd](https://linkerd.io).

## IAM

For `IAM` (Identity and Access Management), install:

+ [Vault](/install/services/vault.md) service.
+ [LDAP](/install/services/ldap.md) service.
+ [Keycloak](/install/services/keycloak.md) service.

```bash
dla dsp-services-install vault
dla dsp-services-install ldap
dla dsp-services-install keycloak
```

## Instrument

For instrumentation, install [Kuber](/install/services/kuber.md) and the [K8S Dashboard](/install/services/k8s-dashboard.md).

```bash
dla dsp-services-install kuber
dla dsp-services-install k8s-dashboard
dla dsp-services-install ark
```

```bash
# Launch a K8S proxy in another terminal to have easy access to the services.
kubectl proxy
```

Check the [K8S Dashboard](http://localhost:8001/api/v1/namespaces/kube-system/services/http:k8s-dashboard-kubernetes-dashboard:/proxy/#!/overview?namespace=_all).

## Observe

For observability, install [Heapster](/install/services/heapser.md), [K8S Metrics](/install/services/k8s-metrics.md) and [Prometheus](/install/services/prometheus.md).

```bash
dla dsp-services-install heapster
dla dsp-services-install k8s-metrics
dla dsp-services-install prometheus
```

## HDFS

Install [HDFS](/install/services/hdfs.md), the `Hadoop Distributed File System` to persist your Big Datasets.

```bash
dla dsp-services-install hdfs
```

## HBase

Install [HBase](/install/services/hbase.md).

```bash
dla dsp-services-install hbase
```

## IPFS

Install [IPFS](/install/services/ipfs.md).

```bash
dla dsp-services-install ipfs
```

## Etcd

Install the [Etcd](/install/services/etcd.md) service.

## Queuing

```bash
dla dsp-services-install zookeeper
dla dsp-services-install kafka
```

## Search

```bash
dla dsp-services-install solr
```

## Spark

Install [Spark](/install/services/spark.md) to analyse your Big Datasets.

```bash
dla dsp-services-install spark
```

## JupyterHub

Install [JupyterHub](/install/services/jupyterhub.md) service.

```bash
dla dsp-services-install jupyterhub
```

## Kernels

Install the [Kernels](/install/services/kernels.md).

```bash
dla dsp-services-install kernels
```

## Binder

Install the [Binder](/install/services/binder.md) service.

```bash
dla dsp-services-install binder
```

## Datalayer

+ [Explorer](/install/services/explorer.md) to analyse datasets and control your system via a WEB UI.
+ [Library](/install/services/library.md).
+ [Ingrewss](/install/services/ingress.md).

```bash
dla dsp-services-install explorer
dla dsp-services-install library
dla dsp-services-install ingress
```
