# HugeGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.hugegraph.HugeGraph.html
**Word Count:** 131
**Links Count:** 143
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# HugeGraph\#

_class _langchain\_community.graphs.hugegraph.HugeGraph\(

    _username : str = 'default'_,     _password : str = 'default'_,     _address : str = '127.0.0.1'_,     _port : int = 8081_,     _graph : str = 'hugegraph'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/hugegraph.html#HugeGraph)\#     

HugeGraph wrapper for graph operations.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new HugeGraph wrapper instance.

Attributes

`get_schema` | Returns the schema of the HugeGraph database   ---|---      Methods

`__init__`\(\[username, password, address, ...\]\) | Create a new HugeGraph wrapper instance.   ---|---   `query`\(query\) |    `refresh_schema`\(\) | Refreshes the HugeGraph schema information.      Parameters:     

  * **username** \(_str_\)

  * **password** \(_str_\)

  * **address** \(_str_\)

  * **port** \(_int_\)

  * **graph** \(_str_\)

\_\_init\_\_\(

    _username : str = 'default'_,     _password : str = 'default'_,     _address : str = '127.0.0.1'_,     _port : int = 8081_,     _graph : str = 'hugegraph'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/hugegraph.html#HugeGraph.__init__)\#     

Create a new HugeGraph wrapper instance.

Parameters:     

  * **username** \(_str_\)

  * **password** \(_str_\)

  * **address** \(_str_\)

  * **port** \(_int_\)

  * **graph** \(_str_\)

Return type:     

None

query\(

    _query : str_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/hugegraph.html#HugeGraph.query)\#     

Parameters:     

**query** \(_str_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

refresh\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/hugegraph.html#HugeGraph.refresh_schema)\#     

Refreshes the HugeGraph schema information.

Return type:     

None

Examples using HugeGraph

  * [HugeGraph](https://python.langchain.com/docs/integrations/graphs/hugegraph/)

__On this page