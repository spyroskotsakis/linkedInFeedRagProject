# Requests — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html
**Word Count:** 155
**Links Count:** 288
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# Requests\#

_class _langchain\_community.utilities.requests.Requests[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests)\#     

Bases: `BaseModel`

Wrapper around requests to handle auth and async.

The main purpose of this wrapper is to handle authentication \(by saving headers\) and enable easy async methods on the same base object.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aiosession _: ClientSession | None_ _ = None_\#     

_param _auth _: Any | None_ _ = None_\#     

_param _headers _: Dict\[str, str\] | None_ _ = None_\#     

_param _verify _: bool | None_ _ = True_\#     

adelete\(

    _url : str_,     _\*\* kwargs: Any_, \) → AsyncGenerator\[ClientResponse, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.adelete)\#     

DELETE the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_AsyncGenerator_\[_ClientResponse_ , None\]

aget\(

    _url : str_,     _\*\* kwargs: Any_, \) → AsyncGenerator\[ClientResponse, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.aget)\#     

GET the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_AsyncGenerator_\[_ClientResponse_ , None\]

apatch\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → AsyncGenerator\[ClientResponse, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.apatch)\#     

PATCH the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_AsyncGenerator_\[_ClientResponse_ , None\]

apost\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → AsyncGenerator\[ClientResponse, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.apost)\#     

POST to the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_AsyncGenerator_\[_ClientResponse_ , None\]

aput\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → AsyncGenerator\[ClientResponse, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.aput)\#     

PUT the URL and return the text asynchronously.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_AsyncGenerator_\[_ClientResponse_ , None\]

delete\(

    _url : str_,     _\*\* kwargs: Any_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.delete)\#     

DELETE the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_Response_

get\(

    _url : str_,     _\*\* kwargs: Any_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.get)\#     

GET the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_Response_

patch\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.patch)\#     

PATCH the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Response_

post\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.post)\#     

POST to the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Response_

put\(

    _url : str_,     _data : Dict\[str, Any\]_,     _\*\* kwargs: Any_, \) → Response[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/requests.html#Requests.put)\#     

PUT the URL and return the text.

Parameters:     

  * **url** \(_str_\)

  * **data** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Response_

Examples using Requests

  * [Natural Language API Toolkits](https://python.langchain.com/docs/integrations/tools/openapi_nla/)

__On this page