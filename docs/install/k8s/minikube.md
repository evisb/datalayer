---
title: Install Minikube
---

# Install Minikube

> Quick Start the Datalayer Science Platform on your local minikube.
>
> Check the [requirements](/devops/requirements.md) to setup your local environment.

Install and start Minikube on your local env.

```bash
dla minikube-install && \
  dla minikube-start
```

Read more about [Minikube on Github](https://github.com/kubernetes/minikube).

## Validate

List the Pods.

```bash
k get pods --all-namespaces --watch
```

Test with a simple HTTP Headers echo.

```bash
kubectl apply -f $DLAHOME/etc/k8s/specs/echo/echo.yaml
minikube service echoheaders --url
curl $(minikube service echoheaders --url)
kubectl delete -f $DLAHOME/etc/k8s/specs/echo/echo.yaml
```

## Install the Services

Follow the [instructions to install the Datlayer services](/install/services/index.md) on top of Minikube.

# Addons

List the Minikube addons.

```bash
dla minikube-addons
```

## Commands

Some useful Minikube commands.

```bash
minikube status
minikube ssh
minikube ip
minikube update-context
minikube logs -f
minikube start
minikube stop
minikube delete
```

## Local Registry

Share your Docker Images with a Minikube hosted local registry.

Minikube Registry - Option 1

```bash
# This command sets up docker to use the same docker daemon as your minikube cluster does.
# This means images you build are directly available to the cluster.
eval $(minikube docker-env)
#            When you no longer wish to use the minikube host, you can undo this change by running.
eval $(minikube docker-env -u)
```

Minikube Registry - Option 2.

```bash
minikube addons enable registry
kubectl create -f $DLAHOME/etc/k8s/specs/registry/kube-registry.yaml
kubectl port-forward --namespace kube-system $(kubectl get po -n kube-system | grep kube-registry-v0 | awk '{print $1;}') 5000:5000
```

```bash
minikube ssh
curl http://localhost:5000
kubectl port-forward --namespace kube-system $(kubectl get po -n kube-system | grep kube-registry-v0 | awk '{print $1;}') 5000:5000
curl http://localhost:5000
```

## Alternatives

+ https://github.com/kubernetes-sigs/kubeadm-dind-cluster.
+ https://github.com/kinvolk/kube-spawn.
+ https://github.com/kubernetes/minikube.
+ https://github.com/danderson/virtuakube.
+ https://github.com/ubuntu/microk8s ([Microk8s](https://microk8s.io)).

See also [kind](/devops/k8s/kind.md) for a docker based local multinode cluster.
