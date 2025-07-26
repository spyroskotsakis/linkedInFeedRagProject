# GraphStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_store.GraphStore.html
**Word Count:** 61
**Links Count:** 94
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# GraphStore\#

_class _langchain\_neo4j.graphs.graph\_store.GraphStore\(_\* args_, _\*\* kwargs_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/graph_store.html#GraphStore)\#     

Abstract class for graph operations.

Attributes

`get_schema` | Return the schema of the Graph database   ---|---   `get_structured_schema` | Return the schema of the Graph database      Methods

`__init__`\(\*args, \*\*kwargs\) |    ---|---   `add_graph_documents`\(graph\_documents\[, ...\]\) | Take GraphDocument as input as uses it to construct a graph.   `query`\(query\[, params\]\) | Query the graph.   `refresh_schema`\(\) | Refresh the graph schema information.      \_\_init\_\_\(_\* args_, _\*\* kwargs_\)\#     

add\_graph\_documents\(

    _graph\_documents : List\[[GraphDocument](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument")\]_,     _include\_source : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/graph_store.html#GraphStore.add_graph_documents)\#     

Take GraphDocument as input as uses it to construct a graph.

Parameters:     

  * **graph\_documents** \(_List_ _\[_[_GraphDocument_](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument") _\]_\)

  * **include\_source** \(_bool_\)

Return type:     

None

query\(

    _query : str_,     _params : dict = \{\}_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/graph_store.html#GraphStore.query)\#     

Query the graph.

Parameters:     

  * **query** \(_str_\)

  * **params** \(_dict_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/graph_store.html#GraphStore.refresh_schema)\#     

Refresh the graph schema information.

Return type:     

None

__On this page