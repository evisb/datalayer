[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

# BinderHub

```bash
dla minikube-start
helm version
cd $DLAHOME/repos/jupyter-binderhub
pip install -e . -r dev-requirements.txt
./testing/minikube/install-hub
eval $(minikube docker-env)
python -m binderhub -f testing/minikube/binderhub_config.py
open http://localhost:8585
```
