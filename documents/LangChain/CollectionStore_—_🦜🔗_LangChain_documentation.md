# CollectionStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.pgembedding.CollectionStore.html
**Word Count:** 123
**Links Count:** 331
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# CollectionStore\#

_class _langchain\_community.vectorstores.pgembedding.CollectionStore\(_\*\* kwargs_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/pgembedding.html#CollectionStore)\#     

Collection store.

A simple constructor that allows initialization from kwargs.

Sets attributes on the constructed instance using the names and values in `kwargs`.

Only keys that are present as attributes of the instance’s class are allowed. These could be, for example, any mapped columns or relationships.

Attributes

`cmetadata` |    ---|---   `embeddings` |    `metadata` |    `name` |    `registry` |    `uuid` |       Methods

`__init__`\(\*\*kwargs\) | A simple constructor that allows initialization from kwargs.   ---|---   `get_by_name`\(session, name\) |    `get_or_create`\(session, name\[, cmetadata\]\) | Get or create a collection.      \_\_init\_\_\(_\*\* kwargs_\)\#     

A simple constructor that allows initialization from kwargs.

Sets attributes on the constructed instance using the names and values in `kwargs`.

Only keys that are present as attributes of the instance’s class are allowed. These could be, for example, any mapped columns or relationships.

_classmethod _get\_by\_name\(

    _session : Session_,     _name : str_, \) → CollectionStore | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/pgembedding.html#CollectionStore.get_by_name)\#     

Parameters:     

  * **session** \(_Session_\)

  * **name** \(_str_\)

Return type:     

_CollectionStore_ | None

_classmethod _get\_or\_create\(

    _session : Session_,     _name : str_,     _cmetadata : dict | None = None_, \) → Tuple\[CollectionStore, bool\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/pgembedding.html#CollectionStore.get_or_create)\#     

Get or create a collection. Returns \[Collection, bool\] where the bool is True if the collection was created.

Parameters:     

  * **session** \(_Session_\)

  * **name** \(_str_\)

  * **cmetadata** \(_dict_ _|__None_\)

Return type:     

_Tuple_\[_CollectionStore_, bool\]

__On this page