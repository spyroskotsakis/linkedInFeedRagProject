# DataForSeoAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.dataforseo_api_search.DataForSeoAPIWrapper.html
**Word Count:** 122
**Links Count:** 278
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# DataForSeoAPIWrapper\#

_class _langchain\_community.utilities.dataforseo\_api\_search.DataForSeoAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dataforseo_api_search.html#DataForSeoAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around the DataForSeo API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aiosession _: ClientSession | None_ _ = None_\#     

The aiohttp session to use for the DataForSEO SERP API.

_param _api\_login _: str | None_ _ = None_\#     

The API login to use for the DataForSEO SERP API.

_param _api\_password _: str | None_ _ = None_\#     

The API password to use for the DataForSEO SERP API.

_param _default\_params _: dict_ _ = \{'depth': 10, 'language\_code': 'en', 'location\_name': 'United States', 'se\_name': 'google', 'se\_type': 'organic'\}_\#     

Default parameters to use for the DataForSEO SERP API.

_param _json\_result\_fields _: list | None_ _ = None_\#     

The JSON result fields.

_param _json\_result\_types _: list | None_ _ = None_\#     

The JSON result types.

_param _params _: dict_ _ = \{\}_\#     

Additional parameters to pass to the DataForSEO SERP API.

_param _top\_count _: int | None_ _ = None_\#     

The number of top results to return.

_async _aresults\(_url : str_\) → list[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dataforseo_api_search.html#DataForSeoAPIWrapper.aresults)\#     

Parameters:     

**url** \(_str_\)

Return type:     

list

_async _arun\(_url : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dataforseo_api_search.html#DataForSeoAPIWrapper.arun)\#     

Run request to DataForSEO SERP API and parse result async.

Parameters:     

**url** \(_str_\)

Return type:     

str

results\(_url : str_\) → list[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dataforseo_api_search.html#DataForSeoAPIWrapper.results)\#     

Parameters:     

**url** \(_str_\)

Return type:     

list

run\(_url : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dataforseo_api_search.html#DataForSeoAPIWrapper.run)\#     

Run request to DataForSEO SERP API and parse result async.

Parameters:     

**url** \(_str_\)

Return type:     

str

Examples using DataForSeoAPIWrapper

  * [DataForSEO](https://python.langchain.com/docs/integrations/providers/dataforseo/)

__On this page