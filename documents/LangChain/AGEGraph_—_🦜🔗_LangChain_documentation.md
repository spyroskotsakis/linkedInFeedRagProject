# AGEGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.age_graph.AGEGraph.html
**Word Count:** 319
**Links Count:** 153
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# AGEGraph\#

_class _langchain\_community.graphs.age\_graph.AGEGraph\(

    _graph\_name : str_,     _conf : Dict\[str, Any\]_,     _create : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/age_graph.html#AGEGraph)\#     

Apache AGE wrapper for graph operations.

Parameters:     

  * **graph\_name** \(_str_\) – the name of the graph to connect to or create

  * **conf** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – the pgsql connection config passed directly to psycopg2.connect

  * **create** \(_bool_\) – if True and graph doesn’t exist, attempt to create it

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new AGEGraph instance.

Attributes

`get_schema` | Returns the schema of the Graph   ---|---   `get_structured_schema` | Returns the structured schema of the Graph   `label_regex` |    `types` |       Methods

`__init__`\(graph\_name, conf\[, create\]\) | Create a new AGEGraph instance.   ---|---   `add_graph_documents`\(graph\_documents\[, ...\]\) | insert a list of graph documents into the graph   `clean_graph_labels`\(label\) | remove any disallowed characters from a label and replace with '\_'   `query`\(query\[, params\]\) | Query the graph by taking a cypher query, converting it to an age compatible query, executing it and converting the result   `refresh_schema`\(\) | Refresh the graph schema information by updating the available labels, relationships, and properties      \_\_init\_\_\(

    _graph\_name : str_,     _conf : Dict\[str, Any\]_,     _create : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/age_graph.html#AGEGraph.__init__)\#     

Create a new AGEGraph instance.

Parameters:     

  * **graph\_name** \(_str_\)

  * **conf** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **create** \(_bool_\)

Return type:     

None

add\_graph\_documents\(

    _graph\_documents : List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\]_,     _include\_source : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/age_graph.html#AGEGraph.add_graph_documents)\#     

insert a list of graph documents into the graph

Parameters:     

  * **graph\_documents** \(_List_ _\[_[_GraphDocument_](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument") _\]_\) – the list of documents to be inserted

  * **include\_source** \(_bool_\) – if True add nodes for the sources with MENTIONS edges to the entities they mention

Returns:     

None

Return type:     

None

_static _clean\_graph\_labels\(_label : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/age_graph.html#AGEGraph.clean_graph_labels)\#     

remove any disallowed characters from a label and replace with ‘\_’

Parameters:     

**label** \(_str_\) – the original label

Returns:     

the sanitized version of the label

Return type:     

str

query\(

    _query : str_,     _params : dict = \{\}_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/age_graph.html#AGEGraph.query)\#     

Query the graph by taking a cypher query, converting it to an age compatible query, executing it and converting the result

Parameters:     

  * **query** \(_str_\) – a cypher query to be executed

  * **params** \(_dict_\) – parameters for the query \(not used in this implementation\)

Returns:     

a list of dictionaries containing the result set

Return type:     

List\[Dict\[str, Any\]\]

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/age_graph.html#AGEGraph.refresh_schema)\#     

Refresh the graph schema information by updating the available labels, relationships, and properties

Return type:     

None

Examples using AGEGraph

  * [Apache AGE](https://python.langchain.com/docs/integrations/graphs/apache_age/)

__On this page