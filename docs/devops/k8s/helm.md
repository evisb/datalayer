---
title: Helm
---

# Helm

> [Helm](https://helm.sh) is the package manager for Kubernetes - A way to find, share, and use software built for Kubernetes.

Install the [binary Helm](https://github.com/helm/helm/blob/master/docs/install.md) on your local env.

```bash
dla helm-install
```

Use Helm with CLI commands.

```bash
helm version
helm ls
```

Deploy a Hello world chart.

```bash
helm install $DLAHOME/etc/k8s/helm/hello -n hello
helm ls
helm status hello
kubectl get po
kubectl get svc
```

Browse the `hello` page if you run on minikube.

```bash
minikube service hello
```

Delete your chart.

```bash
helm delete hello --purge
```

## Options

In case of docker pull timeout, use `--timeout=`.

```bash
helm install --dry-run
```

```bash
helm template
```

# Helm Repository

```bash
cd $DLAHOME/etc/helm
helm package .
helm serve --repo-path .
```

```bash
helm repo rm datalayer
helm repo add datalayer http://helm-charts.datalayer.io
```

```bash
helm reset
```

## Upgrade

```bash
# --wait
helm init --canary-image --upgrade
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
helm init --service-account tiller --upgrade
kubectl rollout status -w deployment/tiller-deploy --namespace=kube-system
helm repo list
helm ls -a
```

## Alternatives

+ [KsonNet](https://github.com/ksonnet/ksonnet), see also [official website](https://ksonnet.io).
+ [Flekszible](https://github.com/elek/flekszible).
