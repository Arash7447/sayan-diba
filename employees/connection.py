from elasticsearch import Elasticsearch

es = Elasticsearch(['https://localhost:9200'], verify_certs=False)