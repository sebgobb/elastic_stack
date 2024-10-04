from pprint import pprint
from elasticsearch import Elasticsearch

username = 'elastic'
password = 'elastic'

client = Elasticsearch(
    "http://localhost:9200",
    basic_auth=(username, password)
)

# INDEXING A DOCUMENT
doc = {
    'author': 'author_name',
    'text': 'Interesting content...',
    'timestamp': datetime.now(),
}
resp = client.index(index="test-index", id=1, document=doc)
print(resp['result'])


# GETTING A DOCUMENT
resp = client.get(index="test-index", id=1)
pprint(resp['_source'])


# REFRESHING AN INDEX
client.indices.refresh(index="test-index")


# SEARCHING FOR A DOCUMENT
resp = client.search(index="test-index", query={"match_all": {}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


# UPDATING A DOCUMENT
doc = {
    'author': 'author_name',
    'text': 'Interesting modified content...',
    'timestamp': datetime.now(),
}
resp = client.update(index="test-index", id=1, doc=doc)
print(resp['result'])
