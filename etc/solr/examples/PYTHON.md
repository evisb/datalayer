# Solr with Python

## Python Tutorials

+ https://www.zylk.net/en/web-2-0/blog/-/blogs/solr-client-apis
+ https://medium.com/@avremelk/solr-gottchas-a-tutorial-a953c8b3e775
+ https://github.com/avremel/Solr-Python-Tutorial
+ https://lucidworks.com/2013/06/13/indexing-web-sites-in-solr-with-python

## PySolr

```bash
# https://github.com/django-haystack/pysolr
pip install pysolr kazoo simplejson
export DEBUG_PYSOLR=true
```

```python
import pysolr
pysolr.ZooKeeper.CLUSTER_STATE = '/collections/demo/state.json'
pysolr.ZooKeeper.CLUSTER_STATE = '/collections/datalayer/state.json'
# For SolrCloud mode, initialize your Solr like this:
zookeeper = pysolr.ZooKeeper("zk:2181")
# solr = pysolr.SolrCloud(zookeeper, "datalayer", results_cls=dict, always_commit=True)
solr = pysolr.SolrCloud(zookeeper, "demo", always_commit=True)
solr = pysolr.SolrCloud(zookeeper, "datalayer", always_commit=True)
# Setup a Solr instance. The timeout is optional.
# solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)
# Do a health check.
solr.ping() # In dev source code.
# How you'd index data.
solr.add([{
        "id": "doc_1",
        "title": "A test document",
        "tweet_id": "asdf",
        "tweet_text": "asdf",
        "tweet_capture_bin": "dGVzdA==",
    },
    {
        "id": "doc_2",
        "title": "The Banana: Tasty or Dangerous?",
        "tweet_id": "asdf",
        "tweet_text": "asdf",
        "tweet_capture_bin": "dGVzdA==",
        "_childDocuments_": [
            { 
                "id": "child_doc_1", 
                "title": "peel",
                "tweet_id": "asdf",
                "tweet_text": "asdf",
                "tweet_capture_bin": "dGVzdA==" 
            },
            { 
                "id": "child_doc_2", 
                "title": "seed",
                "tweet_id": "asdf",
                "tweet_text": "asdf",
                "tweet_capture_bin": "dGVzdA=="
            },
        ]
    }],
    commit=True
    )
# Note that the add method has commit=True by default, so this is immediately committed to your index.
# You can index a parent/child document relationship by associating a list of child documents with the special key '_childDocuments_'.
# This is helpful for queries that join together conditions on children and parent documents.
# Later, searching is easy. In the simple case, just a plain Lucene-style query is fine.
results = solr.search('bananas')
results = solr.search('title:seed')
results = solr.search('title:*')
solr.search('title:*RO*', **{'rows': 0, 'start':5, 'sort':'id DESC'})
# The ``Results`` object stores total results found, by default the top
# ten most relevant results and any additional data like facets/highlighting/spelling/etc.
print("Found {} result(s).".format(len(results)))
# Just loop over it to access the results.
def print_results(results):
    for result in results:
        print("Title: {} - Capture: {}".format(result['title'], result.get('capture_bin', None)))

print_results(results)
# For a more advanced query, say involving highlighting, you can pass additional options to Solr.
results = solr.search('title:banana', **{
    'hl': 'true',
    'hl.fragsize': 10,
})
print_results(results)
list(map(lambda r: r, results))
# Update.
doc_1 = {'id':'doc_1', 'title':'now half off!'}
solr.add([doc_1], fieldUpdates={'title': 'set'})
print_results(solr.search('title:half'))
# You can also perform More Like This searches, if your Solr is configured correctly.
similar = solr.more_like_this(q='id:doc_2', mltfl='text')

from io import StringIO
html = StringIO("""
    <html>
        <head>
            <meta charset="utf-8">
            <meta name="haystack-test" content="test 1234">
            <title>Test Title ☃&#x2603;</title>
        </head>
            <body>foobar</body>
    </html>
""")
html.name = "test.html"
extracted = solr.extract(html, extractOnly=False)
print(extracted)
print(extracted['contents'])
print(extracted['metadata'])

# Finally, you can delete either individual documents.
solr.delete(id='doc_1')
# also in batches...
solr.delete(id=['doc_1', 'doc_2'])
# ...or all documents.
solr.delete(q='*:*', commit=True)
```

## Other Python Clients

+ https://github.com/solrcloudpy/solrcloudpy
+ https://github.com/tow/sunburnt
+ https://github.com/moonlitesolutions/SolrClient
+ https://github.com/swistakm/solrq
+ https://github.com/avremel/Solr-Python-Tutorial
+ https://lucene.apache.org/solr/guide/7_1/using-python.html
