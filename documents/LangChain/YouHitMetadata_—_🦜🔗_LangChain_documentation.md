# YouHitMetadata — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouHitMetadata.html
**Word Count:** 60
**Links Count:** 257
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# YouHitMetadata\#

_class _langchain\_community.utilities.you.YouHitMetadata[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/you.html#YouHitMetadata)\#     

Bases: `BaseModel`

Metadata on a single hit from you.com

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _description _: str_ _\[Required\]_\#     

Details about the result

_param _thumbnail\_url _: str_ _\[Required\]_\#     

Thumbnail associated with the result

_param _title _: str_ _\[Required\]_\#     

The title of the result

_param _url _: str_ _\[Required\]_\#     

The url of the result

__On this page