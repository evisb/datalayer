"""

jupyterhub -f $DLAHOME/etc/jupyterhub/examples/keycloak-docker/jupyterhub_config.py
open http://localhost:8000

Working configuration for generic authenticator with Keycloak https://github.com/jupyterhub/oauthenticator/issues/107

https://github.com/matipp/oauthenticator/tree/keycloak_auth/oauthenticator
https://github.com/matipp/oauthenticator/tree/keycloak/oauthenticator
https://github.com/matipp/oauthenticator/commit/326d2617ce09749ca0c4d9a19e9651fe437e1755

https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues/886
https://github.com/jupyterhub/jupyterhub/issues/2045
https://github.com/jupyter-on-openshift/poc-hub-openshift-auth

https://github.com/jupyterhub/oauthenticator/pull/183
https://github.com/jupyterhub/jupyterhub/issues/1805

"""

"""
Custom Authenticator to use Keycloak OAuth with JupyterHub.
Most of the code c/o Kyle Kelley (@rgbkrk).
"""
import json, os, urllib

from tornado.auth import OAuth2Mixin
from tornado import gen, web
from tornado.httputil import url_concat
from tornado.httpclient import HTTPRequest, AsyncHTTPClient

from jupyterhub.auth import LocalAuthenticator
from jupyterhub.handlers import LogoutHandler
from jupyterhub.utils import url_path_join

from oauthenticator.oauth2 import OAuthLoginHandler, OAuthenticator

class KeycloakMixin(OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = os.getenv('KEYCLOAK_AUTH_URL', "http://localhost:8092/auth/realms/datalayer/protocol/openid-connect/auth")
    _OAUTH_ACCESS_TOKEN_URL = os.getenv('KEYCLOAK_TOKEN_URL', "http://localhost:8092/auth/realms/datalayer/protocol/openid-connect/token")
    _OAUTH_LOGOUT_URL = os.getenv('KEYCLOAK_LOGOUT_URL', "http://localhost:8092/auth/realms/datalayer/protocol/openid-connect/logout")
    _OAUTH_USERINFO_URL = os.getenv('KEYCLOAK_USERINFO_URL', "http://localhost:8092/auth/realms/datalayer/protocol/openid-connect/userinfo")

class KeycloakLoginHandler(OAuthLoginHandler, KeycloakMixin):
    pass

class KeycloakLogoutHandler(LogoutHandler, KeycloakMixin):
    def get(self):
        params = dict(
            redirect_uri="%s://%s%slogout" % (
                self.request.protocol, self.request.host,
                self.hub.server.base_url)
        )
        logout_url = KeycloakMixin._OAUTH_LOGOUT_URL
        logout_url = url_concat(logout_url, params)
        self.redirect(logout_url, permanent=False)

class KeycloakOAuthenticator(OAuthenticator, KeycloakMixin):
    login_service = "Datalayer"
    login_handler = KeycloakLoginHandler

    def logout_url(self, base_url):
        return url_path_join(base_url, 'oauth_logout')

    def get_handlers(self, app):
        handlers = OAuthenticator.get_handlers(self, app)
        handlers.extend([(r'/oauth_logout', KeycloakLogoutHandler)])
        return handlers

    @gen.coroutine
    def authenticate(self, handler, data=None):
        code = handler.get_argument("code", False)
        if not code:
            raise web.HTTPError(400, "oauth callback made without a token")

        http_client = AsyncHTTPClient()

        params = dict(
            grant_type='authorization_code',
            code=code,
            redirect_uri=self.get_callback_url(handler),
        )

        tokenUrl = KeycloakMixin._OAUTH_ACCESS_TOKEN_URL

        tokenReq = HTTPRequest(
            tokenUrl,
            method="POST",
            headers={
                "Accept": "application/json",
                 "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
            },
            auth_username = self.client_id,
            auth_password = self.client_secret,
            body = urllib.parse.urlencode(params).encode('utf-8'),
            )

        tokenResp = yield http_client.fetch(tokenReq)
        tokenResp_json = json.loads(tokenResp.body.decode('utf8', 'replace'))
        access_token = tokenResp_json['access_token']
        if not access_token:
            raise web.HTTPError(400, "failed to get access token")

        self.log.info('oauth token: %r', access_token)
        userInfoUrl = KeycloakMixin._OAUTH_USERINFO_URL
        userInfoReq = HTTPRequest(
            userInfoUrl,
            method="GET",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer %s" % access_token
                },
            )
        userInfoResp = yield http_client.fetch(userInfoReq)
        userInfoResp_json = json.loads(
            userInfoResp.body.decode('utf8', 'replace'))

        return userInfoResp_json['preferred_username']

class LocalKeycloakOAuthenticator(LocalAuthenticator, KeycloakOAuthenticator):
    """A version that mixes in local system user creation"""
    pass

c.JupyterHub.base_url = '/jupyterlab'

# --- Proxy ---
c.ConfigurableHTTPProxy.api_url  = 'http://localhost:8002'

# --- Common ---
c.JupyterHub.cookie_secret = bytes.fromhex('c336ff8bc0f477928cfc73454821ee11182e90a49de57f81e0919e66851349c6')
c.JupyterHub.confirm_no_ssl = True
c.ConfigurableHTTPProxy.auth_token = '0bc02bede919e99a26de1e2a7a5aadfaf6228de836ec39a05a6c6942831d8fe5'

# --- Users ---
c.Authenticator.admin_users = { os.environ['USER'] }
c.Authenticator.whitelist = set()

# --- Authenticator ---
# os.environ["OAUTH2_AUTHORIZE_URL"] = "http://localhost:8092/auth/realms/datalayer/protocol/openid-connect/auth"
# os.environ["OAUTH2_TOKEN_URL"] = "http://localhost:8092/auth/realms/datalayer/protocol/openid-connect/token"
c.JupyterHub.authenticator_class = KeycloakOAuthenticator
c.KeycloakOAuthenticator.client_id = 'datalayer'
c.KeycloakOAuthenticator.client_secret = os.getenv('DLA_KEYCLOAK_REALM_CLIENT_SECRET')
c.Authenticator.auto_login = False
c.LocalAuthenticator.create_system_users = True

# c.OAuthenticator.client_id = 'datalayer' # oauth2 client id for your app.
# c.OAuthenticator.client_secret = os.getenv('DLA_KEYCLOAK_REALM_CLIENT_SECRET') # oauth2 client secret for your app.

# --- Spawner ---
from dockerspawner import DockerSpawner
c.JupyterHub.spawner_class = DockerSpawner
c.DockerSpawner.image = 'jupyterhub/singleuser:0.9'
c.DockerSpawner.default_url = '/lab'
c.Spawner.cmd = ['jupyter-labhub']
# The docker instances need access to the Hub, so the default loopback port doesn't work:
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
