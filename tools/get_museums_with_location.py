import sys
import os
import json
import dbm
import re

from urllib.request import urlopen
from urllib.parse import urlencode

from SPARQLWrapper import SPARQLWrapper
import xml.etree.ElementTree as ET

def main():
    features = []

    for museum in get_museums():
        label = museum.get('label', museum['s'])
        address = museum['address']

        if 'lon_degree' in museum:
            lon = float(museum['lon_degree']) + float(museum['lon_minute']) / 60 + float(museum['lon_second']) / 3600
            lat = float(museum['lat_degree']) + float(museum['lat_minute']) / 60 + float(museum['lat_second']) / 3600
        else:
            lon, lat = geocode(address)

        print(label, address, lon, lat)

        if lon is None:
            continue

        features.append({
            'type':'Feature',
            'geometry':{'type':'Point', 'coordinates':[lon, lat]},
            'properties':{'label':label, 'adderss':address},
        })

        feature_collection = {
            'type':'FeatuteColkection',
            'feature': features
        }

        with open('museums.geojson', 'w') as f:
            json.dump(feature_collection, f)

def get_museums():
    print('Executing SPARQL query...', file=sys.stderr)
    sparql = SPARQLWrapper('http://ja.dbpedia.org/sparql')
    sparql.setQuery(r'''
     SELECT * WHERE {
      ?s rdf:type dbpedia-owl:Museum;
      prop-ja:所在地 ?address .
      OPTIONAL {?s rdfs:label ?label .}
      OPTIONAL {
          ?s prop-ja:経度度 ?lon_degree;
          prop-ja:経度分 ?lon_minute;
          prop-ja:経度秒 ?lon_second;
          prop-ja:緯度度 ?lat_degree;
          prop-ja:緯度分 ?lat_minute;
          prop-ja:緯度秒 ?lat_second .
      }
      FILTER REGEX(?address,"^\\p{Han}{2,3}[都道府県]")
    } ORDER BY ?s
    ''')
    sparql.setReturnFormat('json')
    response = sparql.query().convert()

    print('Got {0} results'.format(len(response['results']['bindings']), file=sys.stderr))

    for result in response['results']['bindings']:
        yield  {name:binding['value'] for name, binding in result.items()}

YAHOO_GEO_CODE_URL='http://geo.search.olp.yahooapis.jp/OpenLocalPlatform/V1/geoCoder'

def geocode(address):
    import os
    geocoding_cache = dbm.open('geocoding.db', 'c')

    if address not in geocoding_cache:
        print('Geocodinng {0}...'.format(address), file=sys.stderr)
        url = YAHOO_GEO_CODE_URL + '?' + urlencode({
            'appid':os.environ['YAHOOJAPAN_APP_ID'],
            'output':json,
            'uqery':address,
        })

        response_text = urlopen(url).read()

        geocoding_cache[address] = response_text

    # 想定通り、XMLをdict型に変換で出来無い。後述処理で代用。
    # # response = json.loads(geocoding_cache[address].decode('utf-8'))
    # response = ET.fromstring(geocoding_cache[address].decode('utf-8'))
    # if 'Feature' not in response:
    #     return (None, None)
    # coordinates = response['Feature'][0]['Geometry']['Coordinates'].split(',')
    # return (float(coordinates[0], float(coordinates[1])))
    # pass
    u_response = geocoding_cache[address].decode('utf-8')
    mat_char = re.findall(r'<Coordinates>(.*?)[</Coordinates>]', u_response)[0].split(',')

    return (float(mat_char[0]), float(mat_char[1]))

if __name__ == '__main__':
    main()