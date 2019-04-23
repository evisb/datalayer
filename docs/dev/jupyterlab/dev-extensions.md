---
title: JupyterLab Develop Extensions
---

# JupyterLab Develop Extensions

[JupyterLab Extensions Dev Doc](https://jupyterlab.readthedocs.io/en/latest/developer/extension_dev.html).

```bash
cookiecutter https://github.com/jupyterlab/extension-cookiecutter-ts
# In Extension Repo.
yarn install
yarn run build
# See in /opt/miniconda3/envs/datalayerhub/share/jupyter/lab/build_config.json
jupyter labextension link .
yarn watch
# In JupyterLab Repo.
cd $DLAHOME/repos/jupyterlab
jupyter lab build
jupyter lab --watch
# jupyter lab --dev-mode
# jupyter lab --dev-mode --watch
# jupyter lab --core-mode
```

```bash
cd $DLAHOME/apps/jupyterlab-datalayer
yarn install
yarn run build
jupyter labextension install
```

```bash
# Step 1
cd $DLAHOME/apps/jupyterlab-datalayer
jupyter labextension link
yarn watch
# Step 2
cd $DLAHOME/repos/jupyterlab
jupyter lab --watch
```

```bash
# Installation and activation of Git handler.
# Installation and activation for jupyterlab_git python handler package.
cd $DLAHOME/repos/jupyterlab-git
pip install .
jupyter serverextension enable --py jupyterlab_git
yarn install
yarn run build
jupyter labextension install
# Launch JupyterLab & you will see the new Git buttons on the left side of the window.
jupyter lab
```

```bash
# If you must install a extension into a development branch of JupyterLab, you have to graft it into the source tree of JupyterLab itself. In the JupyterLab root directory, where <path-or-url> refers either to an extension npm package on the local filesystem, or a URL to a git repository for an extension npm package.
yarn run add:sibling $DLAHOME/apps/jupyterlab-datalayer
jupyter lab --dev-mode --watch
# This operation may be subsequently reversed by running.
yarn run remove:sibling $DLAHOME/apps/jupyterlab-datalayer
```

## Versions

```bash
# Align dependencies with latest jupyterlab releases.
jupyter labextension update
# or...
yarn upgrade --latest --exact --scope @jupyterlab
```

## Publish

```bash
npm login
npm config set scope datalayer
# Publishing extensions.
npm publish --access=public
```

## Example

```bash
# Link all extensions in packages.
yarn run link
# Link geojson-extension only.
jupyter labextension link packages/geojson-extension
# After making changes to the source packages, the jupyter packages must be rebuilt.
# Rebuild the source.
cd $DLAHOME/repos/jupyterlab && \
  jupyter lab build
```

## Watch

```bash
# You may also watch the jupyter-renderers directory for changes and automatically rebuild.
# In one terminal tab, watch the jupyter-renderers directory.
yarn watch
# In another terminal tab, run jupyterlab with the watch flag.
jupyter lab --watch
```
