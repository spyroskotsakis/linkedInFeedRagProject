# RememberizerAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.rememberizer.RememberizerAPIWrapper.html
**Word Count:** 51
**Links Count:** 261
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# RememberizerAPIWrapper\#

_class _langchain\_community.utilities.rememberizer.RememberizerAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/rememberizer.html#RememberizerAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Rememberizer APIs.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _rememberizer\_api\_key _: str | None_ _ = None_\#     

_param _top\_k\_results _: int_ _ = 10_\#     

load\(

    _query : str_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/rememberizer.html#RememberizerAPIWrapper.load)\#     

Parameters:     

**query** \(_str_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

search\(_query : str_\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/rememberizer.html#RememberizerAPIWrapper.search)\#     

Search for a query in the Rememberizer API.

Parameters:     

**query** \(_str_\)

Return type:     

dict

__On this page