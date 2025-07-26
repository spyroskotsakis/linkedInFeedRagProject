# PythonInputs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/tools/langchain_experimental.tools.python.tool.PythonInputs.html
**Word Count:** 43
**Links Count:** 100
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# PythonInputs\#

_class _langchain\_experimental.tools.python.tool.PythonInputs[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tools/python/tool.html#PythonInputs)\#     

Bases: `BaseModel`

Python inputs.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

code snippet to run

__On this page