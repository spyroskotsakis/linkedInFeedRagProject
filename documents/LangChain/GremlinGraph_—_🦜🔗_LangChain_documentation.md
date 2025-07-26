# GremlinGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.gremlin_graph.GremlinGraph.html
**Word Count:** 259
**Links Count:** 176
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# GremlinGraph\#

_class _langchain\_community.graphs.gremlin\_graph.GremlinGraph\(

    _url : str | None = None_,     _username : str | None = None_,     _password : str | None = None_,     _traversal\_source : str = 'g'_,     _message\_serializer : Any | None = None_,     _include\_edge\_properties : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/gremlin_graph.html#GremlinGraph)\#     

Gremlin wrapper for graph operations.

Parameters: url \(Optional\[str\]\): The URL of the Gremlin database server or env GREMLIN\_URI username \(Optional\[str\]\): The collection-identifier like ‘/dbs/database/colls/graph’

> or env GREMLIN\_USERNAME if none provided

password \(Optional\[str\]\): The connection-key for database authentication     

or env GREMLIN\_PASSWORD if none provided

traversal\_source \(str\): The traversal source to use for queries. Defaults to ‘g’. message\_serializer \(Optional\[Any\]\): The message serializer to use for requests.

> Defaults to serializer.GraphSONSerializersV2d0\(\)

include\_edge\_properties \(bool\): Whether to include edge properties in     

the gremlin graph schema. Defaults to False

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

_Implementation details_ :     

The Gremlin queries are designed to work with Azure CosmosDB limitations

Create a new Gremlin graph wrapper instance.

Attributes

`get_schema` | Returns the schema of the Gremlin database   ---|---   `get_structured_schema` | Return the schema of the Graph database      Methods

`__init__`\(\[url, username, password, ...\]\) | Create a new Gremlin graph wrapper instance.   ---|---   `add_edge`\(relationship\) |    `add_graph_documents`\(graph\_documents\[, ...\]\) | Take GraphDocument as input as uses it to construct a graph.   `add_node`\(node\[, node\_cache\]\) |    `build_edge_query`\(relationship\) |    `build_vertex_query`\(node\) |    `query`\(query\[, params\]\) | Query the graph.   `refresh_schema`\(\) | Refreshes the Gremlin graph schema information.      Parameters:     

  * **url** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **traversal\_source** \(_str_\)

  * **message\_serializer** \(_Any_ _|__None_\)

  * **include\_edge\_properties** \(_bool_\)

\_\_init\_\_\(

    _url : str | None = None_,     _username : str | None = None_,     _password : str | None = None_,     _traversal\_source : str = 'g'_,     _message\_serializer : Any | None = None_,     _include\_edge\_properties : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/gremlin_graph.html#GremlinGraph.__init__)\#     

Create a new Gremlin graph wrapper instance.

Parameters:     

  * **url** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **traversal\_source** \(_str_\)

  * **message\_serializer** \(_Any_ _|__None_\)

  * **include\_edge\_properties** \(_bool_\)

Return type:     

None

add\_edge\(

    _relationship : [Relationship](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Relationship.html#langchain_community.graphs.graph_document.Relationship "langchain_community.graphs.graph_document.Relationship")_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/gremlin_graph.html#GremlinGraph.add_edge)\#     

Parameters:     

**relationship** \([_Relationship_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Relationship.html#langchain_community.graphs.graph_document.Relationship "langchain_community.graphs.graph_document.Relationship")\)

Return type:     

_Any_

add\_graph\_documents\(

    _graph\_documents : List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\]_,     _include\_source : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/gremlin_graph.html#GremlinGraph.add_graph_documents)\#     

Take GraphDocument as input as uses it to construct a graph.

Parameters:     

  * **graph\_documents** \(_List_ _\[_[_GraphDocument_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument") _\]_\)

  * **include\_source** \(_bool_\)

Return type:     

None

add\_node\(

    _node : [Node](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")_,     _node\_cache : dict = \{\}_, \) → [Node](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/gremlin_graph.html#GremlinGraph.add_node)\#     

Parameters:     

  * **node** \([_Node_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")\)

  * **node\_cache** \(_dict_\)

Return type:     

[_Node_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")

build\_edge\_query\(

    _relationship : [Relationship](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Relationship.html#langchain_community.graphs.graph_document.Relationship "langchain_community.graphs.graph_document.Relationship")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/gremlin_graph.html#GremlinGraph.build_edge_query)\#     

Parameters:     

**relationship** \([_Relationship_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Relationship.html#langchain_community.graphs.graph_document.Relationship "langchain_community.graphs.graph_document.Relationship")\)

Return type:     

str

build\_vertex\_query\(

    _node : [Node](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/gremlin_graph.html#GremlinGraph.build_vertex_query)\#     

Parameters:     

**node** \([_Node_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")\)

Return type:     

str

query\(

    _query : str_,     _params : dict = \{\}_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/gremlin_graph.html#GremlinGraph.query)\#     

Query the graph.

Parameters:     

  * **query** \(_str_\)

  * **params** \(_dict_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/gremlin_graph.html#GremlinGraph.refresh_schema)\#     

Refreshes the Gremlin graph schema information.

Return type:     

None

Examples using GremlinGraph

  * [Azure Cosmos DB for Apache Gremlin](https://python.langchain.com/docs/integrations/graphs/azure_cosmosdb_gremlin/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page