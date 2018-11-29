import requests
import lxml.html
import re
import time
from pymongo import MongoClient

def main():
    # mongo
    cli = MongoClient('localhost')
    coll = cli.scraping.ebooks
    coll.create_index('key', unique=True)

    # scraping
    ses = requests.Session()

    res = ses.get('https://gihyo.jp/dp')
    urls = sc_lsit(res)

    for u in urls:

        key = extract_key(u)
        ebook = coll.find_one({'key': key})

        if not ebook:
            time.sleep(1)
            res = ses.get(u)
            ebook = sc_detali(res)
            coll.insert_one(ebook)
            print('registration ->', ebook['url'])

def sc_detali(res):
    root = lxml.html.fromstring(res.content)
    ebook = {
        'key' : extract_key(res.url),
        'url' : res.url,
        'title' : root.cssselect('#bookTitle')[0].text_content(),
        'price' : root.cssselect('.buy')[0].text.strip(),
        'content' : [norm_spaces( h3.text_content() ) for h3 in root.cssselect('#content > h3')],
    }

    return ebook

def norm_spaces(s):
    return re.sub(r'\s+', '', s).strip()

def extract_key(url):
    m = re.search(r'/([^/]+)$', url)
    return m.group(1)

def sc_lsit(res):
    root = lxml.html.fromstring(res.content)
    root.make_links_absolute(res.url)

    for v in root.cssselect('#listBook a[itemprop="url"]'):
        url = v.get('href')
        yield url

if __name__ == '__main__':
    main()