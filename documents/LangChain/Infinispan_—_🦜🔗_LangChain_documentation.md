# Infinispan — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.infinispanvs.Infinispan.html
**Word Count:** 760
**Links Count:** 373
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# Infinispan\#

_class _langchain\_community.vectorstores.infinispanvs.Infinispan\(

    _schema : str = 'http'_,     _user : str = ''_,     _password : str = ''_,     _hosts : List\[str\] = \['127.0.0.1:11222'\]_,     _cache\_url : str = '/rest/v2/caches'_,     _schema\_url : str = '/rest/v2/schemas'_,     _use\_post\_for\_query : bool = True_,     _http2 : bool = True_,     _verify : bool = True_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan)\#     

Helper class for Infinispan REST interface.

This class exposes the Infinispan operations needed to create and set up a vector db.

You need a running Infinispan \(15+\) server without authentication. You can easily start one, see: [rigazilla/infinispan-vector](https://github.com/rigazilla/infinispan-vector#run-infinispan)

Parameters:     

  * **schema** \(_str_\) – Schema for HTTP request: “http” or “https”. Default “http”

  * **user** \(_str_\) – User and password if auth is required. Default None

  * **password** \(_str_\) – User and password if auth is required. Default None

  * **hosts** \(_List_ _\[__str_ _\]_\) – List of server addresses. Default \[“127.0.0.1:11222”\]

  * **cache\_url** \(_str_\) – URL endpoint for cache API. Default “/rest/v2/caches”

  * **schema\_url** \(_str_\) – URL endpoint for schema API. Default “/rest/v2/schemas”

  * **use\_post\_for\_query** \(_bool_\) – Whether POST method should be used for query. Default True

  * **http2** \(_bool_\) – Whether HTTP/2 protocol should be used. pip install “httpx\[http2\]” is needed for HTTP/2. Default True

  * **verify** \(_bool_\) – Whether TLS certificate must be verified. Default True

  * **kwargs** \(_Any_\)

Methods

`__init__`\(\[schema, user, password, hosts, ...\]\) |    ---|---   `cache_clear`\(cache\_name\) | Clear a cache :param cache\_name: name of the cache.   `cache_delete`\(name\) | Delete a cache :param name: name of the cache.   `cache_exists`\(cache\_name\) | Check if a cache exists :param cache\_name: name of the cache.   `cache_post`\(name, config\) | Create a cache :param name: name of the cache.   `get`\(key, cache\_name\) | Get an entry :param key: key of the entry :type key: str :param cache\_name: target cache :type cache\_name: str   `index_clear`\(cache\_name\) | Clear an index on a cache :param cache\_name: name of the cache.   `index_reindex`\(cache\_name\) | Rebuild index on a cache :param cache\_name: name of the cache.   `post`\(key, data, cache\_name\) | Post an entry :param key: key of the entry :type key: str :param data: content of the entry in json format :type data: str :param cache\_name: target cache :type cache\_name: str   `put`\(key, data, cache\_name\) | Put an entry :param key: key of the entry :type key: str :param data: content of the entry in json format :type data: str :param cache\_name: target cache :type cache\_name: str   `req_query`\(query, cache\_name\[, local\]\) | Request a query :param query: query requested :type query: str :param cache\_name: name of the target cache :type cache\_name: str :param local: whether the query is local to clustered :type local: boolean   `resource_exists`\(api\_url\) | Check if a resource exists :param api\_url: url of the resource.   `schema_delete`\(name\) | Delete a schema :param name: name of the schema.   `schema_post`\(name, proto\) | Deploy a schema :param name: name of the schema.      \_\_init\_\_\(

    _schema : str = 'http'_,     _user : str = ''_,     _password : str = ''_,     _hosts : List\[str\] = \['127.0.0.1:11222'\]_,     _cache\_url : str = '/rest/v2/caches'_,     _schema\_url : str = '/rest/v2/schemas'_,     _use\_post\_for\_query : bool = True_,     _http2 : bool = True_,     _verify : bool = True_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.__init__)\#     

Parameters:     

  * **schema** \(_str_\) – Schema for HTTP request: “http” or “https”. Default “http”

  * **user** \(_str_\) – User and password if auth is required. Default None

  * **password** \(_str_\) – User and password if auth is required. Default None

  * **hosts** \(_List_ _\[__str_ _\]_\) – List of server addresses. Default \[“127.0.0.1:11222”\]

  * **cache\_url** \(_str_\) – URL endpoint for cache API. Default “/rest/v2/caches”

  * **schema\_url** \(_str_\) – URL endpoint for schema API. Default “/rest/v2/schemas”

  * **use\_post\_for\_query** \(_bool_\) – Whether POST method should be used for query. Default True

  * **http2** \(_bool_\) – Whether HTTP/2 protocol should be used. pip install “httpx\[http2\]” is needed for HTTP/2. Default True

  * **verify** \(_bool_\) – Whether TLS certificate must be verified. Default True

  * **kwargs** \(_Any_\)

cache\_clear\(_cache\_name : str_\) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.cache_clear)\#     

Clear a cache :param cache\_name: name of the cache. :type cache\_name: str

Returns:     

An http Response containing the result of the operation

Parameters:     

**cache\_name** \(_str_\)

Return type:     

_Response_

cache\_delete\(_name : str_\) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.cache_delete)\#     

Delete a cache :param name: name of the cache. :type name: str

Returns:     

An http Response containing the result of the operation

Parameters:     

**name** \(_str_\)

Return type:     

_Response_

cache\_exists\(_cache\_name : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.cache_exists)\#     

Check if a cache exists :param cache\_name: name of the cache. :type cache\_name: str

Returns:     

True if cache exists

Parameters:     

**cache\_name** \(_str_\)

Return type:     

bool

cache\_post\(

    _name : str_,     _config : str_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.cache_post)\#     

Create a cache :param name: name of the cache. :type name: str :param config: configuration of the cache. :type config: str

Returns:     

An http Response containing the result of the operation

Parameters:     

  * **name** \(_str_\)

  * **config** \(_str_\)

Return type:     

_Response_

get\(_key : str_, _cache\_name : str_\) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.get)\#     

Get an entry :param key: key of the entry :type key: str :param cache\_name: target cache :type cache\_name: str

Returns:     

An http Response containing the entry or errors

Parameters:     

  * **key** \(_str_\)

  * **cache\_name** \(_str_\)

Return type:     

_Response_

index\_clear\(_cache\_name : str_\) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.index_clear)\#     

Clear an index on a cache :param cache\_name: name of the cache. :type cache\_name: str

Returns:     

An http Response containing the result of the operation

Parameters:     

**cache\_name** \(_str_\)

Return type:     

_Response_

index\_reindex\(_cache\_name : str_\) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.index_reindex)\#     

Rebuild index on a cache :param cache\_name: name of the cache. :type cache\_name: str

Returns:     

An http Response containing the result of the operation

Parameters:     

**cache\_name** \(_str_\)

Return type:     

_Response_

post\(

    _key : str_,     _data : str_,     _cache\_name : str_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.post)\#     

Post an entry :param key: key of the entry :type key: str :param data: content of the entry in json format :type data: str :param cache\_name: target cache :type cache\_name: str

Returns:     

An http Response containing the result of the operation

Parameters:     

  * **key** \(_str_\)

  * **data** \(_str_\)

  * **cache\_name** \(_str_\)

Return type:     

_Response_

put\(

    _key : str_,     _data : str_,     _cache\_name : str_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.put)\#     

Put an entry :param key: key of the entry :type key: str :param data: content of the entry in json format :type data: str :param cache\_name: target cache :type cache\_name: str

Returns:     

An http Response containing the result of the operation

Parameters:     

  * **key** \(_str_\)

  * **data** \(_str_\)

  * **cache\_name** \(_str_\)

Return type:     

_Response_

req\_query\(

    _query : str_,     _cache\_name : str_,     _local : bool = False_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.req_query)\#     

Request a query :param query: query requested :type query: str :param cache\_name: name of the target cache :type cache\_name: str :param local: whether the query is local to clustered :type local: boolean

Returns:     

An http Response containing the result set or errors

Parameters:     

  * **query** \(_str_\)

  * **cache\_name** \(_str_\)

  * **local** \(_bool_\)

Return type:     

_Response_

resource\_exists\(_api\_url : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.resource_exists)\#     

Check if a resource exists :param api\_url: url of the resource. :type api\_url: str

Returns:     

true if resource exists

Parameters:     

**api\_url** \(_str_\)

Return type:     

bool

schema\_delete\(_name : str_\) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.schema_delete)\#     

Delete a schema :param name: name of the schema. :type name: str

Returns:     

An http Response containing the result of the operation

Parameters:     

**name** \(_str_\)

Return type:     

_Response_

schema\_post\(

    _name : str_,     _proto : str_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/infinispanvs.html#Infinispan.schema_post)\#     

Deploy a schema :param name: name of the schema. Will be used as a key :type name: str :param proto: protobuf schema :type proto: str

Returns:     

An http Response containing the result of the operation

Parameters:     

  * **name** \(_str_\)

  * **proto** \(_str_\)

Return type:     

_Response_

__On this page