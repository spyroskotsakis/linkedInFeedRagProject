# get_arangodb_client — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.arangodb_graph.get_arangodb_client.html
**Word Count:** 85
**Links Count:** 130
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# get\_arangodb\_client\#

langchain\_community.graphs.arangodb\_graph.get\_arangodb\_client\(

    _url : str | None = None_,     _dbname : str | None = None_,     _username : str | None = None_,     _password : str | None = None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/arangodb_graph.html#get_arangodb_client)\#     

Get the Arango DB client from credentials.

Parameters:     

  * **url** \(_str_ _|__None_\) – Arango DB url. Can be passed in as named arg or set as environment var `ARANGODB_URL`. Defaults to “<http://localhost:8529>”.

  * **dbname** \(_str_ _|__None_\) – Arango DB name. Can be passed in as named arg or set as environment var `ARANGODB_DBNAME`. Defaults to “\_system”.

  * **username** \(_str_ _|__None_\) – Can be passed in as named arg or set as environment var `ARANGODB_USERNAME`. Defaults to “root”.

  * **password** \(_str_ _|__None_\) – Can be passed ni as named arg or set as environment var `ARANGODB_PASSWORD`. Defaults to “”.

Returns:     

An arango.database.StandardDatabase.

Return type:     

_Any_

__On this page