---
title: JupyterHub Configuration
---

# JupyterHub Configuration

```bash
jupyterhub --generate-config
```

```bash
jupyterhub --generate-config && \
  mv ./jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py && \
  jupyterhub -f /etc/jupyterhub/jupyterhub_config.py --Spawner.notebook_dir='~/notebooks'
```

## Used Files

+ `$DLAHOME/etc/conf/jupyterhub`: Configuration files.
+ `$DLAHOME/srv/jupyterhub`: Security and runtime files.
+ `$DLAHOME/var/log`: Log files.

## Cookie Secret

The cookie secret should be 32 random bytes, encoded as hex, and is typically stored in a `jupyterhub_cookie_secret` file. 

```bash
# Generate the jupyterhub_cookie_secret.
openssl rand -hex 32 > /srv/jupyterhub/jupyterhub_cookie_secret
# If you would like to avoid the need for files, the value can be loaded in the Hub process from the JPY_COOKIE_SECRET environment variable, which is a hex-encoded string. For security reasons, this environment variable should only be visible to the Hub. If you set it dynamically, all users will be logged out each time the Hub starts.
export JPY_COOKIE_SECRET=`openssl rand -hex 32`
```

```bash
# In most deployments of JupyterHub, you should point this to a secure location
# on the file system, such as /srv/jupyterhub/jupyterhub_cookie_secret.
# The location of the jupyterhub_cookie_secret file 
# can be specified in the jupyterhub_config.py file as follows.
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'
```

```bash
c.JupyterHub.cookie_secret = bytes.fromhex('VERY LONG SECRET HEX STRING')
```

## Proxy Authentication Token

The Hub authenticates its requests to the Proxy using a secret token that the Hub and Proxy agree upon. The value of this string should be a random string.

Default if token is not set. If you don’t set the Proxy authentication token, the Hub will generate a random key itself, which means that any time you restart the Hub you must also restart the Proxy. If the proxy is a subprocess of the Hub, this should happen automatically (this is the default configuration).

```bash
# Generate and store token in the configuration file
openssl rand -hex 32 > /srv/jupyterhub/jupyterhub_config_secret
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/cookie_secret'
# Or you can set the value in the configuration file, jupyterhub_config.py:
c.JupyterHub.proxy_auth_token = '0bc02bede919e99a26de1e2a7a5aadfaf6228de836ec39a05a6c6942831d8fe5'
# Generating and storing as an environment variable
# You can pass this value of the proxy authentication token to the Hub and Proxy using the CONFIGPROXY_AUTH_TOKEN environment variable. This environment variable needs to be visible to the Hub and Proxy.
export CONFIGPROXY_AUTH_TOKEN='openssl rand -hex 32'
```
