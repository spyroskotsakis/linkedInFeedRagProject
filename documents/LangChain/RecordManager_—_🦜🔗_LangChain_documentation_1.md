# RecordManager — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.RecordManager.html
**Word Count:** 853
**Links Count:** 160
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# RecordManager\#

_class _langchain\_core.indexing.base.RecordManager\(_namespace : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager)\#     

Abstract base class representing the interface for a record manager.

The record manager abstraction is used by the langchain indexing API.

The record manager keeps track of which documents have been written into a vectorstore and when they were written.

The indexing API computes hashes for each document and stores the hash together with the write time and the source id in the record manager.

On subsequent indexing runs, the indexing API can check the record manager to determine which documents have already been indexed and which have not.

This allows the indexing API to avoid re-indexing documents that have already been indexed, and to only index new documents.

The main benefit of this abstraction is that it works across many vectorstores. To be supported, a vectorstore needs to only support the ability to add and delete documents by ID. Using the record manager, the indexing API will be able to delete outdated documents and avoid redundant indexing of documents that have already been indexed.

The main constraints of this abstraction are:

  1. It relies on the time-stamps to determine which documents have been indexed and which have not. This means that the time-stamps must be monotonically increasing. The timestamp should be the timestamp as measured by the server to minimize issues.

  2. The record manager is currently implemented separately from the vectorstore, which means that the overall system becomes distributed and may create issues with consistency. For example, writing to record manager succeeds, but corresponding writing to vectorstore fails.

Initialize the record manager.

Parameters:     

**namespace** \(_str_\) – The namespace for the record manager.

Methods

`__init__`\(namespace\) | Initialize the record manager.   ---|---   `acreate_schema`\(\) | Asynchronously create the database schema for the record manager.   `adelete_keys`\(keys\) | Asynchronously delete specified records from the database.   `aexists`\(keys\) | Asynchronously check if the provided keys exist in the database.   `aget_time`\(\) | Asynchronously get the current server time as a high resolution timestamp.   `alist_keys`\(\*\[, before, after, group\_ids, limit\]\) | Asynchronously list records in the database based on the provided filters.   `aupdate`\(keys, \*\[, group\_ids, time\_at\_least\]\) | Asynchronously upsert records into the database.   `create_schema`\(\) | Create the database schema for the record manager.   `delete_keys`\(keys\) | Delete specified records from the database.   `exists`\(keys\) | Check if the provided keys exist in the database.   `get_time`\(\) | Get the current server time as a high resolution timestamp\!   `list_keys`\(\*\[, before, after, group\_ids, limit\]\) | List records in the database based on the provided filters.   `update`\(keys, \*\[, group\_ids, time\_at\_least\]\) | Upsert records into the database.      \_\_init\_\_\(_namespace : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.__init__)\#     

Initialize the record manager.

Parameters:     

**namespace** \(_str_\) – The namespace for the record manager.

Return type:     

None

_abstractmethod async _acreate\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.acreate_schema)\#     

Asynchronously create the database schema for the record manager.

Return type:     

None

_abstractmethod async _adelete\_keys\(_keys : Sequence\[str\]_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.adelete_keys)\#     

Asynchronously delete specified records from the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to delete.

Return type:     

None

_abstractmethod async _aexists\(_keys : Sequence\[str\]_\) → list\[bool\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.aexists)\#     

Asynchronously check if the provided keys exist in the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to check.

Returns:     

A list of boolean values indicating the existence of each key.

Return type:     

list\[bool\]

_abstractmethod async _aget\_time\(\) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.aget_time)\#     

Asynchronously get the current server time as a high resolution timestamp.

It’s important to get this from the server to ensure a monotonic clock, otherwise there may be data loss when cleaning up old documents\!

Returns:     

The current server time as a float timestamp.

Return type:     

float

_abstractmethod async _alist\_keys\(

    _\*_ ,     _before : float | None = None_,     _after : float | None = None_,     _group\_ids : Sequence\[str\] | None = None_,     _limit : int | None = None_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.alist_keys)\#     

Asynchronously list records in the database based on the provided filters.

Parameters:     

  * **before** \(_Optional_ _\[__float_ _\]_\) – Filter to list records updated before this time.

  * **after** \(_Optional_ _\[__float_ _\]_\) – Filter to list records updated after this time.

  * **group\_ids** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Filter to list records with specific group IDs.

  * **limit** \(_Optional_ _\[__int_ _\]_\) – optional limit on the number of records to return.

Returns:     

A list of keys for the matching records.

Return type:     

list\[str\]

_abstractmethod async _aupdate\(

    _keys : Sequence\[str\]_,     _\*_ ,     _group\_ids : Sequence\[str | None\] | None = None_,     _time\_at\_least : float | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.aupdate)\#     

Asynchronously upsert records into the database.

Parameters:     

  * **keys** \(_Sequence_ _\[__str_ _\]_\) – A list of record keys to upsert.

  * **group\_ids** \(_Optional_ _\[__Sequence_ _\[__Optional_ _\[__str_ _\]__\]__\]_\) – A list of group IDs corresponding to the keys.

  * **time\_at\_least** \(_Optional_ _\[__float_ _\]_\) – 

Optional timestamp. Implementation can use this to optionally verify that the timestamp IS at least this time in the system that stores the data.

e.g., use to validate that the time in the postgres database is equal to or larger than the given timestamp, if not raise an error.

This is meant to help prevent time-drift issues since time may not be monotonically increasing\!

Raises:     

**ValueError** – If the length of keys doesn’t match the length of group\_ids.

Return type:     

None

_abstractmethod _create\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.create_schema)\#     

Create the database schema for the record manager.

Return type:     

None

_abstractmethod _delete\_keys\(_keys : Sequence\[str\]_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.delete_keys)\#     

Delete specified records from the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to delete.

Return type:     

None

_abstractmethod _exists\(_keys : Sequence\[str\]_\) → list\[bool\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.exists)\#     

Check if the provided keys exist in the database.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A list of keys to check.

Returns:     

A list of boolean values indicating the existence of each key.

Return type:     

list\[bool\]

_abstractmethod _get\_time\(\) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.get_time)\#     

Get the current server time as a high resolution timestamp\!

It’s important to get this from the server to ensure a monotonic clock, otherwise there may be data loss when cleaning up old documents\!

Returns:     

The current server time as a float timestamp.

Return type:     

float

_abstractmethod _list\_keys\(

    _\*_ ,     _before : float | None = None_,     _after : float | None = None_,     _group\_ids : Sequence\[str\] | None = None_,     _limit : int | None = None_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.list_keys)\#     

List records in the database based on the provided filters.

Parameters:     

  * **before** \(_Optional_ _\[__float_ _\]_\) – Filter to list records updated before this time.

  * **after** \(_Optional_ _\[__float_ _\]_\) – Filter to list records updated after this time.

  * **group\_ids** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Filter to list records with specific group IDs.

  * **limit** \(_Optional_ _\[__int_ _\]_\) – optional limit on the number of records to return.

Returns:     

A list of keys for the matching records.

Return type:     

list\[str\]

_abstractmethod _update\(

    _keys : Sequence\[str\]_,     _\*_ ,     _group\_ids : Sequence\[str | None\] | None = None_,     _time\_at\_least : float | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#RecordManager.update)\#     

Upsert records into the database.

Parameters:     

  * **keys** \(_Sequence_ _\[__str_ _\]_\) – A list of record keys to upsert.

  * **group\_ids** \(_Optional_ _\[__Sequence_ _\[__Optional_ _\[__str_ _\]__\]__\]_\) – A list of group IDs corresponding to the keys.

  * **time\_at\_least** \(_Optional_ _\[__float_ _\]_\) – 

Optional timestamp. Implementation can use this to optionally verify that the timestamp IS at least this time in the system that stores the data.

e.g., use to validate that the time in the postgres database is equal to or larger than the given timestamp, if not raise an error.

This is meant to help prevent time-drift issues since time may not be monotonically increasing\!

Raises:     

**ValueError** – If the length of keys doesn’t match the length of group\_ids.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)