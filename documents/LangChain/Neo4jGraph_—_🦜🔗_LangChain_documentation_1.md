# Neo4jGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.neo4j_graph.Neo4jGraph.html
**Word Count:** 523
**Links Count:** 107
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# Neo4jGraph\#

_class _langchain\_neo4j.graphs.neo4j\_graph.Neo4jGraph\(

    _url : str | None = None_,     _username : str | None = None_,     _password : str | None = None_,     _database : str | None = None_,     _timeout : float | None = None_,     _sanitize : bool = False_,     _refresh\_schema : bool = True_,     _\*_ ,     _driver\_config : Dict | None = None_,     _enhanced\_schema : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/neo4j_graph.html#Neo4jGraph)\#     

Neo4j database wrapper for various graph operations.

Parameters: url \(Optional\[str\]\): The URL of the Neo4j database server. username \(Optional\[str\]\): The username for database authentication. password \(Optional\[str\]\): The password for database authentication. database \(str\): The name of the database to connect to. Default is ‘neo4j’. timeout \(Optional\[float\]\): The timeout for transactions in seconds.

> Useful for terminating long-running queries. By default, there is no timeout set.

sanitize \(bool\): A flag to indicate whether to remove lists with     

more than 128 elements from results. Useful for removing embedding-like properties from database responses. Default is False.

refresh\_schema \(bool\): A flag whether to refresh schema information     

at initialization. Default is True.

enhanced\_schema \(bool\): A flag whether to scan the database for     

example values and use them in the graph schema. Default is False.

driver\_config \(Dict\): Configuration passed to Neo4j Driver.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new Neo4j graph wrapper instance.

Attributes

`get_schema` | Returns the schema of the Graph   ---|---   `get_structured_schema` | Returns the structured schema of the Graph      Methods

`__init__`\(\[url, username, password, ...\]\) | Create a new Neo4j graph wrapper instance.   ---|---   `add_graph_documents`\(graph\_documents\[, ...\]\) | This method constructs nodes and relationships in the graph based on the provided GraphDocument objects.   `close`\(\) | Explicitly close the Neo4j driver connection.   `query`\(query\[, params, session\_params\]\) | Query Neo4j database.   `refresh_schema`\(\) | Refreshes the Neo4j graph schema information.      Parameters:     

  * **url** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **database** \(_str_ _|__None_\)

  * **timeout** \(_float_ _|__None_\)

  * **sanitize** \(_bool_\)

  * **refresh\_schema** \(_bool_\)

  * **driver\_config** \(_Dict_ _|__None_\)

  * **enhanced\_schema** \(_bool_\)

\_\_init\_\_\(

    _url : str | None = None_,     _username : str | None = None_,     _password : str | None = None_,     _database : str | None = None_,     _timeout : float | None = None_,     _sanitize : bool = False_,     _refresh\_schema : bool = True_,     _\*_ ,     _driver\_config : Dict | None = None_,     _enhanced\_schema : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/neo4j_graph.html#Neo4jGraph.__init__)\#     

Create a new Neo4j graph wrapper instance.

Parameters:     

  * **url** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **database** \(_str_ _|__None_\)

  * **timeout** \(_float_ _|__None_\)

  * **sanitize** \(_bool_\)

  * **refresh\_schema** \(_bool_\)

  * **driver\_config** \(_Dict_ _|__None_\)

  * **enhanced\_schema** \(_bool_\)

Return type:     

None

add\_graph\_documents\(

    _graph\_documents : List\[[GraphDocument](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument")\]_,     _include\_source : bool = False_,     _baseEntityLabel : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/neo4j_graph.html#Neo4jGraph.add_graph_documents)\#     

This method constructs nodes and relationships in the graph based on the provided GraphDocument objects.

Parameters: \- graph\_documents \(List\[GraphDocument\]\): A list of GraphDocument objects that contain the nodes and relationships to be added to the graph. Each GraphDocument should encapsulate the structure of part of the graph, including nodes, relationships, and optionally the source document information. \- include\_source \(bool, optional\): If True, stores the source document and links it to nodes in the graph using the MENTIONS relationship. This is useful for tracing back the origin of data. Merges source documents based on the id property from the source document metadata if available; otherwise it calculates the MD5 hash of page\_content for merging process. Defaults to False. \- baseEntityLabel \(bool, optional\): If True, each newly created node gets a secondary \_\_Entity\_\_ label, which is indexed and improves import speed and performance. Defaults to False.

Raises:     

**RuntimeError** – If the connection has been closed.

Parameters:     

  * **graph\_documents** \(_List_ _\[_[_GraphDocument_](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument") _\]_\)

  * **include\_source** \(_bool_\)

  * **baseEntityLabel** \(_bool_\)

Return type:     

None

close\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/neo4j_graph.html#Neo4jGraph.close)\#     

Explicitly close the Neo4j driver connection.

Delegates connection management to the Neo4j driver.

Return type:     

None

query\(

    _query : str_,     _params : dict = \{\}_,     _session\_params : dict = \{\}_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/neo4j_graph.html#Neo4jGraph.query)\#     

Query Neo4j database.

Parameters:     

  * **query** \(_str_\) – The Cypher query to execute.

  * **params** \(_dict_\) – The parameters to pass to the query.

  * **session\_params** \(_dict_\) – Parameters to pass to the session used for executing the query.

Returns:     

The list of dictionaries containing the query results.

Return type:     

List\[Dict\[str, Any\]\]

Raises:     

**RuntimeError** – If the connection has been closed.

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/graphs/neo4j_graph.html#Neo4jGraph.refresh_schema)\#     

Refreshes the Neo4j graph schema information.

Raises:     

**RuntimeError** – If the connection has been closed.

Return type:     

None

Examples using Neo4jGraph

  * [Build a Question Answering application over a Graph Database](https://python.langchain.com/docs/tutorials/graph/)

  * [Diffbot](https://python.langchain.com/docs/integrations/graphs/diffbot/)

  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)

  * [How to best prompt for Graph-RAG](https://python.langchain.com/docs/how_to/graph_prompting/)

  * [How to construct knowledge graphs](https://python.langchain.com/docs/how_to/graph_constructing/)

  * [How to map values to a graph database](https://python.langchain.com/docs/how_to/graph_mapping/)

  * [Neo4j](https://python.langchain.com/docs/integrations/graphs/neo4j_cypher/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)