# get_from_dict_or_env — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.env.get_from_dict_or_env.html
**Word Count:** 81
**Links Count:** 166
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# get\_from\_dict\_or\_env\#

langchain\_core.utils.env.get\_from\_dict\_or\_env\(

    _data : dict\[str, Any\]_,     _key : str | list\[str\]_,     _env\_key : str_,     _default : str | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/env.html#get_from_dict_or_env)\#     

Get a value from a dictionary or an environment variable.

Parameters:     

  * **data** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The dictionary to look up the key in.

  * **key** \(_str_ _|__list_ _\[__str_ _\]_\) – The key to look up in the dictionary. This can be a list of keys to try in order.

  * **env\_key** \(_str_\) – The environment variable to look up if the key is not in the dictionary.

  * **default** \(_str_ _|__None_\) – The default value to return if the key is not in the dictionary or the environment. Defaults to None.

Return type:     

str

__On this page