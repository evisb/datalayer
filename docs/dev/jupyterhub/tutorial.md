---
title: JupyterHub Tutorial
---

# JupyterHub Tutorial

[JupyterHub Tutorial](https://jupyterhub-tutorial.readthedocs.io).

[JupyterHub Tutorial Repository](https://github.com/jupyterhub/jupyterhub-tutorial).

## Examples

```bash
echo http://localhost:8010
AUTH_SPAWN=pam-sudo && \
  jupyterhub \
    -f $DLAHOME/conf/jupyterhub/_template/${AUTH_SPAWN}/jupyterhub_config.py \
    --log-level=DEBUG \
    --port 8010
```
