# YouDocument — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouDocument.html
**Word Count:** 46
**Links Count:** 254
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# YouDocument\#

_class _langchain\_community.utilities.you.YouDocument[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/you.html#YouDocument)\#     

Bases: `BaseModel`

Output of parsing one snippet.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _metadata _: [YouHitMetadata](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouHitMetadata.html#langchain_community.utilities.you.YouHitMetadata "langchain_community.utilities.you.YouHitMetadata")_ _\[Required\]_\#     

_param _page\_content _: str_ _\[Required\]_\#     

One snippet of text

__On this page