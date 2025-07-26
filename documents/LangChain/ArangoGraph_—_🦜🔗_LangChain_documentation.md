# ArangoGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.arangodb_graph.ArangoGraph.html
**Word Count:** 297
**Links Count:** 156
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# ArangoGraph\#

_class _langchain\_community.graphs.arangodb\_graph.ArangoGraph\(_db : Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/arangodb_graph.html#ArangoGraph)\#     

ArangoDB wrapper for graph operations.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new ArangoDB graph wrapper instance.

Attributes

`db` |    ---|---   `schema` |       Methods

`__init__`\(db\) | Create a new ArangoDB graph wrapper instance.   ---|---   `from_db_credentials`\(\[url, dbname, username, ...\]\) | Convenience constructor that builds Arango DB from credentials.   `generate_schema`\(\[sample\_ratio\]\) | Generates the schema of the ArangoDB Database and returns it User can specify a **sample\_ratio** \(0 to 1\) to determine the ratio of documents/edges used \(in relation to the Collection size\) to render each Collection Schema.   `query`\(query\[, top\_k\]\) | Query the ArangoDB database.   `set_db`\(db\) |    `set_schema`\(\[schema\]\) | Set the schema of the ArangoDB Database.      Parameters:     

**db** \(_Any_\)

\_\_init\_\_\(_db : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/arangodb_graph.html#ArangoGraph.__init__)\#     

Create a new ArangoDB graph wrapper instance.

Parameters:     

**db** \(_Any_\)

Return type:     

None

_classmethod _from\_db\_credentials\(

    _url : str | None = None_,     _dbname : str | None = None_,     _username : str | None = None_,     _password : str | None = None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/arangodb_graph.html#ArangoGraph.from_db_credentials)\#     

Convenience constructor that builds Arango DB from credentials.

Parameters:     

  * **url** \(_str_ _|__None_\) – Arango DB url. Can be passed in as named arg or set as environment var `ARANGODB_URL`. Defaults to “<http://localhost:8529>”.

  * **dbname** \(_str_ _|__None_\) – Arango DB name. Can be passed in as named arg or set as environment var `ARANGODB_DBNAME`. Defaults to “\_system”.

  * **username** \(_str_ _|__None_\) – Can be passed in as named arg or set as environment var `ARANGODB_USERNAME`. Defaults to “root”.

  * **password** \(_str_ _|__None_\) – Can be passed ni as named arg or set as environment var `ARANGODB_PASSWORD`. Defaults to “”.

Returns:     

An arango.database.StandardDatabase.

Return type:     

_Any_

generate\_schema\(

    _sample\_ratio : float = 0_, \) → Dict\[str, List\[Dict\[str, Any\]\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/arangodb_graph.html#ArangoGraph.generate_schema)\#     

Generates the schema of the ArangoDB Database and returns it User can specify a **sample\_ratio** \(0 to 1\) to determine the ratio of documents/edges used \(in relation to the Collection size\) to render each Collection Schema.

Parameters:     

**sample\_ratio** \(_float_\)

Return type:     

_Dict_\[str, _List_\[_Dict_\[str, _Any_\]\]\]

query\(

    _query : str_,     _top\_k : int | None = None_,     _\*\* kwargs: Any_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/arangodb_graph.html#ArangoGraph.query)\#     

Query the ArangoDB database.

Parameters:     

  * **query** \(_str_\)

  * **top\_k** \(_int_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

set\_db\(_db : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/arangodb_graph.html#ArangoGraph.set_db)\#     

Parameters:     

**db** \(_Any_\)

Return type:     

None

set\_schema\(

    _schema : Dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/arangodb_graph.html#ArangoGraph.set_schema)\#     

Set the schema of the ArangoDB Database. Auto-generates Schema if **schema** is None.

Parameters:     

**schema** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Return type:     

None

Examples using ArangoGraph

  * [ArangoDB](https://python.langchain.com/docs/integrations/graphs/arangodb/)

__On this page