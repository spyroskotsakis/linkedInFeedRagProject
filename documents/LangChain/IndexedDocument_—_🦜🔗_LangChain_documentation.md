# IndexedDocument — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.IndexedDocument.html
**Word Count:** 54
**Links Count:** 260
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# IndexedDocument\#

_class _langchain\_community.utilities.pebblo.IndexedDocument[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#IndexedDocument)\#     

Bases: [`Document`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

Pebblo Indexed Document.

Pass page\_content in as positional or named arg.

_param _id _: str | None_ _ = None_\#     

An optional identifier for the document.

Ideally this should be unique across the document collection and formatted as a UUID, but this will not be enforced.

Added in version 0.2.11.

Constraints:     

  * **coerce\_numbers\_to\_str** = True

_param _metadata _: dict_ _\[Optional\]_\#     

Arbitrary metadata associated with the content.

_param _page\_content _: str_ _\[Required\]_\#     

String text.

_param _pb\_id _: str_ _\[Required\]_\#     

Unique ID of the document.

_param _type _: Literal\['Document'\]__ = 'Document'_\#     

__On this page