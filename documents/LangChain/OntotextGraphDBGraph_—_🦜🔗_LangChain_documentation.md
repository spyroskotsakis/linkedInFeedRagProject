# OntotextGraphDBGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.ontotext_graphdb_graph.OntotextGraphDBGraph.html
**Word Count:** 427
**Links Count:** 148
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# OntotextGraphDBGraph\#

_class _langchain\_community.graphs.ontotext\_graphdb\_graph.OntotextGraphDBGraph\(

    _query\_endpoint : str_,     _query\_ontology : str | None = None_,     _local\_file : str | None = None_,     _local\_file\_format : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/ontotext_graphdb_graph.html#OntotextGraphDBGraph)\#     

Ontotext GraphDB <https://graphdb.ontotext.com/> wrapper for graph operations.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Set up the GraphDB wrapper

Parameters:     

  * **query\_endpoint** \(_str_\) – SPARQL endpoint for queries, read access

  * **query\_ontology** \(_Optional_ _\[__str_ _\]_\)

  * **local\_file** \(_Optional_ _\[__str_ _\]_\)

  * **local\_file\_format** \(_Optional_ _\[__str_ _\]_\)

If GraphDB is secured, set the environment variables ‘GRAPHDB\_USERNAME’ and ‘GRAPHDB\_PASSWORD’.

Parameters:     

  * **query\_ontology** \(_Optional_ _\[__str_ _\]_\) – a CONSTRUCT query that is executed

  * **query\_endpoint** \(_str_\)

  * **local\_file** \(_Optional_ _\[__str_ _\]_\)

  * **local\_file\_format** \(_Optional_ _\[__str_ _\]_\)

on the SPARQL endpoint and returns the KG schema statements Example: ‘CONSTRUCT \{?s ?p ?o\} FROM <<https://example.com/ontology/>> WHERE \{?s ?p ?o\}’ Currently, DESCRIBE queries like ‘PREFIX onto: <<https://example.com/ontology/>> PREFIX rdfs: <<http://www.w3.org/2000/01/rdf>-schema\#> DESCRIBE ?term WHERE \{

> ?term rdfs:isDefinedBy onto:

\}’ are not supported, because DESCRIBE returns the Symmetric Concise Bounded Description \(SCBD\), i.e. also the incoming class links. In case of large graphs with a million of instances, this is not efficient. Check [eclipse-rdf4j/rdf4j\#4857](https://github.com/eclipse-rdf4j/rdf4j/issues/4857)

Parameters:     

  * **local\_file** \(_Optional_ _\[__str_ _\]_\) – a local RDF ontology file.

  * **query\_endpoint** \(_str_\)

  * **query\_ontology** \(_Optional_ _\[__str_ _\]_\)

  * **local\_file\_format** \(_Optional_ _\[__str_ _\]_\)

Supported RDF formats: Turtle, RDF/XML, JSON-LD, N-Triples, Notation-3, Trig, Trix, N-Quads. If the rdf format can’t be determined from the file extension, pass explicitly the rdf format in local\_file\_format param.

Parameters:     

  * **local\_file\_format** \(_Optional_ _\[__str_ _\]_\) – Used if the rdf format can’t be determined

  * **query\_endpoint** \(_str_\)

  * **query\_ontology** \(_Optional_ _\[__str_ _\]_\)

  * **local\_file** \(_Optional_ _\[__str_ _\]_\)

from the local file extension. One of “json-ld”, “xml”, “n3”, “turtle”, “nt”, “trig”, “nquads”, “trix”

Either query\_ontology or local\_file should be passed.

Attributes

`get_schema` | Returns the schema of the graph database in turtle format   ---|---      Methods

`__init__`\(query\_endpoint\[, query\_ontology, ...\]\) | Set up the GraphDB wrapper   ---|---   `query`\(query\) | Query the graph.      \_\_init\_\_\(

    _query\_endpoint : str_,     _query\_ontology : str | None = None_,     _local\_file : str | None = None_,     _local\_file\_format : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/ontotext_graphdb_graph.html#OntotextGraphDBGraph.__init__)\#     

Set up the GraphDB wrapper

Parameters:     

  * **query\_endpoint** \(_str_\) – SPARQL endpoint for queries, read access

  * **query\_ontology** \(_str_ _|__None_\)

  * **local\_file** \(_str_ _|__None_\)

  * **local\_file\_format** \(_str_ _|__None_\)

Return type:     

None

If GraphDB is secured, set the environment variables ‘GRAPHDB\_USERNAME’ and ‘GRAPHDB\_PASSWORD’.

Parameters:     

  * **query\_ontology** \(_str_ _|__None_\) – a CONSTRUCT query that is executed

  * **query\_endpoint** \(_str_\)

  * **local\_file** \(_str_ _|__None_\)

  * **local\_file\_format** \(_str_ _|__None_\)

Return type:     

None

on the SPARQL endpoint and returns the KG schema statements Example: ‘CONSTRUCT \{?s ?p ?o\} FROM <<https://example.com/ontology/>> WHERE \{?s ?p ?o\}’ Currently, DESCRIBE queries like ‘PREFIX onto: <<https://example.com/ontology/>> PREFIX rdfs: <<http://www.w3.org/2000/01/rdf>-schema\#> DESCRIBE ?term WHERE \{

> ?term rdfs:isDefinedBy onto:

\}’ are not supported, because DESCRIBE returns the Symmetric Concise Bounded Description \(SCBD\), i.e. also the incoming class links. In case of large graphs with a million of instances, this is not efficient. Check [eclipse-rdf4j/rdf4j\#4857](https://github.com/eclipse-rdf4j/rdf4j/issues/4857)

Parameters:     

  * **local\_file** \(_str_ _|__None_\) – a local RDF ontology file.

  * **query\_endpoint** \(_str_\)

  * **query\_ontology** \(_str_ _|__None_\)

  * **local\_file\_format** \(_str_ _|__None_\)

Return type:     

None

Supported RDF formats: Turtle, RDF/XML, JSON-LD, N-Triples, Notation-3, Trig, Trix, N-Quads. If the rdf format can’t be determined from the file extension, pass explicitly the rdf format in local\_file\_format param.

Parameters:     

  * **local\_file\_format** \(_str_ _|__None_\) – Used if the rdf format can’t be determined

  * **query\_endpoint** \(_str_\)

  * **query\_ontology** \(_str_ _|__None_\)

  * **local\_file** \(_str_ _|__None_\)

Return type:     

None

from the local file extension. One of “json-ld”, “xml”, “n3”, “turtle”, “nt”, “trig”, “nquads”, “trix”

Either query\_ontology or local\_file should be passed.

query\(

    _query : str_, \) → List\[rdflib.query.ResultRow\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/ontotext_graphdb_graph.html#OntotextGraphDBGraph.query)\#     

Query the graph.

Parameters:     

**query** \(_str_\)

Return type:     

List\[rdflib.query.ResultRow\]

Examples using OntotextGraphDBGraph

  * [Ontotext GraphDB](https://python.langchain.com/docs/integrations/graphs/ontotext/)

__On this page