# SerpAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.serpapi.SerpAPIWrapper.html
**Word Count:** 107
**Links Count:** 273
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# SerpAPIWrapper\#

_class _langchain\_community.utilities.serpapi.SerpAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/serpapi.html#SerpAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around SerpAPI.

To use, you should have the `google-search-results` python package installed, and the environment variable `SERPAPI_API_KEY` set with your API key, or pass serpapi\_api\_key as a named parameter to the constructor.

Example               from langchain_community.utilities import SerpAPIWrapper     serpapi = SerpAPIWrapper()     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aiosession _: ClientSession | None_ _ = None_\#     

_param _params _: dict_ _ = \{'engine': 'google', 'gl': 'us', 'google\_domain': 'google.com', 'hl': 'en'\}_\#     

_param _serpapi\_api\_key _: str | None_ _ = None_\#     

_async _aresults\(_query : str_\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/serpapi.html#SerpAPIWrapper.aresults)\#     

Use aiohttp to run query through SerpAPI and return the results async.

Parameters:     

**query** \(_str_\)

Return type:     

dict

_async _arun\(

    _query : str_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/serpapi.html#SerpAPIWrapper.arun)\#     

Run query through SerpAPI and parse result async.

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str

get\_params\(

    _query : str_, \) → Dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/serpapi.html#SerpAPIWrapper.get_params)\#     

Get parameters for SerpAPI.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_\[str, str\]

results\(_query : str_\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/serpapi.html#SerpAPIWrapper.results)\#     

Run query through SerpAPI and return the raw result.

Parameters:     

**query** \(_str_\)

Return type:     

dict

run\(_query : str_, _\*\* kwargs: Any_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/serpapi.html#SerpAPIWrapper.run)\#     

Run query through SerpAPI and parse result.

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str

Examples using SerpAPIWrapper

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [MLX](https://python.langchain.com/docs/integrations/chat/mlx/)

  * [SerpAPI](https://python.langchain.com/docs/integrations/providers/serpapi/)

__On this page