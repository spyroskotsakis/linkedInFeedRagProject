# Action — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Action.html
**Word Count:** 41
**Links Count:** 425
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# Action\#

_class _langchain\_community.tools.connery.models.Action[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/connery/models.html#Action)\#     

Bases: `BaseModel`

Connery Action model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _description _: str | None_ _ = None_\#     

_param _id _: str_ _\[Required\]_\#     

_param _inputParameters _: List\[[Parameter](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html#langchain_community.tools.connery.models.Parameter "langchain_community.tools.connery.models.Parameter")\]__\[Required\]_\#     

_param _key _: str_ _\[Required\]_\#     

_param _outputParameters _: List\[[Parameter](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html#langchain_community.tools.connery.models.Parameter "langchain_community.tools.connery.models.Parameter")\]__\[Required\]_\#     

_param _pluginId _: str_ _\[Required\]_\#     

_param _title _: str_ _\[Required\]_\#     

_param _type _: str_ _\[Required\]_\#     

__On this page