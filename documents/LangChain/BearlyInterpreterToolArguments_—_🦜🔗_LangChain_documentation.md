# BearlyInterpreterToolArguments — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.bearly.tool.BearlyInterpreterToolArguments.html
**Word Count:** 61
**Links Count:** 409
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# BearlyInterpreterToolArguments\#

_class _langchain\_community.tools.bearly.tool.BearlyInterpreterToolArguments[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/bearly/tool.html#BearlyInterpreterToolArguments)\#     

Bases: `BaseModel`

Arguments for the BearlyInterpreterTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _python\_code _: str_ _\[Required\]_\#     

The pure python script to be evaluated. The contents will be in main.py. It should not be in markdown format.

__On this page