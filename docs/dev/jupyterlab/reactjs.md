---
title: JupyterLab React.js
---

# JupyterLab React.js

## Pull Requests

[Track migration to ui-components](https://github.com/jupyterlab/jupyterlab/issues/5702).

[[WIP] Add @jupyterlab/ui-components package](https://github.com/jupyterlab/jupyterlab/pull/5538).

[Figure out if tree shaking is working with blueprint](https://github.com/jupyterlab/jupyterlab/issues/5601).

[Create a @jupyterlab/ui package based on Blueprint and possibly Material UI](https://github.com/jupyterlab/jupyterlab/issues/5170).

[Add ui package and refactor toolbars](https://github.com/jupyterlab/jupyterlab/pull/4234).

## Architecture

[React component for a button - It knows nothing about phospohr or signals](https://github.com/jupyterlab/jupyterlab/blob/master/packages/apputils/src/toolbar.tsx#L375).

[Phosphor widget that wraps the previous button and takes the exact same props](https://github.com/jupyterlab/jupyterlab/blob/master/packages/apputils/src/toolbar.tsx#L401).

[A bit awkward to manage the transition between signals and props, see a component that does that](https://github.com/jupyterlab/jupyterlab/blob/master/packages/apputils/src/toolbar.tsx#L432).

> I am imagining that as we do more of these things, we will start to see the patterns and can build more logic to make it easy.  In general though, we are trying to keep phosphor stuff out of our react components, so they are truly reusable.
