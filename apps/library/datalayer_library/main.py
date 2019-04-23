import os, json, logging, datetime, uuid

from flask import Flask, g, send_from_directory, jsonify, request, redirect
from flask_oidc import OpenIDConnect
from flask_cors import CORS

from datalayer_library.library import index_tweet, search_tweets

logging.basicConfig(level=logging.DEBUG)

ROOT_FOLDER='./..'
OIDC_CLIENT_SECRETS= os.getenv('HOME') + '/.datalayer/oidc.json'
PORT = 9800

app = Flask(__name__, static_folder = ROOT_FOLDER)

app.logger.setLevel(logging.DEBUG)

app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'TESTING': False,
    'DEBUG': False,
    'OIDC_CLIENT_SECRETS': OIDC_CLIENT_SECRETS,
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'datalayer',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OVERWRITE_REDIRECT_URI': os.getenv('DLA_Library_AUTH_CALLBACK'),
})

CORS(app, supports_credentials = True)
oidc = OpenIDConnect(app)
oidc_conf = None

@app.route('/library')
@app.route('/library/')
def show_index():
    return '<h1>Datalayer Library</h1>'

@app.route('/library/index', methods=['POST'])
@oidc.require_login
def get_index_tweet():
    post = request.get_json()
    post['tweet_date'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    post['id'] = str(uuid.uuid4())
    index_tweet(post)
    return jsonify({
        'success': True,
    })

@app.route('/library/search', methods=['GET'])
def get_search_tweets():
    q = request.args.get('q')
    results = search_tweets(q)
    j = list(map(lambda r: r, results))
    return jsonify({
        'success': True,
        'results': j,
    })
"""
@app.route('/library/delete', methods=['GET'])
def delete(id):
    if oidc.user_loggedin:
        solr.delete(id=id)
        return jsonify({
            'success': True,
            'results': j,
        })
    else:
        return jsonify({ 'success': False })
"""
@app.route('/library/logout')
def logout():
    """Performs local logout by removing the session cookie."""
    oidc.logout()
    return jsonify({ 'success': True })

def init():
    csr = open(OIDC_CLIENT_SECRETS, 'r')
    global oidc_conf
    oidc_conf = json.load(csr)
    oidc_conf['web']['client_secret'] = os.getenv('DLA_KEYCLOAK_REALM_CLIENT_SECRET')
    with open(OIDC_CLIENT_SECRETS, 'w') as csw:
        json.dump(oidc_conf, csw, indent=4, sort_keys=True)

if __name__ == '__main__':
    init()
    logging.info('Server listening on port {} - Browse http://localhost:{}'.format(PORT, PORT))
    app.run(
        host='0.0.0.0', 
        port = PORT,
        threaded = True,
        processes = 1,
        )
