[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

:sparkles: :mega: Documentation for Datalayer. :lollipop:

The content of this repository is deployed on the [Datalayer documentation website](https://docs.datalayer.io).

## Build the Documentation

You need [gitbook](https://www.gitbook.com).

```bash
# Install gitbook and its plugins.
make env install
```

Ready to build and serve on http://localhost:4000.

```bash
# Build and Serve the documentation.
make build serve
```

To generate the PDF, you need to install [calibre](https://calibre-ebook.com).

> For MacOS, you also need to link ebook-convert with `ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/local/bin`.

```bash
# Generate a PDF - TODO Fix issue with SVG in PDF.
make pdf
```
