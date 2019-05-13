[![Datalayer](https://docs.datalayer.io/logo/datalayer-25.svg)](https://datalayer.io)

# Docker Keycloak Example

```bash
# based on https://github.com/jboss-dockerfiles/keycloak/blob/master/docker-compose-examples/keycloak-postgres.yml
docker-compose -f keycloak-postgres.yml up -d
open http://localhost:8080/auth # login as user 'admin' with password 'Pa55w0rd'.
docker-compose -f keycloak-postgres.yml down
```
