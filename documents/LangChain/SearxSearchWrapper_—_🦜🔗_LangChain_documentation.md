# SearxSearchWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.searx_search.SearxSearchWrapper.html
**Word Count:** 331
**Links Count:** 281
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# SearxSearchWrapper\#

_class _langchain\_community.utilities.searx\_search.SearxSearchWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searx_search.html#SearxSearchWrapper)\#     

Bases: `BaseModel`

Wrapper for Searx API.

To use you need to provide the searx host by passing the named parameter `searx_host` or exporting the environment variable `SEARX_HOST`.

In some situations you might want to disable SSL verification, for example if you are running searx locally. You can do this by passing the named parameter `unsecure`. You can also pass the host url scheme as `http` to disable SSL.

Example               from langchain_community.utilities import SearxSearchWrapper     searx = SearxSearchWrapper(searx_host="http://localhost:8888")     

Example with SSL disabled:                    from langchain_community.utilities import SearxSearchWrapper     # note the unsecure parameter is not needed if you pass the url scheme as     # http     searx = SearxSearchWrapper(searx_host="http://localhost:8888",                                             unsecure=True)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aiosession _: Any | None_ _ = None_\#     

_param _categories _: List\[str\] | None_ _ = \[\]_\#     

_param _engines _: List\[str\] | None_ _ = \[\]_\#     

_param _headers _: dict | None_ _ = None_\#     

_param _k _: int_ _ = 10_\#     

_param _params _: dict_ _\[Optional\]_\#     

_param _query\_suffix _: str | None_ _ = ''_\#     

_param _searx\_host _: str_ _ = ''_\#     

_param _unsecure _: bool_ _ = False_\#     

_async _aresults\(

    _query : str_,     _num\_results : int_,     _engines : List\[str\] | None = None_,     _query\_suffix : str | None = ''_,     _\*\* kwargs: Any_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searx_search.html#SearxSearchWrapper.aresults)\#     

Asynchronously query with json results.

Uses aiohttp. See results for more info.

Parameters:     

  * **query** \(_str_\)

  * **num\_results** \(_int_\)

  * **engines** \(_List_ _\[__str_ _\]__|__None_\)

  * **query\_suffix** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_Dict_\]

_async _arun\(

    _query : str_,     _engines : List\[str\] | None = None_,     _query\_suffix : str | None = ''_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searx_search.html#SearxSearchWrapper.arun)\#     

Asynchronously version of run.

Parameters:     

  * **query** \(_str_\)

  * **engines** \(_List_ _\[__str_ _\]__|__None_\)

  * **query\_suffix** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

str

results\(

    _query : str_,     _num\_results : int_,     _engines : List\[str\] | None = None_,     _categories : List\[str\] | None = None_,     _query\_suffix : str | None = ''_,     _\*\* kwargs: Any_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searx_search.html#SearxSearchWrapper.results)\#     

Run query through Searx API and returns the results with metadata.

Parameters:     

  * **query** \(_str_\) – The query to search for.

  * **query\_suffix** \(_str_ _|__None_\) – Extra suffix appended to the query.

  * **num\_results** \(_int_\) – Limit the number of results to return.

  * **engines** \(_List_ _\[__str_ _\]__|__None_\) – List of engines to use for the query.

  * **categories** \(_List_ _\[__str_ _\]__|__None_\) – List of categories to use for the query.

  * **\*\*kwargs** \(_Any_\) – extra parameters to pass to the searx API.

Returns:     

\{     

snippet: The description of the result. title: The title of the result. link: The link to the result. engines: The engines used for the result. category: Searx category of the result.

\}

Return type:     

Dict with the following keys

run\(

    _query : str_,     _engines : List\[str\] | None = None_,     _categories : List\[str\] | None = None_,     _query\_suffix : str | None = ''_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/searx_search.html#SearxSearchWrapper.run)\#     

Run query through Searx API and parse results.

You can pass any other params to the searx query API.

Parameters:     

  * **query** \(_str_\) – The query to search for.

  * **query\_suffix** \(_str_ _|__None_\) – Extra suffix appended to the query.

  * **engines** \(_List_ _\[__str_ _\]__|__None_\) – List of engines to use for the query.

  * **categories** \(_List_ _\[__str_ _\]__|__None_\) – List of categories to use for the query.

  * **\*\*kwargs** \(_Any_\) – extra parameters to pass to the searx API.

Returns:     

The result of the query.

Return type:     

str

Raises:     

**ValueError** – If an error occurred with the query.

Example

This will make a query to the qwant engine:               from langchain_community.utilities import SearxSearchWrapper     searx = SearxSearchWrapper(searx_host="http://my.searx.host")     searx.run("what is the weather in France ?", engine="qwant")          # the same result can be achieved using the `!` syntax of searx     # to select the engine using `query_suffix`     searx.run("what is the weather in France ?", query_suffix="!qwant")     

Examples using SearxSearchWrapper

  * [SearxNG Search](https://python.langchain.com/docs/integrations/tools/searx_search/)

  * [SearxNG Search API](https://python.langchain.com/docs/integrations/providers/searx/)

__On this page