# MojeekSearchAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.mojeek_search.MojeekSearchAPIWrapper.html
**Word Count:** 40
**Links Count:** 258
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# MojeekSearchAPIWrapper\#

_class _langchain\_community.utilities.mojeek\_search.MojeekSearchAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/mojeek_search.html#MojeekSearchAPIWrapper)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_key _: str_ _\[Required\]_\#     

_param _api\_url _: str_ _ = 'https://api.mojeek.com/search'_\#     

_param _search\_kwargs _: dict_ _\[Optional\]_\#     

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/mojeek_search.html#MojeekSearchAPIWrapper.run)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

__On this page