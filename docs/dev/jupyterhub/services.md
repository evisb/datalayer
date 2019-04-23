---
title: JupyterHub Services
---

# JupyterHub Services

```bash
# Get the auth token.
jupyterhub token
```

```bash
cat <<EOF > jupyterhub_config.py
# --- Services ---
c.JupyterHub.services = [
    {'name': 'cull-idle', 'api_token': 'd587ce42bc34407687901bbc723dcb0f'},
]
EOF
```

```bash
export JUPYTERHUB_API_TOKEN=`jupyterhub token`
python3 cull_idle_servers.py [--timeout=900] [--url=http://127.0.0.1:8081/hub/api]
```

## Examples

Try the [JupyterHub Services examples](https://github.com/datalayer/datalayer/tree/master/etc/examples/jupyterhub-services).
