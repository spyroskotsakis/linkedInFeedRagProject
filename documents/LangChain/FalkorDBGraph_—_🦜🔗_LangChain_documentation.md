# FalkorDBGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.falkordb_graph.FalkorDBGraph.html
**Word Count:** 172
**Links Count:** 149
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# FalkorDBGraph\#

_class _langchain\_community.graphs.falkordb\_graph.FalkorDBGraph\(

    _database : str_,     _host : str = 'localhost'_,     _port : int = 6379_,     _username : str | None = None_,     _password : str | None = None_,     _ssl : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/falkordb_graph.html#FalkorDBGraph)\#     

FalkorDB wrapper for graph operations.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new FalkorDB graph wrapper instance.

Attributes

`get_schema` | Returns the schema of the FalkorDB database   ---|---   `get_structured_schema` | Returns the structured schema of the Graph      Methods

`__init__`\(database\[, host, port, username, ...\]\) | Create a new FalkorDB graph wrapper instance.   ---|---   `add_graph_documents`\(graph\_documents\[, ...\]\) | Take GraphDocument as input as uses it to construct a graph.   `query`\(query\[, params\]\) | Query FalkorDB database.   `refresh_schema`\(\) | Refreshes the schema of the FalkorDB database      Parameters:     

  * **database** \(_str_\)

  * **host** \(_str_\)

  * **port** \(_int_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **ssl** \(_bool_\)

\_\_init\_\_\(

    _database : str_,     _host : str = 'localhost'_,     _port : int = 6379_,     _username : str | None = None_,     _password : str | None = None_,     _ssl : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/falkordb_graph.html#FalkorDBGraph.__init__)\#     

Create a new FalkorDB graph wrapper instance.

Parameters:     

  * **database** \(_str_\)

  * **host** \(_str_\)

  * **port** \(_int_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **ssl** \(_bool_\)

Return type:     

None

add\_graph\_documents\(

    _graph\_documents : List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\]_,     _include\_source : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/falkordb_graph.html#FalkorDBGraph.add_graph_documents)\#     

Take GraphDocument as input as uses it to construct a graph.

Parameters:     

  * **graph\_documents** \(_List_ _\[_[_GraphDocument_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument") _\]_\)

  * **include\_source** \(_bool_\)

Return type:     

None

query\(

    _query : str_,     _params : dict = \{\}_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/falkordb_graph.html#FalkorDBGraph.query)\#     

Query FalkorDB database.

Parameters:     

  * **query** \(_str_\)

  * **params** \(_dict_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/falkordb_graph.html#FalkorDBGraph.refresh_schema)\#     

Refreshes the schema of the FalkorDB database

Return type:     

None

Examples using FalkorDBGraph

  * [FalkorDB](https://python.langchain.com/docs/integrations/graphs/falkordb/)

__On this page