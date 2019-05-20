[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

# Jupyter Kernel Gateway

```bash
pip install jupyter_kernel_gateway
# conda install -c conda-forge jupyter_kernel_gateway
jupyter kernelgateway --help-all
# --api='kernel_gateway.notebook_http'
# --seed_uri='x'
jupyter kernelgateway --KernelGatewayApp.ip=0.0.0.0 --KernelGatewayApp.port=8889 --port_retries=0
```

## Nb2Kg - Notebook to Kernel Gateway

[Notebook to Kernel Gateway](https://github.com/jupyter/nb2kg).

[Add support for retrieving kernelspec resources](https://github.com/jupyter/nb2kg/pull/23).

```bash
pip install nb2kg
jupyter serverextension enable --py nb2kg --sys-prefix
```

```bash
cd $DLAHOME/repos/jupyter-nb2kg && \
  pip install -e . && \
  jupyter serverextension enable --py nb2kg --sys-prefix
```

```bash
export KG_URL=http://127.0.0.1:8889
jupyter lab \
  --NotebookApp.session_manager_class=nb2kg.managers.SessionManager \
  --NotebookApp.kernel_manager_class=nb2kg.managers.RemoteKernelManager \
  --NotebookApp.kernel_spec_manager_class=nb2kg.managers.RemoteKernelSpecManager 
```

```bash
jupyter serverextension disable nb2kg
```
