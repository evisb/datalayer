---
title: Install Spark Service
---

# Install Spark Service

You need to install the Spark `Resource Staging Server` and the Spark `Shuffle Service`.

```
helm install spark \
  -n spark
```

```bash
# Deploy Spark Helm Chart.
cd $DLAHOME/etc/k8s/helm/spark
helm install \
  spark \
  --set spark.resourceStagingServer.image=localhost:5000/spark-resource-staging-server:2.2.0 \
  --set spark.resourceStagingServer.masterOperator=In \
  --set spark.shuffleService.image=localhost:5000/spark-shuffle-service:2.2.0 \
  --set spark.shuffleService.masterOperator=In \
  --set spark.imagePullPolicy=Always \
  -n spark
```

List the pods with `kubectl get pods -l kuber=spark` and check the running Spark pods.

```
NAME                                                READY     STATUS    RESTARTS   AGE
spark-resource-staging-server-c5db88df9-n42gw   1/1       Running   0          15s
spark-shuffle-service-5r2h7                     1/1       Running   0          15s
spark-shuffle-service-9pxxc                     1/1       Running   0          15s
spark-shuffle-service-s2vk8                     1/1       Running   0          15s
```
