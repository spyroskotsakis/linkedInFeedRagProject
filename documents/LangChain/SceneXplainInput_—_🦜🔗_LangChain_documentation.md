# SceneXplainInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.scenexplain.tool.SceneXplainInput.html
**Word Count:** 47
**Links Count:** 409
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# SceneXplainInput\#

_class _langchain\_community.tools.scenexplain.tool.SceneXplainInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/scenexplain/tool.html#SceneXplainInput)\#     

Bases: `BaseModel`

Input for SceneXplain.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

The link to the image to explain

__On this page