# Heapster

> Heapster is [deprecated](https://github.com/kubernetes-retired/heapster/blob/master/docs/deprecation.md).

To ease the management, it is interesting to install `Heapster` as monitoring tool.

```bash
helm install -n heapster \
  --namespace kube-system \
  stable/heapster
```

Check `Heapster` is running.

```bash
export POD_NAME=$(kubectl get pods --namespace kube-system -l "app=heapster-heapster" -o jsonpath="{.items[0].metadata.name}")
echo http://127.0.0.1:8082
kubectl --namespace kube-system port-forward $POD_NAME 8082
```
