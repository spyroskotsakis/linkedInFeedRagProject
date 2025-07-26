# GetThreadSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.gmail.get_thread.GetThreadSchema.html
**Word Count:** 43
**Links Count:** 409
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# GetThreadSchema\#

_class _langchain\_community.tools.gmail.get\_thread.GetThreadSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/gmail/get_thread.html#GetThreadSchema)\#     

Bases: `BaseModel`

Input for GetMessageTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _thread\_id _: str_ _\[Required\]_\#     

The thread ID.

__On this page