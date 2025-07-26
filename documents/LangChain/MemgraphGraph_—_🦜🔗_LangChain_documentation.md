# MemgraphGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.memgraph_graph.MemgraphGraph.html
**Word Count:** 377
**Links Count:** 153
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# MemgraphGraph\#

_class _langchain\_community.graphs.memgraph\_graph.MemgraphGraph\(

    _url : str | None = None_,     _username : str | None = None_,     _password : str | None = None_,     _database : str | None = None_,     _refresh\_schema : bool = True_,     _\*_ ,     _driver\_config : Dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/memgraph_graph.html#MemgraphGraph)\#     

Memgraph wrapper for graph operations.

Parameters: url \(Optional\[str\]\): The URL of the Memgraph database server. username \(Optional\[str\]\): The username for database authentication. password \(Optional\[str\]\): The password for database authentication. database \(str\): The name of the database to connect to. Default is ‘memgraph’. refresh\_schema \(bool\): A flag whether to refresh schema information at initialization. Default is True. driver\_config \(Dict\): Configuration passed to Neo4j Driver.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new Memgraph graph wrapper instance.

Attributes

`get_schema` | Returns the schema of the Graph database   ---|---   `get_structured_schema` | Returns the structured schema of the Graph database      Methods

`__init__`\(\[url, username, password, ...\]\) | Create a new Memgraph graph wrapper instance.   ---|---   `add_graph_documents`\(graph\_documents\[, ...\]\) | Take GraphDocument as input as uses it to construct a graph in Memgraph.   `close`\(\) |    `query`\(query\[, params\]\) | Query the graph.   `refresh_schema`\(\) | Refreshes the Memgraph graph schema information.      Parameters:     

  * **url** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **database** \(_str_ _|__None_\)

  * **refresh\_schema** \(_bool_\)

  * **driver\_config** \(_Dict_ _|__None_\)

\_\_init\_\_\(

    _url : str | None = None_,     _username : str | None = None_,     _password : str | None = None_,     _database : str | None = None_,     _refresh\_schema : bool = True_,     _\*_ ,     _driver\_config : Dict | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/memgraph_graph.html#MemgraphGraph.__init__)\#     

Create a new Memgraph graph wrapper instance.

Parameters:     

  * **url** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **database** \(_str_ _|__None_\)

  * **refresh\_schema** \(_bool_\)

  * **driver\_config** \(_Dict_ _|__None_\)

Return type:     

None

add\_graph\_documents\(

    _graph\_documents : List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\]_,     _include\_source : bool = False_,     _baseEntityLabel : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/memgraph_graph.html#MemgraphGraph.add_graph_documents)\#     

Take GraphDocument as input as uses it to construct a graph in Memgraph.

Parameters: \- graph\_documents \(List\[GraphDocument\]\): A list of GraphDocument objects that contain the nodes and relationships to be added to the graph. Each GraphDocument should encapsulate the structure of part of the graph, including nodes, relationships, and the source document information. \- include\_source \(bool, optional\): If True, stores the source document and links it to nodes in the graph using the MENTIONS relationship. This is useful for tracing back the origin of data. Merges source documents based on the id property from the source document metadata if available; otherwise it calculates the MD5 hash of page\_content for merging process. Defaults to False. \- baseEntityLabel \(bool, optional\): If True, each newly created node gets a secondary \_\_Entity\_\_ label, which is indexed and improves import speed and performance. Defaults to False.

Parameters:     

  * **graph\_documents** \(_List_ _\[_[_GraphDocument_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument") _\]_\)

  * **include\_source** \(_bool_\)

  * **baseEntityLabel** \(_bool_\)

Return type:     

None

close\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/memgraph_graph.html#MemgraphGraph.close)\#     

Return type:     

None

query\(

    _query : str_,     _params : dict = \{\}_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/memgraph_graph.html#MemgraphGraph.query)\#     

Query the graph.

Parameters:     

  * **query** \(_str_\) – The Cypher query to execute.

  * **params** \(_dict_\) – The parameters to pass to the query.

Returns:     

The list of dictionaries containing the query results.

Return type:     

List\[Dict\[str, Any\]\]

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/memgraph_graph.html#MemgraphGraph.refresh_schema)\#     

Refreshes the Memgraph graph schema information.

Return type:     

None

Examples using MemgraphGraph

  * [Memgraph](https://python.langchain.com/docs/integrations/graphs/memgraph/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)