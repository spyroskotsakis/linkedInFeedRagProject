# AIPluginToolSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.plugin.AIPluginToolSchema.html
**Word Count:** 41
**Links Count:** 409
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# AIPluginToolSchema\#

_class _langchain\_community.tools.plugin.AIPluginToolSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/plugin.html#AIPluginToolSchema)\#     

Bases: `BaseModel`

Schema for AIPluginTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tool\_input _: str | None_ _ = ''_\#     

__On this page