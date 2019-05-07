---
title: Static Site
---

# Static Site

Examples.

https://github.com/expo/expo/tree/master/docs

## Gitbook

https://github.com/GitbookIO/gitbook

## Hugo

```bash
hugo new site quickstart
cd quickstart
git init
git submodule add https://github.com/budparr/gohugo-theme-ananke.git themes/ananke
hugo new posts/my-first-post.md 
echo 'theme = "ananke"' >> config.toml
hugo server --disableFastRender
# hugo server -D
open http://localhost:1313
```

```bash
baseURL = "https://example.org"
languageCode = "en-us"
title = "My New Hugo Site"
theme = "ananke"
```

## MkDocs

[MkDocs](https://www.mkdocs.org).

Examples.

https://github.com/floydhub/floyd-docs

```bash
pip install mkdocs
mkdocs --version
mkdocs new my-project
cd my-project
mkdocs serve
```

```bash
# Add to your mkdocs.yml: theme: 'material'
pip install mkdocs-material
```

```bash
# Add to your mkdocs.yml: theme: 'alabaster'
# pip install mkdocs-alabaster
pip install git+https://github.com/notpushkin/mkdocs-alabaster
```

## Ghost

https://github.com/tryghost/ghost

## Docusaurus

https://docusaurus.io

## Vuepress

https://vuepress.vuejs.org

## Documentalist

https://palantir.github.io/documentalist/

https://github.com/palantir/documentalist

## React-based

+ https://www.gatsbyjs.org

## Vue-based

+ https://vuepress.vuejs.org

## Other

+ https://github.com/phenomic/phenomic
+ https://docsify.js.org
+ https://github.com/lord/slate
+ https://middlemanapp.com
+ https://github.com/jnordberg/wintersmith
+ https://github.com/jaredpalmer/razzle
+ https://github.com/pedronauck/docz
