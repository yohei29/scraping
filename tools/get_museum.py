from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper('http://ja.dbpedia.org/sparql')
sparql.setQuery(r'''
    select * where {
    ?s rdf:type dbpedia-owl:Museum .
    ?s prop-ja:所在地 ?address .
    FILTER REGEX(?address, "^\\p{Han}{2,3}[都道府県]")
  } ORDER BY ?s
  ''')

sparql.setReturnFormat('json')
res = sparql.query().convert()

for res in res['results']['bindings']:
    print(res['s']['value'], res['address']['value'])