---
title: Kernel Gateway
---

# Kernel Gateway

[Kernel Gateway Repository](https://github.com/jupyter/kernel_gateway).

[Kernel Gateway Docs](https://jupyter-kernel-gateway.readthedocs.io).

```bash
pip install jupyter_kernel_gateway
# conda install -c conda-forge jupyter_kernel_gateway
jupyter kernelgateway --help-all
# --api='kernel_gateway.notebook_http'
# --seed_uri='x'
jupyter kernelgateway --KernelGatewayApp.ip=0.0.0.0 --KernelGatewayApp.port=8889 --port_retries=0
```

