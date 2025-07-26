# RdfGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.rdf_graph.RdfGraph.html
**Word Count:** 333
**Links Count:** 147
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# RdfGraph\#

_class _langchain\_community.graphs.rdf\_graph.RdfGraph\(

    _source\_file : str | None = None_,     _serialization : str | None = 'ttl'_,     _query\_endpoint : str | None = None_,     _update\_endpoint : str | None = None_,     _standard : str | None = 'rdf'_,     _local\_copy : str | None = None_,     _graph\_kwargs : Dict | None = None_,     _store\_kwargs : Dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/rdf_graph.html#RdfGraph)\#     

RDFlib wrapper for graph operations.

Modes: \* local: Local file - can be queried and changed \* online: Online file - can only be queried, changes can be stored locally \* store: Triple store - can be queried and changed if update\_endpoint available Together with a source file, the serialization should be specified.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Set up the RDFlib graph

Parameters:     

  * **source\_file** \(_Optional_ _\[__str_ _\]_\) – either a path for a local file or a URL

  * **serialization** \(_Optional_ _\[__str_ _\]_\) – serialization of the input

  * **query\_endpoint** \(_Optional_ _\[__str_ _\]_\) – SPARQL endpoint for queries, read access

  * **update\_endpoint** \(_Optional_ _\[__str_ _\]_\) – SPARQL endpoint for UPDATE queries, write access

  * **standard** \(_Optional_ _\[__str_ _\]_\) – RDF, RDFS, or OWL

  * **local\_copy** \(_Optional_ _\[__str_ _\]_\) – new local copy for storing changes

  * **graph\_kwargs** \(_Optional_ _\[__Dict_ _\]_\) – Additional rdflib.Graph specific kwargs

  * **store\_kwargs** \(_Optional_ _\[__Dict_ _\]_\)

that will be used to initialize it, if query\_endpoint is provided. :param store\_kwargs: Additional sparqlstore.SPARQLStore specific kwargs that will be used to initialize it, if query\_endpoint is provided.

Attributes

`get_schema` | Returns the schema of the graph database.   ---|---      Methods

`__init__`\(\[source\_file, serialization, ...\]\) | Set up the RDFlib graph   ---|---   `load_schema`\(\) | Load the graph schema information.   `query`\(query\) | Query the graph.   `update`\(query\) | Update the graph.      \_\_init\_\_\(

    _source\_file : str | None = None_,     _serialization : str | None = 'ttl'_,     _query\_endpoint : str | None = None_,     _update\_endpoint : str | None = None_,     _standard : str | None = 'rdf'_,     _local\_copy : str | None = None_,     _graph\_kwargs : Dict | None = None_,     _store\_kwargs : Dict | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/rdf_graph.html#RdfGraph.__init__)\#     

Set up the RDFlib graph

Parameters:     

  * **source\_file** \(_str_ _|__None_\) – either a path for a local file or a URL

  * **serialization** \(_str_ _|__None_\) – serialization of the input

  * **query\_endpoint** \(_str_ _|__None_\) – SPARQL endpoint for queries, read access

  * **update\_endpoint** \(_str_ _|__None_\) – SPARQL endpoint for UPDATE queries, write access

  * **standard** \(_str_ _|__None_\) – RDF, RDFS, or OWL

  * **local\_copy** \(_str_ _|__None_\) – new local copy for storing changes

  * **graph\_kwargs** \(_Dict_ _|__None_\) – Additional rdflib.Graph specific kwargs

  * **store\_kwargs** \(_Dict_ _|__None_\)

Return type:     

None

that will be used to initialize it, if query\_endpoint is provided. :param store\_kwargs: Additional sparqlstore.SPARQLStore specific kwargs that will be used to initialize it, if query\_endpoint is provided.

load\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/rdf_graph.html#RdfGraph.load_schema)\#     

Load the graph schema information.

Return type:     

None

query\(_query : str_\) → List\[rdflib.query.ResultRow\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/rdf_graph.html#RdfGraph.query)\#     

Query the graph.

Parameters:     

**query** \(_str_\)

Return type:     

List\[rdflib.query.ResultRow\]

update\(_query : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/rdf_graph.html#RdfGraph.update)\#     

Update the graph.

Parameters:     

**query** \(_str_\)

Return type:     

None

Examples using RdfGraph

  * [RDFLib](https://python.langchain.com/docs/integrations/graphs/rdflib_sparql/)

__On this page