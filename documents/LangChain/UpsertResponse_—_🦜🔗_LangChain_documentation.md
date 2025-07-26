# UpsertResponse — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.UpsertResponse.html
**Word Count:** 136
**Links Count:** 112
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# UpsertResponse\#

_class _langchain\_core.indexing.base.UpsertResponse[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#UpsertResponse)\#     

A generic response for upsert operations.

The upsert response will be used by abstractions that implement an upsert operation for content that can be upserted by ID.

Upsert APIs that accept inputs with IDs and generate IDs internally will return a response that includes the IDs that succeeded and the IDs that failed.

If there are no failures, the failed list will be empty, and the order of the IDs in the succeeded list will match the order of the input documents.

If there are failures, the response becomes ill defined, and a user of the API cannot determine which generated ID corresponds to which input document.

It is recommended for users explicitly attach the IDs to the items being indexed to avoid this issue.

succeeded _: list\[str\]_\#     

The IDs that were successfully indexed.

failed _: list\[str\]_\#     

The IDs that failed to index.

__On this page