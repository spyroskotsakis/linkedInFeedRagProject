# get_from_env — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.env.get_from_env.html
**Word Count:** 90
**Links Count:** 167
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# get\_from\_env\#

langchain\_core.utils.env.get\_from\_env\(

    _key : str_,     _env\_key : str_,     _default : str | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/env.html#get_from_env)\#     

Get a value from a dictionary or an environment variable.

Parameters:     

  * **key** \(_str_\) – The key to look up in the dictionary.

  * **env\_key** \(_str_\) – The environment variable to look up if the key is not in the dictionary.

  * **default** \(_str_ _|__None_\) – The default value to return if the key is not in the dictionary or the environment. Defaults to None.

Returns:     

The value of the key.

Return type:     

str

Raises:     

**ValueError** – If the key is not in the dictionary and no default value is provided or if the environment variable is not set.

Examples using get\_from\_env

  * [Passio NutritionAI](https://python.langchain.com/docs/integrations/tools/passio_nutrition_ai/)

__On this page