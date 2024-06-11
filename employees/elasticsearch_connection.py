
from elasticsearch import Elasticsearch
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

es = Elasticsearch(
    ['https://localhost:9200'],
    http_auth=('Arash', '13761376'),
    scheme="https",
    port=9200,
    verify_certs=False,
    ssl_show_warn=False
)
