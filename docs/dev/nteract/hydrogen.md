---
title: Nteract Hydrogen
---

# Nteract Hydrogen

[Hydrogen Documentation](https://nteract.gitbooks.io/hydrogen).

[Hydrogen Source Code](https://github.com/nteract/hydrogen).

[Nteract Web Site](https://nteract.io/atom).

```bash
apm install hydrogen
```

```bash
cd $DLAHOME/repos/nteract-hydrogen
yarn install
# If I add `hydrogen:hot-reload-package` to `activationCommands` in `package.json`, it shows up, but then it also shows up when not in dev mode.
# Since it's not an activation command, hydrogen will need to be active before you can use it. That said, I've never been sure how that command works so I usually just reload window any time I want to refresh.
# And if I'm doing that a lot during development I write a test to at least make sure things will load.
```

Install the [nteract kernels](/dev/nteract/kernels.md).

[No kernel for language python found` on Hydrogen run command](https://github.com/nteract/hydrogen/issues/243)

## Visual Studio Code

https://github.com/nteract/hydrogen/issues/449

https://github.com/DonJayamanne/vscodejupyter

## Plugins

https://github.com/lgeiger/hydrogen-launcher
https://github.com/nikitakit/hydrogen-python
https://github.com/BenRussert/data-explorer
https://atom.io/packages/hydrogen-python
