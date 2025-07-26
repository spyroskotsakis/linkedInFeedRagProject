# InMemoryRecordManager — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.InMemoryRecordManager.html
**Word Count:** 624
**Links Count:** 160
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# InMemoryRecordManager\#

_class _langchain\_core.indexing.base.InMemoryRecordManager\(_namespace : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager)\#     

An in-memory record manager for testing purposes.

Initialize the in-memory record manager.

Parameters:     

**namespace** \(_str_\) – The namespace for the record manager.

Methods

`__init__`\(namespace\) | Initialize the in-memory record manager.   ---|---   `acreate_schema`\(\) | Async in-memory schema creation is simply ensuring the structure is initialized.   `adelete_keys`\(keys\) | Async delete specified records from the database.   `aexists`\(keys\) | Async check if the provided keys exist in the database.   `aget_time`\(\) | Async get the current server time as a high resolution timestamp\!   `alist_keys`\(\*\[, before, after, group\_ids, limit\]\) | Async list records in the database based on the provided filters.   `aupdate`\(keys, \*\[, group\_ids, time\_at\_least\]\) | Async upsert records into the database.   `create_schema`\(\) | In-memory schema creation is simply ensuring the structure is initialized.   `delete_keys`\(keys\) | Delete specified records from the database.   `exists`\(keys\) | Check if the provided keys exist in the database.   `get_time`\(\) | Get the current server time as a high resolution timestamp\!   `list_keys`\(\*\[, before, after, group\_ids, limit\]\) | List records in the database based on the provided filters.   `update`\(keys, \*\[, group\_ids, time\_at\_least\]\) | Upsert records into the database.      \_\_init\_\_\(_namespace : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.__init__)\#     

Initialize the in-memory record manager.

Parameters:     

**namespace** \(_str_\) – The namespace for the record manager.

Return type:     

None

_async _acreate\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.acreate_schema)\#     

Async in-memory schema creation is simply ensuring the structure is initialized.

Return type:     

None

_async _adelete\_keys\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.adelete_keys)\#     

Async delete specified records from the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to delete.

Return type:     

None

_async _aexists\(

    _keys : Sequence\[str\]_, \) → list\[bool\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.aexists)\#     

Async check if the provided keys exist in the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to check.

Returns:     

A list of boolean values indicating the existence of each key.

Return type:     

list\[bool\]

_async _aget\_time\(\) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.aget_time)\#     

Async get the current server time as a high resolution timestamp\!

Return type:     

float

_async _alist\_keys\(

    _\*_ ,     _before : float | None = None_,     _after : float | None = None_,     _group\_ids : Sequence\[str\] | None = None_,     _limit : int | None = None_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.alist_keys)\#     

Async list records in the database based on the provided filters.

Parameters:     

  * **before** \(_Optional_ _\[__float_ _\]_\) – Filter to list records updated before this time. Defaults to None.

  * **after** \(_Optional_ _\[__float_ _\]_\) – Filter to list records updated after this time. Defaults to None.

  * **group\_ids** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Filter to list records with specific group IDs. Defaults to None.

  * **limit** \(_Optional_ _\[__int_ _\]_\) – optional limit on the number of records to return. Defaults to None.

Returns:     

A list of keys for the matching records.

Return type:     

list\[str\]

_async _aupdate\(

    _keys : Sequence\[str\]_,     _\*_ ,     _group\_ids : Sequence\[str | None\] | None = None_,     _time\_at\_least : float | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.aupdate)\#     

Async upsert records into the database.

Parameters:     

  * **keys** \(_Sequence_ _\[__str_ _\]_\) – A list of record keys to upsert.

  * **group\_ids** \(_Optional_ _\[__Sequence_ _\[__Optional_ _\[__str_ _\]__\]__\]_\) – A list of group IDs corresponding to the keys. Defaults to None.

  * **time\_at\_least** \(_Optional_ _\[__float_ _\]_\) – Optional timestamp. Implementation can use this to optionally verify that the timestamp IS at least this time in the system that stores. Defaults to None. E.g., use to validate that the time in the postgres database is equal to or larger than the given timestamp, if not raise an error. This is meant to help prevent time-drift issues since time may not be monotonically increasing\!

Raises:     

  * **ValueError** – If the length of keys doesn’t match the length of group ids.

  * **ValueError** – If time\_at\_least is in the future.

Return type:     

None

create\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.create_schema)\#     

In-memory schema creation is simply ensuring the structure is initialized.

Return type:     

None

delete\_keys\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.delete_keys)\#     

Delete specified records from the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to delete.

Return type:     

None

exists\(

    _keys : Sequence\[str\]_, \) → list\[bool\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.exists)\#     

Check if the provided keys exist in the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to check.

Returns:     

A list of boolean values indicating the existence of each key.

Return type:     

list\[bool\]

get\_time\(\) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.get_time)\#     

Get the current server time as a high resolution timestamp\!

Return type:     

float

list\_keys\(

    _\*_ ,     _before : float | None = None_,     _after : float | None = None_,     _group\_ids : Sequence\[str\] | None = None_,     _limit : int | None = None_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.list_keys)\#     

List records in the database based on the provided filters.

Parameters:     

  * **before** \(_Optional_ _\[__float_ _\]_\) – Filter to list records updated before this time. Defaults to None.

  * **after** \(_Optional_ _\[__float_ _\]_\) – Filter to list records updated after this time. Defaults to None.

  * **group\_ids** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Filter to list records with specific group IDs. Defaults to None.

  * **limit** \(_Optional_ _\[__int_ _\]_\) – optional limit on the number of records to return. Defaults to None.

Returns:     

A list of keys for the matching records.

Return type:     

list\[str\]

update\(

    _keys : Sequence\[str\]_,     _\*_ ,     _group\_ids : Sequence\[str | None\] | None = None_,     _time\_at\_least : float | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#InMemoryRecordManager.update)\#     

Upsert records into the database.

Parameters:     

  * **keys** \(_Sequence_ _\[__str_ _\]_\) – A list of record keys to upsert.

  * **group\_ids** \(_Optional_ _\[__Sequence_ _\[__Optional_ _\[__str_ _\]__\]__\]_\) – A list of group IDs corresponding to the keys. Defaults to None.

  * **time\_at\_least** \(_Optional_ _\[__float_ _\]_\) – Optional timestamp. Implementation can use this to optionally verify that the timestamp IS at least this time in the system that stores. Defaults to None. E.g., use to validate that the time in the postgres database is equal to or larger than the given timestamp, if not raise an error. This is meant to help prevent time-drift issues since time may not be monotonically increasing\!

Raises:     

  * **ValueError** – If the length of keys doesn’t match the length of group ids.

  * **ValueError** – If time\_at\_least is in the future.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)