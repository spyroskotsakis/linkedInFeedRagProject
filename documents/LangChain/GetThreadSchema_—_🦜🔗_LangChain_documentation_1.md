# GetThreadSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/gmail/langchain_google_community.gmail.get_thread.GetThreadSchema.html
**Word Count:** 43
**Links Count:** 106
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# GetThreadSchema\#

_class _langchain\_google\_community.gmail.get\_thread.GetThreadSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/gmail/get_thread.html#GetThreadSchema)\#     

Bases: `BaseModel`

Input for GetMessageTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _thread\_id _: str_ _\[Required\]_\#     

The thread ID.

__On this page