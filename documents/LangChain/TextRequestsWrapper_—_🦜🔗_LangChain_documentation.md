# TextRequestsWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.TextRequestsWrapper.html
**Word Count:** 148
**Links Count:** 284
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# TextRequestsWrapper\#

_class _langchain\_community.utilities.requests.TextRequestsWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#TextRequestsWrapper)\#     

Bases: [`GenericRequestsWrapper`](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.GenericRequestsWrapper.html#langchain_community.utilities.requests.GenericRequestsWrapper "langchain_community.utilities.requests.GenericRequestsWrapper")

Lightweight wrapper around requests library, with async support.

The main purpose of this wrapper is to always return a text output.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aiosession _: aiohttp.ClientSession | None_ _ = None_\#     

_param _auth _: Any | None_ _ = None_\#     

_param _headers _: Dict\[str, str\] | None_ _ = None_\#     

_param _response\_content\_type _: Literal\['text', 'json'\]__ = 'text'_\#     

_param _verify _: bool_ _ = True_\#     

_async _adelete\(

    _url : str_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

DELETE the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

_async _aget\(

    _url : str_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

GET the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

_async _apatch\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

PATCH the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

_async _apost\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

POST to the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

_async _aput\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

PUT the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

delete\(

    _url : str_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

DELETE the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

get\(

    _url : str_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

GET the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

patch\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

PATCH the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

post\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

POST to the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

put\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → str | Dict\[str, Any\]\#     

PUT the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

str | _Dict_\[str, _Any_\]

_property _requests _: [Requests](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html#langchain_community.utilities.requests.Requests "langchain_community.utilities.requests.Requests")_\#     

Examples using TextRequestsWrapper

  * [Requests Toolkit](https://python.langchain.com/docs/integrations/tools/requests/)

__On this page