# SleepInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.sleep.tool.SleepInput.html
**Word Count:** 45
**Links Count:** 409
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# SleepInput\#

_class _langchain\_community.tools.sleep.tool.SleepInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/sleep/tool.html#SleepInput)\#     

Bases: `BaseModel`

Input for CopyFileTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _sleep\_time _: int_ _\[Required\]_\#     

Time to sleep in seconds

__On this page