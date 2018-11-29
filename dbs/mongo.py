import sys
sys.path.append("../..")

from scraping.cnst import cmn
import lxml.html
from pymongo import MongoClient

tree = lxml.html.parse(cmn.HTML_DIR + 'index.html')
html = tree.getroot()

client = MongoClient('localhost')
db = client.scraping
collection = db.links

collection.delete_many({})

for a in html.cssselect('a'):
    collection.insert_one({
        'url':a.get('href'),
        'title':a.text,
    })

for link in collection.find().sort('_id'):
    # print(link['_id'], link['url'], link['title'])
    pass

print('ok')