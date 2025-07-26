# YouHit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouHit.html
**Word Count:** 67
**Links Count:** 260
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# YouHit\#

_class _langchain\_community.utilities.you.YouHit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/you.html#YouHit)\#     

Bases: [`YouHitMetadata`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouHitMetadata.html#langchain_community.utilities.you.YouHitMetadata "langchain_community.utilities.you.YouHitMetadata")

A single hit from you.com, which may contain multiple snippets

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _description _: str_ _\[Required\]_\#     

Details about the result

_param _snippets _: List\[str\]__\[Required\]_\#     

One or snippets of text

_param _thumbnail\_url _: str_ _\[Required\]_\#     

Thumbnail associated with the result

_param _title _: str_ _\[Required\]_\#     

The title of the result

_param _url _: str_ _\[Required\]_\#     

The url of the result

__On this page