# BaseMedia — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.BaseMedia.html
**Word Count:** 91
**Links Count:** 108
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# BaseMedia\#

_class _langchain\_core.documents.base.BaseMedia[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/base.html#BaseMedia)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Use to represent media content.

Media objects can be used to represent raw data, such as text or binary data.

LangChain Media objects allow associating metadata and an optional identifier with the content.

The presence of an ID and metadata make it easier to store, index, and search over the content in a structured way.

_param _id _: str | None_ _ = None_\#     

An optional identifier for the document.

Ideally this should be unique across the document collection and formatted as a UUID, but this will not be enforced.

Added in version 0.2.11.

Constraints:     

  * **coerce\_numbers\_to\_str** = True

_param _metadata _: dict_ _\[Optional\]_\#     

Arbitrary metadata associated with the content.

__On this page