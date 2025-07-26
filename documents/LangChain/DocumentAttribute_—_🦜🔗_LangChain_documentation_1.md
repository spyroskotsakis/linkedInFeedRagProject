# DocumentAttribute — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.DocumentAttribute.html
**Word Count:** 48
**Links Count:** 177
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# DocumentAttribute\#

_class _langchain\_community.retrievers.kendra.DocumentAttribute[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#DocumentAttribute)\#     

Bases: `BaseModel`

Document attribute.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _Key _: str_ _\[Required\]_\#     

The key of the attribute.

_param _Value _: [DocumentAttributeValue](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.DocumentAttributeValue.html#langchain_community.retrievers.kendra.DocumentAttributeValue "langchain_community.retrievers.kendra.DocumentAttributeValue")_ _\[Required\]_\#     

The value of the attribute.

__On this page