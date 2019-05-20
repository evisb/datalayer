[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

# Keycloak Examples

> Federation with Keycloak, a `OAuth 2.0` and `OpenID Connect` provider.

```bash
cd $DLAHOME/etc/keycloak/examples && \
  docker-compose -f keycloak.yml up -d && \
  docker-compose -f keycloak.yml ps && \
  sleep 3s && \
  ldapadd -x -D "cn=admin,dc=datalayer,dc=io" -w admin -H ldap:// -f entries-1.ldif && \
  ldapsearch -x -D "cn=admin,dc=datalayer,dc=io" \
    -w admin -H ldap://localhost:389 \
    -b "ou=users,dc=datalayer,dc=io" \
    -s sub "(uid=*)"
# password is `123`
ldapadd -x -D "cn=admin,dc=datalayer,dc=io" -w admin -H ldap:// -f entries-2.ldif
```

```bash
# Browse and login to keycloak.
open http://localhost:8080 # admin / admin
```

+ Create a new Realm `datalayer`.
+ Create the client `datalayer` with Root URL `http://localhost:8080`.
  + Valid Redirect URIs to `http://localhost:8080/*`.
  + Access Type to `confidential`.
  + Go to Credentials tab an copy the value on Secret field.
+ Create the client `jupyterhub` the same way.
+ Go to Roles tab and add a `user` role.
+  Click on the User Federation, select ldap.
  + Set Vendor field to `Other`.
  + Connection URL type `ldap://ldap`.
  + Users DN type `ou=users,dc=datalayer,dc=io`.
  + Bind DN type `cn=admin,dc=datalayer,dc=io`.
  + Bind Credential set `admin`.
+ Click on `Synchronize all users` and check they are available via the Users management menu (view all users).

```bash
open http://localhost:8080/auth/admin/master/console
open http://localhost:8080/auth/realms/datalayer/account
```

```bash
export CLIENT_SECRET=$DLA_KEYCLOAK_REALM_CLIENT_SECRET
ACCESS_TOKEN=$(curl -s -X POST \
  "http://localhost:8080/auth/realms/datalayer/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=echarles" \
  -d "password=123" \
  -d "grant_type=password" \
  -d "client_secret=$CLIENT_SECRET" \
  -d "client_id=datalayer" | jq -r .access_token)
echo $ACCESS_TOKEN
```

```bash
docker-compose -f keycloak.yml down
```

## Integrations

You are now ready to integrate.

+ [JupyterHub](./jupyterhub).
+ [Java with LDAP and Swagger](./java).
+ [Python](./py).
+ [Go](./go).
+ [Node.js](./node).

See also [question on mailing list](http://lists.jboss.org/pipermail/keycloak-user/2014-September/000928.html).

## Info on URLs

+ http://localhost:8080/auth/realms/datalayer
+ http://localhost:8080/auth/realms/datalayer/.well-known/openid-configuration
+ http://keycloakhost:keycloakport/auth/realms/{realm}/.well-known/openid-configuration

## About Login

+ https://www.keycloak.org/docs/3.2/server_admin/topics/login-settings.html
+ https://www.keycloak.org/docs/3.2/server_admin/topics/authentication.html
+ http://localhost:8080/auth/realms/datalayer/account

## About Theming

+ https://www.keycloak.org/docs/3.2/server_development/topics/themes.html
+ https://github.com/keycloak/keycloak/tree/master/examples/themes
+ https://medium.com/@auscunningham/create-a-custom-theme-for-keycloak-8781207be604
+ https://github.com/austincunningham/raincatcher-keycloak-theme
+ https://github.com/Alfresco/alfresco-keycloak-theme
+ https://github.com/eclipse/che/issues/6116
