---
title: Kernels
---

# Kernels

[Jupyter Kernel install documentation](https://jupyter.readthedocs.io/en/latest/install-kernel.html).

```bash
python -m pip install ipykernel
python -m ipykernel install --user
```

```bash
jupyter kernelspec list
jupyter kernelspec list --json
```

```bash
jupyter kernel
# [KernelApp] Starting kernel 'python3'
# [KernelApp] Connection file: ...kernel-e0bde3c0-00e8-46c0-9e47-d01c3b9d3618.json
# [KernelApp] To connect a client: --existing kernel-e0bde3c0-00e8-46c0-9e47-d01c3b9d3618.json
```

```
jupyter kernel --help

Run a kernel locally in a subprocess

Arguments that take values are actually convenience aliases to full
Configurables, whose aliases are listed on the help line. For more information
on full configurables, see '--help-all'.

--debug
    set log level to logging.DEBUG (maximize logging output)
--kernel=<Unicode> (KernelApp.kernel_name)
    Default: 'python3'
    The name of a kernel type to start
--ip=<Unicode> (KernelManager.ip)
    Default: ''
    Set the kernel's IP address [default localhost]. If the IP address is
    something other than localhost, then Consoles on other machines will be able
    to connect to the Kernel, so be careful!

To see all available configurables, use `--help-all`
```

```bash
# ~/.local/share/jupyter/runtime/kernel-d785bbc8-c058-49d0-861c-97a39089c91e.json
# ./run/user/1000/jupyter/kernel-772af73b-185b-4960-b0fb-a0532dc59e49.json
```

[Callisto](https://github.com/colcarroll/callisto) - A command line utility to create kernels in Jupyter from virtual environments.

[Reactive Python](https://github.com/jupytercalpoly/reactivepy) - A reactive Python kernel. Whenever a variable value is changed, the kernel automatically executes its dependencies (any cells which use that variable) with the updated value. As of now, reactivepy can also support asynchronous functions.

## Share Kernel

+ https://stackoverflow.com/questions/20091154/sharing-a-namespace-across-multiple-ipython-notebooks
+ https://github.com/ipython/ipython/issues/4066
+ https://github.com/minrk/singlecell
+ https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Connecting%20with%20the%20Qt%20Console.html

## Mixed Kernels

+ https://github.com/jupyterlab/jupyterlab/issues/2815
+ https://github.com/minrk/allthekernels
+ https://vatlab.github.io/blog/post/sos-notebook
+ https://vatlab.github.io/sos-docs
