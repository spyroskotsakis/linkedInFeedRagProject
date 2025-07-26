# KuzuGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.kuzu_graph.KuzuGraph.html
**Word Count:** 302
**Links Count:** 148
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# KuzuGraph\#

_class _langchain\_community.graphs.kuzu\_graph.KuzuGraph\(

    _db : Any_,     _database : str = 'kuzu'_,     _allow\_dangerous\_requests : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/kuzu_graph.html#KuzuGraph)\#     

Kùzu wrapper for graph operations.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Initializes the Kùzu graph database connection.

Attributes

`get_schema` | Returns the schema of the Kùzu database   ---|---      Methods

`__init__`\(db\[, database, ...\]\) | Initializes the Kùzu graph database connection.   ---|---   `add_graph_documents`\(graph\_documents, ...\[, ...\]\) | Adds a list of GraphDocument objects that represent nodes and relationships in a graph to a Kùzu backend.   `query`\(query\[, params\]\) | Query Kùzu database   `refresh_schema`\(\) | Refreshes the Kùzu graph schema information      Parameters:     

  * **db** \(_Any_\)

  * **database** \(_str_\)

  * **allow\_dangerous\_requests** \(_bool_\)

\_\_init\_\_\(

    _db : Any_,     _database : str = 'kuzu'_,     _allow\_dangerous\_requests : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/kuzu_graph.html#KuzuGraph.__init__)\#     

Initializes the Kùzu graph database connection.

Parameters:     

  * **db** \(_Any_\)

  * **database** \(_str_\)

  * **allow\_dangerous\_requests** \(_bool_\)

Return type:     

None

add\_graph\_documents\(

    _graph\_documents : List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\]_,     _allowed\_relationships : List\[Tuple\[str, str, str\]\]_,     _include\_source : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/kuzu_graph.html#KuzuGraph.add_graph_documents)\#     

Adds a list of GraphDocument objects that represent nodes and relationships in a graph to a Kùzu backend.

Parameters:     

  * **graph\_documents** \(_-_\) – A list of GraphDocument objects that contain the nodes and relationships to be added to the graph. Each GraphDocument should encapsulate the structure of part of the graph, including nodes, relationships, and the source document information.

  * **allowed\_relationships** \(_-_\) – A list of allowed relationships that exist in the graph. Each tuple contains three elements: the source node type, the relationship type, and the target node type. Required for Kùzu, as the names of the relationship tables that need to pre-exist are derived from these tuples.

  * **include\_source** \(_-_\) – If True, stores the source document and links it to nodes in the graph using the MENTIONS relationship. This is useful for tracing back the origin of data. Merges source documents based on the id property from the source document metadata if available; otherwise it calculates the MD5 hash of page\_content for merging process. Defaults to False.

Return type:     

None

query\(

    _query : str_,     _params : dict = \{\}_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/kuzu_graph.html#KuzuGraph.query)\#     

Query Kùzu database

Parameters:     

  * **query** \(_str_\)

  * **params** \(_dict_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/kuzu_graph.html#KuzuGraph.refresh_schema)\#     

Refreshes the Kùzu graph schema information

Return type:     

None

Examples using KuzuGraph

  * [Kuzu](https://python.langchain.com/docs/integrations/graphs/kuzu_db/)

__On this page