# GoogleSerperAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_serper.GoogleSerperAPIWrapper.html
**Word Count:** 101
**Links Count:** 281
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# GoogleSerperAPIWrapper\#

_class _langchain\_community.utilities.google\_serper.GoogleSerperAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_serper.html#GoogleSerperAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around the Serper.dev Google Search API.

You can create a free API key at <https://serper.dev>.

To use, you should have the environment variable `SERPER_API_KEY` set with your API key, or pass serper\_api\_key as a named parameter to the constructor.

Example               from langchain_community.utilities import GoogleSerperAPIWrapper     google_serper = GoogleSerperAPIWrapper()     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aiosession _: ClientSession | None_ _ = None_\#     

_param _gl _: str_ _ = 'us'_\#     

_param _hl _: str_ _ = 'en'_\#     

_param _k _: int_ _ = 10_\#     

_param _result\_key\_for\_type _: dict_ _ = \{'images': 'images', 'news': 'news', 'places': 'places', 'search': 'organic'\}_\#     

_param _serper\_api\_key _: str | None_ _ = None_\#     

_param _tbs _: str | None_ _ = None_\#     

_param _type _: Literal\['news', 'search', 'places', 'images'\]__ = 'search'_\#     

_async _aresults\(

    _query : str_,     _\*\* kwargs: Any_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_serper.html#GoogleSerperAPIWrapper.aresults)\#     

Run query through GoogleSearch.

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_Dict_

_async _arun\(

    _query : str_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_serper.html#GoogleSerperAPIWrapper.arun)\#     

Run query through GoogleSearch and parse result async.

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str

results\(

    _query : str_,     _\*\* kwargs: Any_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_serper.html#GoogleSerperAPIWrapper.results)\#     

Run query through GoogleSearch.

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_Dict_

run\(

    _query : str_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_serper.html#GoogleSerperAPIWrapper.run)\#     

Run query through GoogleSearch and parse result.

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str

Examples using GoogleSerperAPIWrapper

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [Google Serper](https://python.langchain.com/docs/integrations/tools/google_serper/)

  * [Serper - Google Search API](https://python.langchain.com/docs/integrations/providers/google_serper/)

__On this page