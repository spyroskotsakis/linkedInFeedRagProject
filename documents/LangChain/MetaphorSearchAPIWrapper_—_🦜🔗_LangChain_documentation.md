# MetaphorSearchAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.metaphor_search.MetaphorSearchAPIWrapper.html
**Word Count:** 206
**Links Count:** 259
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# MetaphorSearchAPIWrapper\#

_class _langchain\_community.utilities.metaphor\_search.MetaphorSearchAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/metaphor_search.html#MetaphorSearchAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Metaphor Search API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _k _: int_ _ = 10_\#     

_param _metaphor\_api\_key _: str_ _\[Required\]_\#     

results\(

    _query : str_,     _num\_results : int_,     _include\_domains : List\[str\] | None = None_,     _exclude\_domains : List\[str\] | None = None_,     _start\_crawl\_date : str | None = None_,     _end\_crawl\_date : str | None = None_,     _start\_published\_date : str | None = None_,     _end\_published\_date : str | None = None_,     _use\_autoprompt : bool | None = None_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/metaphor_search.html#MetaphorSearchAPIWrapper.results)\#     

Run query through Metaphor Search and return metadata.

Parameters:     

  * **query** \(_str_\) – The query to search for.

  * **num\_results** \(_int_\) – The number of results to return.

  * **include\_domains** \(_List_ _\[__str_ _\]__|__None_\) – A list of domains to include in the search. Only one of include\_domains and exclude\_domains should be defined.

  * **exclude\_domains** \(_List_ _\[__str_ _\]__|__None_\) – A list of domains to exclude from the search. Only one of include\_domains and exclude\_domains should be defined.

  * **start\_crawl\_date** \(_str_ _|__None_\) – If specified, only pages we crawled after start\_crawl\_date will be returned.

  * **end\_crawl\_date** \(_str_ _|__None_\) – If specified, only pages we crawled before end\_crawl\_date will be returned.

  * **start\_published\_date** \(_str_ _|__None_\) – If specified, only pages published after start\_published\_date will be returned.

  * **end\_published\_date** \(_str_ _|__None_\) – If specified, only pages published before end\_published\_date will be returned.

  * **use\_autoprompt** \(_bool_ _|__None_\) – If true, we turn your query into a more Metaphor-friendly query. Adds latency.

Returns:     

title - The title of the page url - The url author - Author of the content, if applicable. Otherwise, None. published\_date - Estimated date published

> in YYYY-MM-DD format. Otherwise, None.

Return type:     

A list of dictionaries with the following keys

_async _results\_async\(

    _query : str_,     _num\_results : int_,     _include\_domains : List\[str\] | None = None_,     _exclude\_domains : List\[str\] | None = None_,     _start\_crawl\_date : str | None = None_,     _end\_crawl\_date : str | None = None_,     _start\_published\_date : str | None = None_,     _end\_published\_date : str | None = None_,     _use\_autoprompt : bool | None = None_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/metaphor_search.html#MetaphorSearchAPIWrapper.results_async)\#     

Get results from the Metaphor Search API asynchronously.

Parameters:     

  * **query** \(_str_\)

  * **num\_results** \(_int_\)

  * **include\_domains** \(_List_ _\[__str_ _\]__|__None_\)

  * **exclude\_domains** \(_List_ _\[__str_ _\]__|__None_\)

  * **start\_crawl\_date** \(_str_ _|__None_\)

  * **end\_crawl\_date** \(_str_ _|__None_\)

  * **start\_published\_date** \(_str_ _|__None_\)

  * **end\_published\_date** \(_str_ _|__None_\)

  * **use\_autoprompt** \(_bool_ _|__None_\)

Return type:     

_List_\[_Dict_\]

__On this page