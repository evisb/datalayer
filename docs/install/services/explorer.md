---
title: Install Explorer Service
---

# Install Explorer Service

`Datalayer Explorer` is the WEB user interface to analyse datasets, an innovative WEB Notebook for Data Scientists to better collaborate with Business.

![Datalayer Explorer](/_images/what/explorer.svg "Datalayer Explorer")

```bash
# --type= ClusterIP | NodePort | LoadBalancer
kubectl expose pod $POD --port=9090 --name=dashboard-ci-9090 --type=ClusterIP
kubectl expose pod $POD --port=9090 --target-port=80 --name=dashboard-np-9090 --type=NodePort
kubectl expose pod $POD --port=9090 --target-port=9090 --name=dashboard-np-9090 --type=NodePort
kubectl expose pod $POD --port=9090 --target-port=9090 --name=dashboard-lb-9090 --type=LoadBalancer
kubectl expose pod $POD --target-port=9090 --name=dashboard-lb-9090 --type=LoadBalancer
helm delete k8s-dashboard --purge
```

```bash
metadata:
  name: xxx-lb
  annotations:
    "service.beta.kubernetes.io/aws-load-balancer-ssl-ports": "443"
    "service.beta.kubernetes.io/aws-load-balancer-ssl-cert": "arn:aws:acm:us-west-2:345579675507:certificate/ce5a63ee-e9e0-472b-a5d6-a28303fe1d6a"
```

```bash
    service.beta.kubernetes.io/aws-load-balancer-backend-protocol: "tcp"
    service.beta.kubernetes.io/aws-load-balancer-proxy-protocol: "*"
    service.beta.kubernetes.io/aws-load-balancer-ssl-cert: "01:27:ae:27:54:fc:02:a3:1c:38:08:ba:61:95:8a:fa"
    service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: 3600
```

```bash
cat << EOF | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: ingress-config
data:
  80: "default/explorer-kuber:9091"
```

```bash
cat << EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: spitfire-lb
  annotations:
#    service.beta.kubernetes.io/aws-load-balancer-internal: "0.0.0.0/0"
    service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: 3600
    service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags: "kuber-role=spitfire"
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8080
  selector:
    app: spitfire
    release: spitfire
EOF
```

```bash
kubectl describe services spitfire-lb | grep Ingress
```

```bash
cat << EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: spitfire-lb
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8080
  selector:
    app: spitfire
    release: spitfire
EOF
```

```bash
echo http://localhost:8001/api/v1/namespaces/default/services/http:explorer-explorer:9091/proxy/#/
```

```bash
#    service.beta.kubernetes.io/aws-load-balancer-internal: "0.0.0.0/0"
  cat << EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: explorer-lb
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-connection-idle-timeout: 3600
    service.beta.kubernetes.io/aws-load-balancer-additional-resource-tags: "kuber-role=explorer"
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 9091
  selector:
    app: explorer
    release: explorer
EOF
```

```bash
cat << EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: wabco-spark-ui-lb
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 4040
  selector:
    spark-role: driver
EOF
```
