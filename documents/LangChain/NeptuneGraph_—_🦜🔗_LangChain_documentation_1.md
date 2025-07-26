# NeptuneGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.neptune_graph.NeptuneGraph.html
**Word Count:** 199
**Links Count:** 140
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# NeptuneGraph\#

_class _langchain\_community.graphs.neptune\_graph.NeptuneGraph\(

    _host : str_,     _port : int = 8182_,     _use\_https : bool = True_,     _client : Any = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_,     _sign : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/neptune_graph.html#NeptuneGraph)\#     

Deprecated since version 0.3.15: Use `:class:`~langchain_aws.NeptuneGraph`` instead. It will not be removed until langchain-community==1.0.

Neptune wrapper for graph operations.

Parameters:     

  * **host** \(_str_\) – endpoint for the database instance

  * **port** \(_int_\) – port number for the database instance, default is 8182

  * **use\_https** \(_bool_\) – whether to use secure connection, default is True

  * **client** \(_Any_\) – optional boto3 Neptune client

  * **credentials\_profile\_name** \(_str_ _|__None_\) – optional AWS profile name

  * **region\_name** \(_str_ _|__None_\) – optional AWS region, e.g., us-west-2

  * **sign** \(_bool_\) – optional, whether to sign the request payload, default is True

Example               

graph = NeptuneGraph\(     

host=’<my-cluster>’, port=8182

\)

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new Neptune graph wrapper instance.

Attributes

`get_schema` | Return the schema of the Neptune database   ---|---      Methods

`__init__`\(host\[, port, use\_https, client, ...\]\) | Create a new Neptune graph wrapper instance.   ---|---   `query`\(query\[, params\]\) | Query Neptune database.      \_\_init\_\_\(

    _host : str_,     _port : int = 8182_,     _use\_https : bool = True_,     _client : Any = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_,     _sign : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/neptune_graph.html#NeptuneGraph.__init__)\#     

Create a new Neptune graph wrapper instance.

Parameters:     

  * **host** \(_str_\)

  * **port** \(_int_\)

  * **use\_https** \(_bool_\)

  * **client** \(_Any_\)

  * **credentials\_profile\_name** \(_str_ _|__None_\)

  * **region\_name** \(_str_ _|__None_\)

  * **sign** \(_bool_\)

Return type:     

None

query\(

    _query : str_,     _params : dict = \{\}_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/neptune_graph.html#NeptuneGraph.query)\#     

Query Neptune database.

Parameters:     

  * **query** \(_str_\)

  * **params** \(_dict_\)

Return type:     

_Dict_\[str, _Any_\]

Examples using NeptuneGraph

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [Amazon Neptune with Cypher](https://python.langchain.com/docs/integrations/graphs/amazon_neptune_open_cypher/)

__On this page