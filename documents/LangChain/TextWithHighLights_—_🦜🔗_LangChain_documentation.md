# TextWithHighLights — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.TextWithHighLights.html
**Word Count:** 43
**Links Count:** 102
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# TextWithHighLights\#

_class _langchain\_aws.retrievers.kendra.TextWithHighLights[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#TextWithHighLights)\#     

Bases: `BaseModel`

Text with highlights.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _Highlights _: Any | None_ _ = None_\#     

The highlights.

_param _Text _: str_ _\[Required\]_\#     

The text.

__On this page