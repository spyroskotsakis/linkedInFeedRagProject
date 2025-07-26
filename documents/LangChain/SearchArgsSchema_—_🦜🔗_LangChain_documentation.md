# SearchArgsSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.gmail.get_message.SearchArgsSchema.html
**Word Count:** 51
**Links Count:** 409
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# SearchArgsSchema\#

_class _langchain\_community.tools.gmail.get\_message.SearchArgsSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/gmail/get_message.html#SearchArgsSchema)\#     

Bases: `BaseModel`

Input for GetMessageTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _message\_id _: str_ _\[Required\]_\#     

The unique ID of the email message, retrieved from a search.

__On this page