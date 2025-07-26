# TavilySearchAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.tavily_search.TavilySearchAPIWrapper.html
**Word Count:** 207
**Links Count:** 266
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# TavilySearchAPIWrapper\#

_class _langchain\_community.utilities.tavily\_search.TavilySearchAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/tavily_search.html#TavilySearchAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Tavily Search API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tavily\_api\_key _: SecretStr_ _\[Required\]_\#     

clean\_results\(

    _results : List\[Dict\]_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/tavily_search.html#TavilySearchAPIWrapper.clean_results)\#     

Clean results from Tavily Search API.

Parameters:     

**results** \(_List_ _\[__Dict_ _\]_\)

Return type:     

_List_\[_Dict_\]

raw\_results\(

    _query : str_,     _max\_results : int | None = 5_,     _search\_depth : str | None = 'advanced'_,     _include\_domains : List\[str\] | None = \[\]_,     _exclude\_domains : List\[str\] | None = \[\]_,     _include\_answer : bool | None = False_,     _include\_raw\_content : bool | None = False_,     _include\_images : bool | None = False_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/tavily_search.html#TavilySearchAPIWrapper.raw_results)\#     

Parameters:     

  * **query** \(_str_\)

  * **max\_results** \(_int_ _|__None_\)

  * **search\_depth** \(_str_ _|__None_\)

  * **include\_domains** \(_List_ _\[__str_ _\]__|__None_\)

  * **exclude\_domains** \(_List_ _\[__str_ _\]__|__None_\)

  * **include\_answer** \(_bool_ _|__None_\)

  * **include\_raw\_content** \(_bool_ _|__None_\)

  * **include\_images** \(_bool_ _|__None_\)

Return type:     

_Dict_

_async _raw\_results\_async\(

    _query : str_,     _max\_results : int | None = 5_,     _search\_depth : str | None = 'advanced'_,     _include\_domains : List\[str\] | None = \[\]_,     _exclude\_domains : List\[str\] | None = \[\]_,     _include\_answer : bool | None = False_,     _include\_raw\_content : bool | None = False_,     _include\_images : bool | None = False_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/tavily_search.html#TavilySearchAPIWrapper.raw_results_async)\#     

Get results from the Tavily Search API asynchronously.

Parameters:     

  * **query** \(_str_\)

  * **max\_results** \(_int_ _|__None_\)

  * **search\_depth** \(_str_ _|__None_\)

  * **include\_domains** \(_List_ _\[__str_ _\]__|__None_\)

  * **exclude\_domains** \(_List_ _\[__str_ _\]__|__None_\)

  * **include\_answer** \(_bool_ _|__None_\)

  * **include\_raw\_content** \(_bool_ _|__None_\)

  * **include\_images** \(_bool_ _|__None_\)

Return type:     

_Dict_

results\(

    _query : str_,     _max\_results : int | None = 5_,     _search\_depth : str | None = 'advanced'_,     _include\_domains : List\[str\] | None = \[\]_,     _exclude\_domains : List\[str\] | None = \[\]_,     _include\_answer : bool | None = False_,     _include\_raw\_content : bool | None = False_,     _include\_images : bool | None = False_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/tavily_search.html#TavilySearchAPIWrapper.results)\#     

Run query through Tavily Search and return metadata.

Parameters:     

  * **query** \(_str_\) – The query to search for.

  * **max\_results** \(_int_ _|__None_\) – The maximum number of results to return.

  * **search\_depth** \(_str_ _|__None_\) – The depth of the search. Can be “basic” or “advanced”.

  * **include\_domains** \(_List_ _\[__str_ _\]__|__None_\) – A list of domains to include in the search.

  * **exclude\_domains** \(_List_ _\[__str_ _\]__|__None_\) – A list of domains to exclude from the search.

  * **include\_answer** \(_bool_ _|__None_\) – Whether to include the answer in the results.

  * **include\_raw\_content** \(_bool_ _|__None_\) – Whether to include the raw content in the results.

  * **include\_images** \(_bool_ _|__None_\) – Whether to include images in the results.

Returns:     

The query that was searched for. follow\_up\_questions: A list of follow up questions. response\_time: The response time of the query. answer: The answer to the query. images: A list of images. results: A list of dictionaries containing the results:

> title: The title of the result. url: The url of the result. content: The content of the result. score: The score of the result. raw\_content: The raw content of the result.

Return type:     

query

_async _results\_async\(

    _query : str_,     _max\_results : int | None = 5_,     _search\_depth : str | None = 'advanced'_,     _include\_domains : List\[str\] | None = \[\]_,     _exclude\_domains : List\[str\] | None = \[\]_,     _include\_answer : bool | None = False_,     _include\_raw\_content : bool | None = False_,     _include\_images : bool | None = False_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/tavily_search.html#TavilySearchAPIWrapper.results_async)\#     

Parameters:     

  * **query** \(_str_\)

  * **max\_results** \(_int_ _|__None_\)

  * **search\_depth** \(_str_ _|__None_\)

  * **include\_domains** \(_List_ _\[__str_ _\]__|__None_\)

  * **exclude\_domains** \(_List_ _\[__str_ _\]__|__None_\)

  * **include\_answer** \(_bool_ _|__None_\)

  * **include\_raw\_content** \(_bool_ _|__None_\)

  * **include\_images** \(_bool_ _|__None_\)

Return type:     

_List_\[_Dict_\]

__On this page