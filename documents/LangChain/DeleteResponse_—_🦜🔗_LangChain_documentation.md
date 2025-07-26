# DeleteResponse — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.DeleteResponse.html
**Word Count:** 111
**Links Count:** 116
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# DeleteResponse\#

_class _langchain\_core.indexing.base.DeleteResponse[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/base.html#DeleteResponse)\#     

A generic response for delete operation.

The fields in this response are optional and whether the vectorstore returns them or not is up to the implementation.

num\_deleted _: int_\#     

The number of items that were successfully deleted.

If returned, this should only include _actual_ deletions.

If the ID did not exist to begin with, it should not be included in this count.

succeeded _: Sequence\[str\]_\#     

The IDs that were successfully deleted.

If returned, this should only include _actual_ deletions.

If the ID did not exist to begin with, it should not be included in this list.

failed _: Sequence\[str\]_\#     

The IDs that failed to be deleted.

Please note that deleting an ID that does not exist is **NOT** considered a failure.

num\_failed _: int_\#     

The number of items that failed to be deleted.

__On this page