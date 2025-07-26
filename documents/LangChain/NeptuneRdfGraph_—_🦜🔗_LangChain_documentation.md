# NeptuneRdfGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/graphs/langchain_aws.graphs.neptune_rdf_graph.NeptuneRdfGraph.html
**Word Count:** 246
**Links Count:** 104
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# NeptuneRdfGraph\#

_class _langchain\_aws.graphs.neptune\_rdf\_graph.NeptuneRdfGraph\(

    _host : str_,     _port : int = 8182_,     _use\_https : bool = True_,     _use\_iam\_auth : bool = False_,     _client : Any = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_,     _service : str = 'neptunedata'_,     _sign : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/graphs/neptune_rdf_graph.html#NeptuneRdfGraph)\#     

Neptune wrapper for RDF graph operations.

Parameters:     

  * **host** \(_str_\) – endpoint for the database instance

  * **port** \(_int_\) – port number for the database instance, default is 8182

  * **use\_iam\_auth** \(_bool_\) – boolean indicating IAM auth is enabled in Neptune cluster

  * **use\_https** \(_bool_\) – whether to use secure connection, default is True

  * **client** \(_Any_\) – optional boto3 Neptune client

  * **credentials\_profile\_name** \(_str_ _|__None_\) – optional AWS profile name

  * **region\_name** \(_str_ _|__None_\) – optional AWS region, e.g., us-west-2

  * **service** \(_str_\) – optional service name, default is neptunedata

  * **sign** \(_bool_\) – optional, whether to sign the request payload, default is True

Example               

graph = NeptuneRdfGraph\(     

host=’<SPARQL host’>, port=<SPARQL port>

\) schema = graph.get\_schema\(\)

OR graph = NeptuneRdfGraph\(

> host=’<SPARQL host’>, port=<SPARQL port>

\) schema\_elem = graph.get\_schema\_elements\(\) \#… change schema\_elements … graph.load\_schema\(schema\_elem\)

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Attributes

`get_schema` | Returns the schema of the graph database.   ---|---   `get_schema_elements` |       Methods

`__init__`\(host\[, port, use\_https, ...\]\) |    ---|---   `get_summary`\(\) | Obtain Neptune statistical summary of classes and predicates in the graph.   `load_schema`\(schema\_elements\) | Generates and sets schema from schema\_elements.   `query`\(query\) | Run Neptune query.      \_\_init\_\_\(

    _host : str_,     _port : int = 8182_,     _use\_https : bool = True_,     _use\_iam\_auth : bool = False_,     _client : Any = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_,     _service : str = 'neptunedata'_,     _sign : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/graphs/neptune_rdf_graph.html#NeptuneRdfGraph.__init__)\#     

Parameters:     

  * **host** \(_str_\)

  * **port** \(_int_\)

  * **use\_https** \(_bool_\)

  * **use\_iam\_auth** \(_bool_\)

  * **client** \(_Any_\)

  * **credentials\_profile\_name** \(_str_ _|__None_\)

  * **region\_name** \(_str_ _|__None_\)

  * **service** \(_str_\)

  * **sign** \(_bool_\)

Return type:     

None

get\_summary\(\) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/graphs/neptune_rdf_graph.html#NeptuneRdfGraph.get_summary)\#     

Obtain Neptune statistical summary of classes and predicates in the graph.

Return type:     

_Dict_\[str, _Any_\]

load\_schema\(

    _schema\_elements : Dict\[str, Any\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/graphs/neptune_rdf_graph.html#NeptuneRdfGraph.load_schema)\#     

Generates and sets schema from schema\_elements. Helpful in cases where introspected schema needs pruning.

Parameters:     

**schema\_elements** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

None

query\(

    _query : str_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/graphs/neptune_rdf_graph.html#NeptuneRdfGraph.query)\#     

Run Neptune query.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_\[str, _Any_\]

Examples using NeptuneRdfGraph

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [Amazon Neptune with SPARQL](https://python.langchain.com/docs/integrations/graphs/amazon_neptune_sparql/)

__On this page