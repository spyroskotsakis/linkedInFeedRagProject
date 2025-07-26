# ExecJavaScriptInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.riza.command.ExecJavaScriptInput.html
**Word Count:** 43
**Links Count:** 409
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# ExecJavaScriptInput\#

_class _langchain\_community.tools.riza.command.ExecJavaScriptInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/riza/command.html#ExecJavaScriptInput)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _code _: str_ _\[Required\]_\#     

the JavaScript code to execute

__On this page