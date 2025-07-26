# NUASchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nuclia.tool.NUASchema.html
**Word Count:** 91
**Links Count:** 423
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# NUASchema\#

_class _langchain\_community.tools.nuclia.tool.NUASchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/nuclia/tool.html#NUASchema)\#     

Bases: `BaseModel`

Input for Nuclia Understanding API.

action\#     

Action to perform. Either push or pull.

id\#     

ID of the file to push or pull.

path\#     

Path to the file to push \(needed only for push action\).

text\#     

Text content to process \(needed only for push action\).

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _action _: str_ _\[Required\]_\#     

Action to perform. Either push or pull.

_param _id _: str_ _\[Required\]_\#     

ID of the file to push or pull.

_param _path _: str | None_ _\[Required\]_\#     

Path to the file to push \(needed only for push action\).

_param _text _: str | None_ _\[Required\]_\#     

Text content to process \(needed only for push action\).

__On this page