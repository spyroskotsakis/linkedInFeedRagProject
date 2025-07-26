# BingSearchAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.bing_search.BingSearchAPIWrapper.html
**Word Count:** 109
**Links Count:** 265
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# BingSearchAPIWrapper\#

_class _langchain\_community.utilities.bing\_search.BingSearchAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/bing_search.html#BingSearchAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Bing Web Search API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _bing\_search\_url _: str_ _\[Required\]_\#     

_param _bing\_subscription\_key _: str_ _\[Required\]_\#     

_param _k _: int_ _ = 10_\#     

_param _search\_kwargs _: dict_ _\[Optional\]_\#     

Additional keyword arguments to pass to the search request.

results\(

    _query : str_,     _num\_results : int_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/bing_search.html#BingSearchAPIWrapper.results)\#     

Run query through BingSearch and return metadata.

Parameters:     

  * **query** \(_str_\) – The query to search for.

  * **num\_results** \(_int_\) – The number of results to return.

Returns:     

snippet - The description of the result. title - The title of the result. link - The link to the result.

Return type:     

A list of dictionaries with the following keys

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/bing_search.html#BingSearchAPIWrapper.run)\#     

Run query through BingSearch and parse result.

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using BingSearchAPIWrapper

  * [Bing Search](https://python.langchain.com/docs/integrations/tools/bing_search/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page