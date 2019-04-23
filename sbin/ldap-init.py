#!/usr/bin/env python3

# Licensed to Datalayer (https://datalayer.io) under one or more
# contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. Datalayer licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import ldap3, os
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE, HASHED_SALTED_SHA
from ldap3.utils.hashed import hashed

print('Connecting to LDAP server {0}'.format(os.environ['DATALAYER_LDAP_HOST']))
server = Server(
    os.environ['DATALAYER_LDAP_HOST'], 
    get_info=ALL,
    )
conn = Connection(
    server, 
    os.environ['DATALAYER_LDAP_BIND'], 
    os.environ['DATALAYER_LDAP_BIND_PWD'], 
    auto_bind=True
    )

dn = 'ou=users,dc=datalayer,dc=io'
print('Adding dn {0}'.format(dn))
server.schema.object_classes['organizationalUnit']
conn.add(dn, 'organizationalUnit')

server.schema.object_classes['inetOrgPerson']

hashed_password = hashed(HASHED_SALTED_SHA, os.environ['DATALAYER_PWD'])

def add_user(user):
    print('Adding user {0}'.format(user))
    conn.add(user, 'inetOrgPerson', {'sn': 'datalayer', 'mail': 'info@datalayer.io'})
    conn.modify(user, {'userPassword': [(MODIFY_REPLACE, [hashed_password])]})

add_user('cn=datalayer,ou=users,dc=datalayer,dc=io')
add_user('cn=admin,ou=users,dc=datalayer,dc=io')
