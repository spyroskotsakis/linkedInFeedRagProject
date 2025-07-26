# KineticaUtil — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.kinetica.KineticaUtil.html
**Word Count:** 72
**Links Count:** 231
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# KineticaUtil\#

_class _langchain\_community.chat\_models.kinetica.KineticaUtil[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/kinetica.html#KineticaUtil)\#     

Kinetica utility functions.

Methods

`create_kdbc`\(\[url, user, passwd\]\) | Create a connectica connection object and verify connectivity.   ---|---      _classmethod _create\_kdbc\(

    _url : str | None = None_,     _user : str | None = None_,     _passwd : str | None = None_, \) → gpudb.GPUdb[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/kinetica.html#KineticaUtil.create_kdbc)\#     

Create a connectica connection object and verify connectivity.

If None is passed for one or more of the parameters then an attempt will be made to retrieve the value from the related environment variable.

Parameters:     

  * **url** \(_str_ _|__None_\) – The Kinetica URL or `KINETICA_URL` if None.

  * **user** \(_str_ _|__None_\) – The Kinetica user or `KINETICA_USER` if None.

  * **passwd** \(_str_ _|__None_\) – The Kinetica password or `KINETICA_PASSWD` if None.

Returns:     

The Kinetica connection object.

Return type:     

gpudb.GPUdb

__On this page