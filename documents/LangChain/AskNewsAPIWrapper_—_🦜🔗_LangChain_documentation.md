# AskNewsAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.asknews.AskNewsAPIWrapper.html
**Word Count:** 64
**Links Count:** 259
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# AskNewsAPIWrapper\#

_class _langchain\_community.utilities.asknews.AskNewsAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/asknews.html#AskNewsAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for AskNews API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _asknews\_client\_id _: str | None_ _ = None_\#     

Client ID for the AskNews API.

_param _asknews\_client\_secret _: str | None_ _ = None_\#     

Client Secret for the AskNews API.

_async _asearch\_news\(

    _query : str_,     _max\_results : int = 10_,     _hours\_back : int = 0_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/asknews.html#AskNewsAPIWrapper.asearch_news)\#     

Search news in AskNews API asynchronously.

Parameters:     

  * **query** \(_str_\)

  * **max\_results** \(_int_\)

  * **hours\_back** \(_int_\)

Return type:     

str

search\_news\(

    _query : str_,     _max\_results : int = 10_,     _hours\_back : int = 0_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/asknews.html#AskNewsAPIWrapper.search_news)\#     

Search news in AskNews API synchronously.

Parameters:     

  * **query** \(_str_\)

  * **max\_results** \(_int_\)

  * **hours\_back** \(_int_\)

Return type:     

str

__On this page