# NebulaGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.nebula_graph.NebulaGraph.html
**Word Count:** 150
**Links Count:** 147
**Scraped:** 2025-07-21 08:11:13
**Status:** completed

---

# NebulaGraph\#

_class _langchain\_community.graphs.nebula\_graph.NebulaGraph\(

    _space : str_,     _username : str = 'root'_,     _password : str = 'nebula'_,     _address : str = '127.0.0.1'_,     _port : int = 9669_,     _session\_pool\_size : int = 30_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/nebula_graph.html#NebulaGraph)\#     

NebulaGraph wrapper for graph operations.

NebulaGraph inherits methods from Neo4jGraph to bring ease to the user space.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new NebulaGraph wrapper instance.

Attributes

`get_schema` | Returns the schema of the NebulaGraph database   ---|---      Methods

`__init__`\(space\[, username, password, ...\]\) | Create a new NebulaGraph wrapper instance.   ---|---   `execute`\(query\[, params, retry\]\) | Query NebulaGraph database.   `query`\(query\[, retry\]\) |    `refresh_schema`\(\) | Refreshes the NebulaGraph schema information.      Parameters:     

  * **space** \(_str_\)

  * **username** \(_str_\)

  * **password** \(_str_\)

  * **address** \(_str_\)

  * **port** \(_int_\)

  * **session\_pool\_size** \(_int_\)

\_\_init\_\_\(

    _space : str_,     _username : str = 'root'_,     _password : str = 'nebula'_,     _address : str = '127.0.0.1'_,     _port : int = 9669_,     _session\_pool\_size : int = 30_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/nebula_graph.html#NebulaGraph.__init__)\#     

Create a new NebulaGraph wrapper instance.

Parameters:     

  * **space** \(_str_\)

  * **username** \(_str_\)

  * **password** \(_str_\)

  * **address** \(_str_\)

  * **port** \(_int_\)

  * **session\_pool\_size** \(_int_\)

Return type:     

None

execute\(

    _query : str_,     _params : dict | None = None_,     _retry : int = 0_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/nebula_graph.html#NebulaGraph.execute)\#     

Query NebulaGraph database.

Parameters:     

  * **query** \(_str_\)

  * **params** \(_dict_ _|__None_\)

  * **retry** \(_int_\)

Return type:     

_Any_

query\(

    _query : str_,     _retry : int = 0_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/nebula_graph.html#NebulaGraph.query)\#     

Parameters:     

  * **query** \(_str_\)

  * **retry** \(_int_\)

Return type:     

_Dict_\[str, _Any_\]

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/nebula_graph.html#NebulaGraph.refresh_schema)\#     

Refreshes the NebulaGraph schema information.

Return type:     

None

Examples using NebulaGraph

  * [NebulaGraph](https://python.langchain.com/docs/integrations/graphs/nebula_graph/)

__On this page