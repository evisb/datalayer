---
title: Notebook to Kernel Gateway
---

## Notebook to Kernel Gateway

[Notebook to Kernel Gateway](https://github.com/jupyter/nb2kg).

[Add support for retrieving kernelspec resources](https://github.com/jupyter/nb2kg/pull/23).

```bash
pip install nb2kg
jupyter serverextension enable --py nb2kg --sys-prefix
export KG_URL=http://127.0.0.1:8889
jupyter lab \
  --NotebookApp.session_manager_class=nb2kg.managers.SessionManager \
  --NotebookApp.kernel_manager_class=nb2kg.managers.RemoteKernelManager \
  --NotebookApp.kernel_spec_manager_class=nb2kg.managers.RemoteKernelSpecManager 
```

```bash
jupyter serverextension disable nb2kg
```
