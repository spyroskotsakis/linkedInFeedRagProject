# NeptuneAnalyticsGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/graphs/langchain_aws.graphs.neptune_graph.NeptuneAnalyticsGraph.html
**Word Count:** 163
**Links Count:** 96
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# NeptuneAnalyticsGraph\#

_class _langchain\_aws.graphs.neptune\_graph.NeptuneAnalyticsGraph\(

    _graph\_identifier : str_,     _client : Any = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_,     _aws\_access\_key\_id : SecretStr | None = None_,     _aws\_secret\_access\_key : SecretStr | None = None_,     _aws\_session\_token : SecretStr | None = None_,     _endpoint\_url : str | None = None_,     _config : Any = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/graphs/neptune_graph.html#NeptuneAnalyticsGraph)\#     

Neptune Analytics wrapper for graph operations.

Parameters:     

  * **client** \(_Any_\) – optional boto3 Neptune client

  * **credentials\_profile\_name** \(_str_ _|__None_\) – optional AWS profile name

  * **region\_name** \(_str_ _|__None_\) – optional AWS region, e.g., us-west-2

  * **graph\_identifier** \(_str_\) – the graph identifier for a Neptune Analytics graph

  * **aws\_access\_key\_id** \(_SecretStr_ _|__None_\)

  * **aws\_secret\_access\_key** \(_SecretStr_ _|__None_\)

  * **aws\_session\_token** \(_SecretStr_ _|__None_\)

  * **endpoint\_url** \(_str_ _|__None_\)

  * **config** \(_Any_\)

Example               

graph = NeptuneAnalyticsGraph\(     

graph\_identifier=’<my-graph-id>’

\)

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new Neptune Analytics graph wrapper instance.

Attributes

`get_schema` | Returns the schema of the Neptune database   ---|---      Methods

`__init__`\(graph\_identifier\[, client, ...\]\) | Create a new Neptune Analytics graph wrapper instance.   ---|---   `query`\(query\[, params\]\) | Query Neptune database.      \_\_init\_\_\(

    _graph\_identifier : str_,     _client : Any = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_,     _aws\_access\_key\_id : SecretStr | None = None_,     _aws\_secret\_access\_key : SecretStr | None = None_,     _aws\_session\_token : SecretStr | None = None_,     _endpoint\_url : str | None = None_,     _config : Any = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/graphs/neptune_graph.html#NeptuneAnalyticsGraph.__init__)\#     

Create a new Neptune Analytics graph wrapper instance.

Parameters:     

  * **graph\_identifier** \(_str_\)

  * **client** \(_Any_\)

  * **credentials\_profile\_name** \(_str_ _|__None_\)

  * **region\_name** \(_str_ _|__None_\)

  * **aws\_access\_key\_id** \(_SecretStr_ _|__None_\)

  * **aws\_secret\_access\_key** \(_SecretStr_ _|__None_\)

  * **aws\_session\_token** \(_SecretStr_ _|__None_\)

  * **endpoint\_url** \(_str_ _|__None_\)

  * **config** \(_Any_\)

Return type:     

None

query\(

    _query : str_,     _params : dict = \{\}_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/graphs/neptune_graph.html#NeptuneAnalyticsGraph.query)\#     

Query Neptune database.

Parameters:     

  * **query** \(_str_\)

  * **params** \(_dict_\)

Return type:     

_Dict_\[str, _Any_\]

Examples using NeptuneAnalyticsGraph

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [Amazon Neptune with Cypher](https://python.langchain.com/docs/integrations/graphs/amazon_neptune_open_cypher/)

__On this page