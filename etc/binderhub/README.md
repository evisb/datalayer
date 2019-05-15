[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

# Binder

[BinderHub Repository](https://github.com/jupyterhub/binderhub)

[BinderHub Docs](https://binderhub.readthedocs.io).

[Binder Examples Repository](https://github.com/binder-examples)

[Binder Gitter Commmunity](https://gitter.im/jupyterhub/binder).

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