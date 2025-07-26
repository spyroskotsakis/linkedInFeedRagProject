# AIPlugin — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.plugin.AIPlugin.html
**Word Count:** 46
**Links Count:** 433
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# AIPlugin\#

_class _langchain\_community.tools.plugin.AIPlugin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/plugin.html#AIPlugin)\#     

Bases: `BaseModel`

AI Plugin Definition.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api _: [ApiConfig](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.plugin.ApiConfig.html#langchain_community.tools.plugin.ApiConfig "langchain_community.tools.plugin.ApiConfig")_ _\[Required\]_\#     

_param _auth _: dict | None_ _ = None_\#     

_param _contact\_email _: str | None_ _\[Required\]_\#     

_param _description\_for\_human _: str_ _\[Required\]_\#     

_param _description\_for\_model _: str_ _\[Required\]_\#     

_param _legal\_info\_url _: str | None_ _\[Required\]_\#     

_param _logo\_url _: str | None_ _\[Required\]_\#     

_param _name\_for\_human _: str_ _\[Required\]_\#     

_param _name\_for\_model _: str_ _\[Required\]_\#     

_param _schema\_version _: str_ _\[Required\]_\#     

_classmethod _from\_url\(

    _url : str_, \) → AIPlugin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/plugin.html#AIPlugin.from_url)\#     

Instantiate AIPlugin from a URL.

Parameters:     

**url** \(_str_\)

Return type:     

_AIPlugin_

__On this page