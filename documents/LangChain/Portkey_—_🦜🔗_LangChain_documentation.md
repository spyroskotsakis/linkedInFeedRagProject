# Portkey — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.portkey.Portkey.html
**Word Count:** 21
**Links Count:** 257
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# Portkey\#

_class _langchain\_community.utilities.portkey.Portkey[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/portkey.html#Portkey)\#     

Portkey configuration.

base\#     

The base URL for the Portkey API. Default: “<https://api.portkey.ai/v1/proxy>”

Type:     

str

Attributes

`base` |    ---|---      Methods

`Config`\(api\_key\[, trace\_id, environment, ...\]\) |    ---|---      _static _Config\(

    _api\_key : str_,     _trace\_id : str | None = None_,     _environment : str | None = None_,     _user : str | None = None_,     _organisation : str | None = None_,     _prompt : str | None = None_,     _retry\_count : int | None = None_,     _cache : str | None = None_,     _cache\_force\_refresh : str | None = None_,     _cache\_age : int | None = None_, \) → Dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/portkey.html#Portkey.Config)\#     

Parameters:     

  * **api\_key** \(_str_\)

  * **trace\_id** \(_str_ _|__None_\)

  * **environment** \(_str_ _|__None_\)

  * **user** \(_str_ _|__None_\)

  * **organisation** \(_str_ _|__None_\)

  * **prompt** \(_str_ _|__None_\)

  * **retry\_count** \(_int_ _|__None_\)

  * **cache** \(_str_ _|__None_\)

  * **cache\_force\_refresh** \(_str_ _|__None_\)

  * **cache\_age** \(_int_ _|__None_\)

Return type:     

_Dict_\[str, str\]

__On this page