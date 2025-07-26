# InfobipAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.infobip.InfobipAPIWrapper.html
**Word Count:** 47
**Links Count:** 257
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# InfobipAPIWrapper\#

_class _langchain\_community.utilities.infobip.InfobipAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/infobip.html#InfobipAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Infobip API for messaging.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _infobip\_api\_key _: str | None_ _ = None_\#     

_param _infobip\_base\_url _: str | None_ _ = 'https://api.infobip.com'_\#     

run\(

    _body : str = ''_,     _to : str = ''_,     _sender : str = ''_,     _subject : str = ''_,     _channel : str = 'sms'_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/infobip.html#InfobipAPIWrapper.run)\#     

Parameters:     

  * **body** \(_str_\)

  * **to** \(_str_\)

  * **sender** \(_str_\)

  * **subject** \(_str_\)

  * **channel** \(_str_\)

Return type:     

str

Examples using InfobipAPIWrapper

  * [Infobip](https://python.langchain.com/docs/integrations/tools/infobip/)

__On this page