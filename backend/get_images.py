import glob
import numpy
import json
import urllib.request
import csv
from hashlib import md5
import os
import requests
import shutil


def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        print("error")

odir = "data/images"

collection_url = "https://nakamura196.github.io/lda2/collections_all.json"

response = urllib.request.urlopen(collection_url)
response_body = response.read().decode("utf-8")
collection = json.loads(response_body)

collections = collection["collections"]

thumbs = {}
thumb_array = []

for i in range(len(collections)):
    print(i)
    collection_url = collections[i]["@id"]

    print(collection_url)

    response = urllib.request.urlopen(collection_url)
    response_body = response.read().decode("utf-8")
    tmp = json.loads(response_body)

    manifests = tmp["manifests"]

    #################

    for manifest in manifests:

        thumbnail = manifest["thumbnail"]
        if thumbnail not in thumb_array:
            thumb_array.append(thumbnail)

        id = manifest["@id"]

        hash = md5(id.encode('utf-8')).hexdigest()

        thumbnail = thumbnail.replace("/,300/", "/,600/")

        path = odir+"/"+hash+".jpg"
        
        if not os.path.exists(path):
            print(id)
            download_img(thumbnail, path)

        thumbs[hash] = thumbnail

with open('data/thumbs_list.json', 'w') as outfile:
    json.dump(thumbs, outfile, ensure_ascii=False,
              sort_keys=True, separators=(',', ': '))

print("画像総数：")
print(len(thumb_array))
