---
title: JupyterHub on Kubernetes
---

# JupyterHub on Kubernetes

[JupyterHub on Kubernetes Repository](https://github.com/jupyterhub/zero-to-jupyterhub-k8s).

[JupyterHub on Kubernetes Docs](https://zero-to-jupyterhub.readthedocs.io).

## Helm Chart

[JupyterHub on Kubernetes Helm Charts Repository](https://github.com/jupyterhub/helm-chart).

[JupyterHub on Kubernetes Helm Charts Deployment Repository](https://jupyterhub.github.io/helm-chart).

```bash
mkdir jupyter
cd jupyter
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart
helm repo update
```

## Install

```bash
# singleuser:
#   image:
#     name: jupyter/scipy-notebook
#     tag: 8a1b90cbcba5

# singleuser:
#   storage:
#     type: none
#   storage:
#     dynamic:
#       storageClass: <storageclass-name>

# rbac:
#    enabled: false

# ingress:
#   enabled: true
#   hosts:
#     - <hostname>
#   annotations:
#     kubernetes.io/tls-acme: "true"
#   tls:
#    - hosts:
#       - <hostname>
#      secretName: kubelego-tls-jupyterhub

echo """
proxy:
  secretToken: \"$(openssl rand -hex 32)\"
singleuser:
  defaultUrl: \"/lab\"
  image:
    name: jupyter/scipy-notebook
    tag: 1085ca054a5f
#    name: datalayer/jupyterlab-hub
#    tag: 0.0.1
    pullPolicy: Always
  cpu:
    limit: .5
    guarantee: .5
  memory:
    limit: 1G
    guarantee: 1G
#  lifecycleHooks:
#    postStart:
#      exec:
#        command: [\"gitpuller\", \"https://github.com/data-8/materials-fa17\", \"master\", \"materials-fa\"]
  storage:
    capacity: 1Gi
hub:
  extraEnv:
    JUPYTER_ENABLE_LAB: 1
  extraConfig: |
    c.KubeSpawner.cmd = [\"jupyter-labhub\"]
  imagePullPolicy: Always
cull:
  enabled: \"true\"
  users: \"true\"
auth:
  admin:
    users:
      - adminuser1
      - adminuser2
""" > ./jupyterhub-config.yaml
cat ./jupyterhub-config.yaml
```

```bash
helm install jupyterhub/jupyterhub \
  --version=v0.7-6162c7b \
  --name=jupyterhub \
  --namespace=jupyterhub \
  --timeout=99999 \
  -f jupyterhub-config.yaml
```

```bash
kubectl get pods -n jupyterhub
kubectl get svc -n jupyterhub
minikube -n jupyterhub service proxy-public --url
open $(minikube -n jupyterhub service proxy-public --url)
```

## Upgrade

```bash
helm upgrade jupyterhub \
  jupyterhub/jupyterhub \
  --version=v0.7-6162c7b \
  --namespace=jupyterhub \
  -f jupyterhub-config.yaml
```

## Delete

```bash
helm delete jupyterhub --purge
kubectl delete namespace jupyterhub
```
