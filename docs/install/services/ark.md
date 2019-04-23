---
title: Install ARK Service
---

# Install ARK Service

Install ARK Service.

```bash
kubectl apply -f $DLAHOME/repos/ark/examples/common/00-prereqs.yaml
kubectl apply -f $DLAHOME/repos/ark/examples/minio
kubectl apply -f $DLAHOME/repos/ark/examples/common/10-deployment.yaml
```

```bash
kubectl apply -f $DLAHOME/repos/ark/examples/nginx-app/base.yaml
```

```bash
kubectl get deployments -l component=ark --namespace=heptio-ark
kubectl get deployments --namespace=nginx-example
open $(minikube -n nginx-example service my-nginx --url)
```

```bash
ark backup create nginx-backup --selector app=nginx
ark backup get nginx-backup
ark backup describe nginx-backup
```

```bash
kubectl delete namespace nginx-example
kubectl get deployments --namespace=nginx-example
kubectl get services --namespace=nginx-example
kubectl get namespace nginx-example
```

```bash
ark restore create --from-backup nginx-backup
ark restore get
ark restore describe nginx-backup-20180412153148
kubectl get namespace nginx-example
kubectl get deployments --namespace=nginx-example
kubectl get services --namespace=nginx-example
open $(minikube -n nginx-example service my-nginx --url)
```

```bash
ark backup delete nginx-backup
ark backup get nginx-backup
```

```bash
kubectl delete -f $DLAHOME/repos/ark/examples/common
kubectl delete -f $DLAHOME/repos/ark/examples/minio
kubectl delete -f $DLAHOME/repos/ark/examples/nginx-app/base.yaml
```

## Plugin Example

+ https://github.com/heptio/ark
+ https://github.com/heptio/ark-plugin-example

+ https://github.com/portworx/ark-plugin

+ https://www.digitalocean.com/community/tutorials/how-to-back-up-and-restore-a-kubernetes-cluster-on-digitalocean-using-heptio-ark
