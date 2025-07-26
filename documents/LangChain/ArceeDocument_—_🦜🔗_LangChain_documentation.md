# ArceeDocument — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.ArceeDocument.html
**Word Count:** 40
**Links Count:** 258
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# ArceeDocument\#

_class _langchain\_community.utilities.arcee.ArceeDocument[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arcee.html#ArceeDocument)\#     

Bases: `BaseModel`

Arcee document.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _id _: str_ _\[Required\]_\#     

_param _index _: str_ _\[Required\]_\#     

_param _score _: float_ _\[Required\]_\#     

_param _source _: [ArceeDocumentSource](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.ArceeDocumentSource.html#langchain_community.utilities.arcee.ArceeDocumentSource "langchain_community.utilities.arcee.ArceeDocumentSource")_ _\[Required\]_\#     

__On this page