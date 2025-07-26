# RecordManager — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/indexes/langchain_community.indexes.base.RecordManager.html
**Word Count:** 517
**Links Count:** 149
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# RecordManager\#

_class _langchain\_community.indexes.base.RecordManager\(_namespace : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager)\#     

Abstract base class for a record manager.

Initialize the record manager.

Parameters:     

**namespace** \(_str_\) – The namespace for the record manager.

Methods

`__init__`\(namespace\) | Initialize the record manager.   ---|---   `acreate_schema`\(\) | Create the database schema for the record manager.   `adelete_keys`\(keys\) | Delete specified records from the database.   `aexists`\(keys\) | Check if the provided keys exist in the database.   `aget_time`\(\) | Get the current server time as a high resolution timestamp\!   `alist_keys`\(\*\[, before, after, group\_ids, limit\]\) | List records in the database based on the provided filters.   `aupdate`\(keys, \*\[, group\_ids, time\_at\_least\]\) | Upsert records into the database.   `create_schema`\(\) | Create the database schema for the record manager.   `delete_keys`\(keys\) | Delete specified records from the database.   `exists`\(keys\) | Check if the provided keys exist in the database.   `get_time`\(\) | Get the current server time as a high resolution timestamp\!   `list_keys`\(\*\[, before, after, group\_ids, limit\]\) | List records in the database based on the provided filters.   `update`\(keys, \*\[, group\_ids, time\_at\_least\]\) | Upsert records into the database.      \_\_init\_\_\(_namespace : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.__init__)\#     

Initialize the record manager.

Parameters:     

**namespace** \(_str_\) – The namespace for the record manager.

Return type:     

None

_abstractmethod async _acreate\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.acreate_schema)\#     

Create the database schema for the record manager.

Return type:     

None

_abstractmethod async _adelete\_keys\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.adelete_keys)\#     

Delete specified records from the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to delete.

Return type:     

None

_abstractmethod async _aexists\(

    _keys : Sequence\[str\]_, \) → List\[bool\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.aexists)\#     

Check if the provided keys exist in the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to check.

Returns:     

A list of boolean values indicating the existence of each key.

Return type:     

_List_\[bool\]

_abstractmethod async _aget\_time\(\) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.aget_time)\#     

Get the current server time as a high resolution timestamp\!

It’s important to get this from the server to ensure a monotonic clock, otherwise there may be data loss when cleaning up old documents\!

Returns:     

The current server time as a float timestamp.

Return type:     

float

_abstractmethod async _alist\_keys\(

    _\*_ ,     _before : float | None = None_,     _after : float | None = None_,     _group\_ids : Sequence\[str\] | None = None_,     _limit : int | None = None_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.alist_keys)\#     

List records in the database based on the provided filters.

Parameters:     

  * **before** \(_float_ _|__None_\) – Filter to list records updated before this time.

  * **after** \(_float_ _|__None_\) – Filter to list records updated after this time.

  * **group\_ids** \(_Sequence_ _\[__str_ _\]__|__None_\) – Filter to list records with specific group IDs.

  * **limit** \(_int_ _|__None_\) – optional limit on the number of records to return.

Returns:     

A list of keys for the matching records.

Return type:     

_List_\[str\]

_abstractmethod async _aupdate\(

    _keys : Sequence\[str\]_,     _\*_ ,     _group\_ids : Sequence\[str | None\] | None = None_,     _time\_at\_least : float | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.aupdate)\#     

Upsert records into the database.

Parameters:     

  * **keys** \(_Sequence_ _\[__str_ _\]_\) – A list of record keys to upsert.

  * **group\_ids** \(_Sequence_ _\[__str_ _|__None_ _\]__|__None_\) – A list of group IDs corresponding to the keys.

  * **time\_at\_least** \(_float_ _|__None_\) – if provided, updates should only happen if the updated\_at field is at least this time.

Raises:     

**ValueError** – If the length of keys doesn’t match the length of group\_ids.

Return type:     

None

_abstractmethod _create\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.create_schema)\#     

Create the database schema for the record manager.

Return type:     

None

_abstractmethod _delete\_keys\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.delete_keys)\#     

Delete specified records from the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to delete.

Return type:     

None

_abstractmethod _exists\(

    _keys : Sequence\[str\]_, \) → List\[bool\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.exists)\#     

Check if the provided keys exist in the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to check.

Returns:     

A list of boolean values indicating the existence of each key.

Return type:     

_List_\[bool\]

_abstractmethod _get\_time\(\) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.get_time)\#     

Get the current server time as a high resolution timestamp\!

It’s important to get this from the server to ensure a monotonic clock, otherwise there may be data loss when cleaning up old documents\!

Returns:     

The current server time as a float timestamp.

Return type:     

float

_abstractmethod _list\_keys\(

    _\*_ ,     _before : float | None = None_,     _after : float | None = None_,     _group\_ids : Sequence\[str\] | None = None_,     _limit : int | None = None_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.list_keys)\#     

List records in the database based on the provided filters.

Parameters:     

  * **before** \(_float_ _|__None_\) – Filter to list records updated before this time.

  * **after** \(_float_ _|__None_\) – Filter to list records updated after this time.

  * **group\_ids** \(_Sequence_ _\[__str_ _\]__|__None_\) – Filter to list records with specific group IDs.

  * **limit** \(_int_ _|__None_\) – optional limit on the number of records to return.

Returns:     

A list of keys for the matching records.

Return type:     

_List_\[str\]

_abstractmethod _update\(

    _keys : Sequence\[str\]_,     _\*_ ,     _group\_ids : Sequence\[str | None\] | None = None_,     _time\_at\_least : float | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/indexes/base.html#RecordManager.update)\#     

Upsert records into the database.

Parameters:     

  * **keys** \(_Sequence_ _\[__str_ _\]_\) – A list of record keys to upsert.

  * **group\_ids** \(_Sequence_ _\[__str_ _|__None_ _\]__|__None_\) – A list of group IDs corresponding to the keys.

  * **time\_at\_least** \(_float_ _|__None_\) – if provided, updates should only happen if the updated\_at field is at least this time.

Raises:     

**ValueError** – If the length of keys doesn’t match the length of group\_ids.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)