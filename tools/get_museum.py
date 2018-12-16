from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper('http://ja.dbpedia.org/sparql')
sparql.setQuery(r'''
    select * where {
    ?s rdf:type dbpedia-owl:Museum .
    ?s prop-ja:所在地 ?address .
    FILTER REGEX(?address, "^\\p{Han}{2,3}[都道府県]")
  } ORDER BY ?s
  ''')
# 緯度経度の情報も取得
# sparql.setQuery(r'''
#  SELECT * WHERE {
#   ?s rdf:type dbpedia-owl:Museum;
#   prop-ja:所在地 ?address .
#   OPTIONAL {?s rdfs:label ?label .}
#   OPTIONAL {
#       ?s prop-ja:経度度 ?lon_degree;
#       prop-ja:経度分 ?lon_minute;
#       prop-ja:経度秒 ?lon_second;
#       prop-ja:緯度度 ?lat_degree;
#       prop-ja:緯度分 ?lat_minute;
#       prop-ja:緯度秒 ?lat_second .
#   }
#   FILTER REGEX(?address, "^\\p{Han}{2, 3}[都道府県]")
# } ORDER BY ?s
# ''')

sparql.setReturnFormat('json')
res = sparql.query().convert()

for res in res['results']['bindings']:
    print(res['s']['value'], res['address']['value'])