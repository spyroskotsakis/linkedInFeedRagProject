# standardize_model_name — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.standardize_model_name.html
**Word Count:** 42
**Links Count:** 76
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# standardize\_model\_name\#

langchain\_nvidia\_ai\_endpoints.callbacks.standardize\_model\_name\(

    _model\_name : str_,     _price\_map : dict = \{\}_,     _is\_completion : bool = False_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/callbacks.html#standardize_model_name)\#     

Standardize the model name to a format that can be used in the OpenAI API.

Parameters:     

  * **model\_name** \(_str_\) – Model name to standardize.

  * **is\_completion** \(_bool_\) – Whether the model is used for completion or not. Defaults to False.

  * **price\_map** \(_dict_\)

Returns:     

Standardized model name.

Return type:     

str

__On this page