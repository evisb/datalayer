---
title: JupyterHub Docker
---

# JupyterHub Docker

```bash
docker run -p 8000:8000 --rm -d --name jupyterhub datalayer/jupyterhub:0.0.1 jupyterhub
open http://localhost:8000
docker ps
docker exec -it jupyterhub bash # adduser datalayer
docker stop jupyterhub
```

See also the [JupyterHub Deploy Docker](https://github.com/jupyterhub/jupyterhub-deploy-docker) repository.
