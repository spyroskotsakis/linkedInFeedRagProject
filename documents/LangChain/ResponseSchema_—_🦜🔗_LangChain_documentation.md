# ResponseSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/output_parsers/langchain.output_parsers.structured.ResponseSchema.html
**Word Count:** 59
**Links Count:** 106
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# ResponseSchema\#

_class _langchain.output\_parsers.structured.ResponseSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/output_parsers/structured.html#ResponseSchema)\#     

Bases: `BaseModel`

Schema for a response from a structured output parser.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _description _: str_ _\[Required\]_\#     

The description of the schema.

_param _name _: str_ _\[Required\]_\#     

The name of the schema.

_param _type _: str_ _ = 'string'_\#     

The type of the response.

__On this page