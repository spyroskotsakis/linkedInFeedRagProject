# TigerGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.tigergraph_graph.TigerGraph.html
**Word Count:** 282
**Links Count:** 168
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# TigerGraph\#

_class _langchain\_community.graphs.tigergraph\_graph.TigerGraph\(_conn : Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/tigergraph_graph.html#TigerGraph)\#     

TigerGraph wrapper for graph operations.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new TigerGraph graph wrapper instance.

Attributes

`conn` |    ---|---   `get_structured_schema` | Return the schema of the Graph database   `schema` |       Methods

`__init__`\(conn\) | Create a new TigerGraph graph wrapper instance.   ---|---   `add_graph_documents`\(graph\_documents\[, ...\]\) | Take GraphDocument as input as uses it to construct a graph.   `generate_schema`\(\) | Generates the schema of the TigerGraph Database and returns it User can specify a **sample\_ratio** \(0 to 1\) to determine the ratio of documents/edges used \(in relation to the Collection size\) to render each Collection Schema.   `get_schema`\(\) | Return the schema of the Graph database   `query`\(query\) | Query the TigerGraph database.   `refresh_schema`\(\) | Refresh the graph schema information.   `register_query`\(function\_header, description, ...\) | Wrapper function to register a custom GSQL query to the TigerGraph NLQS.   `set_connection`\(conn\) |    `set_schema`\(\[schema\]\) | Set the schema of the TigerGraph Database.      Parameters:     

**conn** \(_Any_\)

\_\_init\_\_\(_conn : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/tigergraph_graph.html#TigerGraph.__init__)\#     

Create a new TigerGraph graph wrapper instance.

Parameters:     

**conn** \(_Any_\)

Return type:     

None

_abstractmethod _add\_graph\_documents\(

    _graph\_documents : List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\]_,     _include\_source : bool = False_, \) → None\#     

Take GraphDocument as input as uses it to construct a graph.

Parameters:     

  * **graph\_documents** \(_List_ _\[_[_GraphDocument_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument") _\]_\)

  * **include\_source** \(_bool_\)

Return type:     

None

generate\_schema\(\) → Dict\[str, List\[Dict\[str, Any\]\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/tigergraph_graph.html#TigerGraph.generate_schema)\#     

Generates the schema of the TigerGraph Database and returns it User can specify a **sample\_ratio** \(0 to 1\) to determine the ratio of documents/edges used \(in relation to the Collection size\) to render each Collection Schema.

Return type:     

_Dict_\[str, _List_\[_Dict_\[str, _Any_\]\]\]

get\_schema\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/tigergraph_graph.html#TigerGraph.get_schema)\#     

Return the schema of the Graph database

Return type:     

str

query\(

    _query : str_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/tigergraph_graph.html#TigerGraph.query)\#     

Query the TigerGraph database.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_\[str, _Any_\]

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/tigergraph_graph.html#TigerGraph.refresh_schema)\#     

Refresh the graph schema information.

Return type:     

None

register\_query\(

    _function\_header : str_,     _description : str_,     _docstring : str_,     _param\_types : dict = \{\}_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/tigergraph_graph.html#TigerGraph.register_query)\#     

Wrapper function to register a custom GSQL query to the TigerGraph NLQS.

Parameters:     

  * **function\_header** \(_str_\)

  * **description** \(_str_\)

  * **docstring** \(_str_\)

  * **param\_types** \(_dict_\)

Return type:     

_List_\[str\]

set\_connection\(_conn : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/tigergraph_graph.html#TigerGraph.set_connection)\#     

Parameters:     

**conn** \(_Any_\)

Return type:     

None

set\_schema\(

    _schema : Dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/tigergraph_graph.html#TigerGraph.set_schema)\#     

Set the schema of the TigerGraph Database. Auto-generates Schema if **schema** is None.

Parameters:     

**schema** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Return type:     

None

Examples using TigerGraph

  * [TigerGraph](https://python.langchain.com/docs/integrations/graphs/tigergraph/)

__On this page