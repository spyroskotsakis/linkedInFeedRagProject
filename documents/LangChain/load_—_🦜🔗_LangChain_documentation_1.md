# load — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/load/langchain_core.load.load.load.html
**Word Count:** 141
**Links Count:** 112
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# load\#

langchain\_core.load.load.load\(

    _obj : Any_,     _\*_ ,     _secrets\_map : dict\[str, str\] | None = None_,     _valid\_namespaces : list\[str\] | None = None_,     _secrets\_from\_env : bool = True_,     _additional\_import\_mappings : dict\[tuple\[str, ...\], tuple\[str, ...\]\] | None = None_,     _ignore\_unserializable\_fields : bool = False_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/load/load.html#load)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Revive a LangChain class from a JSON object.

Use this if you already have a parsed JSON object, eg. from json.load or orjson.loads.

Parameters:     

  * **obj** \(_Any_\) – The object to load.

  * **secrets\_map** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – A map of secrets to load. If a secret is not found in the map, it will be loaded from the environment if secrets\_from\_env is True. Defaults to None.

  * **valid\_namespaces** \(_list_ _\[__str_ _\]__|__None_\) – A list of additional namespaces \(modules\) to allow to be deserialized. Defaults to None.

  * **secrets\_from\_env** \(_bool_\) – Whether to load secrets from the environment. Defaults to True.

  * **additional\_import\_mappings** \(_dict_ _\[__tuple_ _\[__str_ _,__...__\]__,__tuple_ _\[__str_ _,__...__\]__\]__|__None_\) – A dictionary of additional namespace mappings You can use this to override default mappings or add new mappings. Defaults to None.

  * **ignore\_unserializable\_fields** \(_bool_\) – Whether to ignore unserializable fields. Defaults to False.

Returns:     

Revived LangChain objects.

Return type:     

_Any_

Examples using load

  * [How to save and load LangChain objects](https://python.langchain.com/docs/how_to/serialization/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)