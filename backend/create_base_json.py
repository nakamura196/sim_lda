import json
from SPARQLWrapper import SPARQLWrapper
from hashlib import md5
import urllib.request
import glob


collection_url = "https://nakamura196.github.io/lda2/collections_all.json"

response = urllib.request.urlopen(collection_url)
response_body = response.read().decode("utf-8")
collections = json.loads(response_body)

collections = collections["collections"]

map = {}

for i in range(len(collections)):
    print(i)
    collection_url = collections[i]["@id"]

    print(collection_url)

    response = urllib.request.urlopen(collection_url)
    response_body = response.read().decode("utf-8")
    collection = json.loads(response_body)

    manifests = collection["manifests"]

    #################

    for manifest in manifests:

        thumbnail = manifest["thumbnail"]

        id = manifest["@id"]

        hash = md5(id.encode('utf-8')).hexdigest()

        map[hash] = {
            "thumbnail": thumbnail,
            "id": hash,
            "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest="+id,
            "label": manifest["label"],
            "metadata": [
                {
                    "label": "機関",
                    "value": collection["label"]
                }
            ]
        }


fw2 = open("data/base.json", 'w')
json.dump(map, fw2, ensure_ascii=False, indent=4,
          sort_keys=True, separators=(',', ': '))
