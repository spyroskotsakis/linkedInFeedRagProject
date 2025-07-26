# SearchApiAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.searchapi.SearchApiAPIWrapper.html
**Word Count:** 67
**Links Count:** 269
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# SearchApiAPIWrapper\#

_class _langchain\_community.utilities.searchapi.SearchApiAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searchapi.html#SearchApiAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around SearchApi API.

To use, you should have the environment variable `SEARCHAPI_API_KEY` set with your API key, or pass searchapi\_api\_key as a named parameter to the constructor.

Example               from langchain_community.utilities import SearchApiAPIWrapper     searchapi = SearchApiAPIWrapper()     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aiosession _: ClientSession | None_ _ = None_\#     

_param _engine _: str_ _ = 'google'_\#     

_param _searchapi\_api\_key _: str | None_ _ = None_\#     

_async _aresults\(

    _query : str_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searchapi.html#SearchApiAPIWrapper.aresults)\#     

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

dict

_async _arun\(

    _query : str_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searchapi.html#SearchApiAPIWrapper.arun)\#     

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str

results\(

    _query : str_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searchapi.html#SearchApiAPIWrapper.results)\#     

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

dict

run\(

    _query : str_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searchapi.html#SearchApiAPIWrapper.run)\#     

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str

Examples using SearchApiAPIWrapper

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [SearchApi](https://python.langchain.com/docs/integrations/providers/searchapi/)

__On this page