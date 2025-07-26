# DocumentAttributeValue — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.kendra.DocumentAttributeValue.html
**Word Count:** 78
**Links Count:** 182
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# DocumentAttributeValue\#

_class _langchain\_community.retrievers.kendra.DocumentAttributeValue[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/kendra.html#DocumentAttributeValue)\#     

Bases: `BaseModel`

Value of a document attribute.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _DateValue _: str | None_ _ = None_\#     

The date expressed as an ISO 8601 string.

_param _LongValue _: int | None_ _ = None_\#     

The long value.

_param _StringListValue _: List\[str\] | None_ _ = None_\#     

The string list value.

_param _StringValue _: str | None_ _ = None_\#     

The string value.

_property _value _: str | int | List\[str\] | None_\#     

The only defined document attribute value or None. According to Amazon Kendra, you can only provide one value for a document attribute.

__On this page