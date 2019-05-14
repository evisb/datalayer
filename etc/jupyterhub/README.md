[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

# JupyterHub

Install JupyterHub on Minikube.

```bash
cd $DLAHOME/repos/jupyterhub-k8s
export DOCKER_REPO=localhost:5000
echo """
hub:
  image:
    name: $DOCKER_REPO/jupyterhub
    tag: 0.0.1
  imagePullPolicy: Always
  extraEnv:
    JUPYTER_ENABLE_LAB: 1
  extraConfig: |
    c.KubeSpawner.cmd = [\"jupyter-labhub\"]
auth:
  admin:
    users:
      - adminuser1
      - adminuser2
proxy:
  secretToken: \"$(openssl rand -hex 32)\"
  chp:
    image:
      name: $DOCKER_REPO/jupyterhub-http-proxy
      tag: 0.0.1
    imagePullPolicy: Always
prePuller:
  hook:
    image:
      name: $DOCKER_REPO/jupyterhub-image-awaiter
      tag: 0.0.1
    imagePullPolicy: Always
singleuser:
  networkTools:
    image:
      name: $DOCKER_REPO/jupyterhub-network-tools
      tag: 0.0.1
    imagePullPolicy: Always
  defaultUrl: \"/lab\"
  image:
    name: $DOCKER_REPO/jupyterlab
    tag: 0.0.1
  imagePullPolicy: Always
  cpu:
    limit: .5
    guarantee: .5
  memory:
    limit: 200M
    guarantee: 200M
  lifecycleHooks:
    postStart:
      exec:
        command: [\"gitpuller\", \"https://github.com/data-8/materials-fa17\", \"master\", \"materials-fa\"]
  storage:
    capacity: 10Mi
cull:
  podCuller:
    image:
      name: $DOCKER_REPO/jupyterhub-pod-culler
      tag: 0.0.1
    imagePullPolicy: Always
""" > ./datalayer-config.yaml
helm install ./jupyterhub \
  --name=datalayer \
  --namespace=datalayer \
  --timeout=99999 \
  -f datalayer-config.yaml
# kubectl get pods -n datalayer
# kubectl get svc -n datalayer
# minikube -n datalayer service proxy-public --url
open $(minikube -n datalayer service proxy-public --url)
```
