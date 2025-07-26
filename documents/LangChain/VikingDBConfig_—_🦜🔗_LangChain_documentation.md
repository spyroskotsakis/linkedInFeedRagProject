# VikingDBConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vikingdb.VikingDBConfig.html
**Word Count:** 59
**Links Count:** 322
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# VikingDBConfig\#

_class _langchain\_community.vectorstores.vikingdb.VikingDBConfig\(

    _host : str = 'host'_,     _region : str = 'region'_,     _ak : str = 'ak'_,     _sk : str = 'sk'_,     _scheme : str = 'http'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vikingdb.html#VikingDBConfig)\#     

vikingdb connection config

See the following documentation for details: <https://www.volcengine.com/docs/6459/1167770>

Attribute:     

host\(str\):The access address of the vector database server     

that the client needs to connect to.

region\(str\):”cn-shanghai” or “cn-beijing” ak\(str\):Access Key ID, security credentials for accessing

> Volcano Engine services.

sk\(str\):Secret Access Key, security credentials for accessing     

Volcano Engine services.

scheme\(str\):http or https, defaulting to http.

Methods

`__init__`\(\[host, region, ak, sk, scheme\]\) |    ---|---      Parameters:     

  * **host** \(_str_\)

  * **region** \(_str_\)

  * **ak** \(_str_\)

  * **sk** \(_str_\)

  * **scheme** \(_str_\)

\_\_init\_\_\(

    _host : str = 'host'_,     _region : str = 'region'_,     _ak : str = 'ak'_,     _sk : str = 'sk'_,     _scheme : str = 'http'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vikingdb.html#VikingDBConfig.__init__)\#     

Parameters:     

  * **host** \(_str_\)

  * **region** \(_str_\)

  * **ak** \(_str_\)

  * **sk** \(_str_\)

  * **scheme** \(_str_\)

Return type:     

None

Examples using VikingDBConfig

  * [viking DB](https://python.langchain.com/docs/integrations/vectorstores/vikingdb/)

__On this page