# DocumentAttribute — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.DocumentAttribute.html
**Word Count:** 48
**Links Count:** 103
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# DocumentAttribute\#

_class _langchain\_aws.retrievers.kendra.DocumentAttribute[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#DocumentAttribute)\#     

Bases: `BaseModel`

Document attribute.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _Key _: str_ _\[Required\]_\#     

The key of the attribute.

_param _Value _: [DocumentAttributeValue](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.DocumentAttributeValue.html#langchain_aws.retrievers.kendra.DocumentAttributeValue "langchain_aws.retrievers.kendra.DocumentAttributeValue")_ _\[Required\]_\#     

The value of the attribute.

__On this page