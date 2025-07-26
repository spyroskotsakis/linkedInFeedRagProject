# ToolInputSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/sema4/toolkits/langchain_sema4.toolkits.ToolInputSchema.html
**Word Count:** 41
**Links Count:** 75
**Scraped:** 2025-07-21 07:58:35
**Status:** completed

---

# ToolInputSchema\#

_class _langchain\_sema4.toolkits.ToolInputSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sema4/toolkits.html#ToolInputSchema)\#     

Bases: `BaseModel`

Tool input schema.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _question _: str_ _\[Required\]_\#     

__On this page