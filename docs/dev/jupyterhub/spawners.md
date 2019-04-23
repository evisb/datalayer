---
title: JupyterHub Spawners
---

# JupyterHub Spawners

Define the Spawner in `jupyterhub_config.py`.

```bash
c.Spawner.options_form = '<input name="c.Spawner.default_url" val="/lab"/><br>Please Choose <select name="letter" multiple="true"><option value="/lab">Jupyter Lab</option><option value="/tree">Classic Notebook</option></select>'
```

```bash
pip install dockerspawner
# Docker Spawner.
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.volumes = {'jupyterhub-user-{username}': '/home/jovyan/work', 'jupyterhub-test': {'bind': '/home/jovyan/shared', 'mode': 'rw'}}
```

```python
# Kube Spawner.
c.KubeSpawner.environment.update({'HADOOP_USER_NAME': get_username})
c.KubeSpawner.extra_pod_config.update({'hostNetwork': "True"})
```

```python
# Custom Spawner.
class CustomDockerSpawner(DockerSpawner):
    def get_env(self):
        env = super().get_env()
        env['VAR'] = self.user.name 
        return env
c.JupyterHub.spawner_class = CustomDockerSpawner
```

## Examples

+ https://github.com/jupyterhub/batchspawner.git
+ https://github.com/jupyterhub/dockerspawner.git
+ https://github.com/jupyterhub/kubespawner.git
+ https://github.com/jupyterhub/sudospawner.git
+ https://github.com/jupyterhub/systemdspawner
+ https://github.com/jupyterhub/wrapspawner.git
