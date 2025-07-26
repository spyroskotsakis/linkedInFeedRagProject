# Reviver — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/load/langchain_core.load.load.Reviver.html
**Word Count:** 189
**Links Count:** 115
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# Reviver\#

_class _langchain\_core.load.load.Reviver\(

    _secrets\_map : dict\[str, str\] | None = None_,     _valid\_namespaces : list\[str\] | None = None_,     _secrets\_from\_env : bool = True_,     _additional\_import\_mappings : dict\[tuple\[str, ...\], tuple\[str, ...\]\] | None = None_,     _\*_ ,     _ignore\_unserializable\_fields : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/load/load.html#Reviver)\#     

Reviver for JSON objects.

Initialize the reviver.

Parameters:     

  * **secrets\_map** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – A map of secrets to load. If a secret is not found in the map, it will be loaded from the environment if secrets\_from\_env is True. Defaults to None.

  * **valid\_namespaces** \(_list_ _\[__str_ _\]__|__None_\) – A list of additional namespaces \(modules\) to allow to be deserialized. Defaults to None.

  * **secrets\_from\_env** \(_bool_\) – Whether to load secrets from the environment. Defaults to True.

  * **additional\_import\_mappings** \(_dict_ _\[__tuple_ _\[__str_ _,__...__\]__,__tuple_ _\[__str_ _,__...__\]__\]__|__None_\) – A dictionary of additional namespace mappings You can use this to override default mappings or add new mappings. Defaults to None.

  * **ignore\_unserializable\_fields** \(_bool_\) – Whether to ignore unserializable fields. Defaults to False.

Methods

`__init__`\(\[secrets\_map, valid\_namespaces, ...\]\) | Initialize the reviver.   ---|---      \_\_init\_\_\(

    _secrets\_map : dict\[str, str\] | None = None_,     _valid\_namespaces : list\[str\] | None = None_,     _secrets\_from\_env : bool = True_,     _additional\_import\_mappings : dict\[tuple\[str, ...\], tuple\[str, ...\]\] | None = None_,     _\*_ ,     _ignore\_unserializable\_fields : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/load/load.html#Reviver.__init__)\#     

Initialize the reviver.

Parameters:     

  * **secrets\_map** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – A map of secrets to load. If a secret is not found in the map, it will be loaded from the environment if secrets\_from\_env is True. Defaults to None.

  * **valid\_namespaces** \(_list_ _\[__str_ _\]__|__None_\) – A list of additional namespaces \(modules\) to allow to be deserialized. Defaults to None.

  * **secrets\_from\_env** \(_bool_\) – Whether to load secrets from the environment. Defaults to True.

  * **additional\_import\_mappings** \(_dict_ _\[__tuple_ _\[__str_ _,__...__\]__,__tuple_ _\[__str_ _,__...__\]__\]__|__None_\) – A dictionary of additional namespace mappings You can use this to override default mappings or add new mappings. Defaults to None.

  * **ignore\_unserializable\_fields** \(_bool_\) – Whether to ignore unserializable fields. Defaults to False.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)