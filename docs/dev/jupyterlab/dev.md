---
title: JupyterLab Develop
---

# JupyterLab Develop

[JupyterLab Docs for Dev](https://jupyterlab.readthedocs.io/en/latest/developer/repo.html).

[TypeScript Doc](http://jupyterlab.github.io/jupyterlab/index.html).

## Build

Building consists of:

+ Populating the staging directory using template files.
+ Handling any locally installed packages.
+ Ensuring all installed assets are available.
+ Bundling the assets.
+ Copying the bundled assets to the static directory.

Note that building will always use the latest JavaScript packages that meet the dependency requirements of JupyterLab itself and any installed extensions.

See also [Add webpack-visualizer-plugin to dev_mode webpack config](https://github.com/jupyterlab/jupyterlab/pull/5722).

```bash
# Set yarn cache dir.
yarn cache dir
yarn config set cache-folder ~/.yarn-cache
```

```bash
# Install prerequisites.
git clone https://github.com/jupyterlab/jupyterlab.git && \
  cd jupyterlab && \
  pip install -e . && \
  yarn install
```

```bash
# Builds the source files into javascript files in lib folder.
cd $DLAHOME/repos/jupyterlab && \
  yarn build && \
  jupyter lab build
```

```bash
# Build more accurate sourcemaps that show the original Typescript code when debugging.
# However, it takes a bit longer to build the sources, so is used only to build for production by default.
cd $DLAHOME/repos/jupyterlab && \
  yarn run build:dev:prod && \
  ls -alph dev_mode/static && \
  du -h dev_mode/static
```

```bash
# Build the core mode assets (optional).
yarn run build:core
```

```bash
# extensions schemas settings staging static themes
ls $DLAHOME/opt/miniconda3/envs/datalayer/share/jupyter/lab
```

## Start

```bash
jupyter lab --dev-mode --watch --browser chromium-browser
# If you wish to run JupyterLab with the set of pinned requirements that was shipped with the Python package, you can launch as.
jupyter lab --core-mode
```

## Test

```bash
cd $DLAHOME/repos/jupyterlab && \
  yarn build:test && \
  yarn test
```

## Docs

```bash
echo file://$PWD/docs/index.html
echo file://$PWD/docs/api/index.html
cd $DLAHOME/repos/jupyterlab && \
  yarn docs
```

## Clean

```bash
# At times, it may be necessary to clean your local repo with the command yarn run clean:slate.
# This will clean the repository, and re-install and rebuild.
yarn clean:slate
# Deletes the lib directory.
yarn clean
```

## Examples

Try the [Datalayer Lab JupyterLab examples](https://github.com/datalayer/datalayer/tree/master/lab/apps/jupyterlab).
