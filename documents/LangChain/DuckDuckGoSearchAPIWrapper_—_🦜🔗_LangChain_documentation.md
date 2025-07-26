# DuckDuckGoSearchAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.duckduckgo_search.DuckDuckGoSearchAPIWrapper.html
**Word Count:** 126
**Links Count:** 269
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# DuckDuckGoSearchAPIWrapper\#

_class _langchain\_community.utilities.duckduckgo\_search.DuckDuckGoSearchAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/duckduckgo_search.html#DuckDuckGoSearchAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for DuckDuckGo Search API.

Free and does not require any setup.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _backend _: str_ _ = 'auto'_\#     

Options: auto, html, lite

_param _max\_results _: int_ _ = 5_\#     

_param _region _: str | None_ _ = 'wt-wt'_\#     

See <https://pypi.org/project/duckduckgo-search/#regions>

_param _safesearch _: str_ _ = 'moderate'_\#     

Options: strict, moderate, off

_param _source _: str_ _ = 'text'_\#     

Options: text, news, images

_param _time _: str | None_ _ = 'y'_\#     

Options: d, w, m, y

results\(

    _query : str_,     _max\_results : int_,     _source : str | None = None_, \) → List\[Dict\[str, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/duckduckgo_search.html#DuckDuckGoSearchAPIWrapper.results)\#     

Run query through DuckDuckGo and return metadata.

Parameters:     

  * **query** \(_str_\) – The query to search for.

  * **max\_results** \(_int_\) – The number of results to return.

  * **source** \(_str_ _|__None_\) – The source to look from.

Returns:     

snippet - The description of the result. title - The title of the result. link - The link to the result.

Return type:     

A list of dictionaries with the following keys

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/duckduckgo_search.html#DuckDuckGoSearchAPIWrapper.run)\#     

Run query through DuckDuckGo and return concatenated results.

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using DuckDuckGoSearchAPIWrapper

  * [DuckDuckGo Search](https://python.langchain.com/docs/integrations/tools/ddg/)

__On this page