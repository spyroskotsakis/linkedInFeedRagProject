# get_token_cost_for_model — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.get_token_cost_for_model.html
**Word Count:** 61
**Links Count:** 77
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# get\_token\_cost\_for\_model\#

langchain\_nvidia\_ai\_endpoints.callbacks.get\_token\_cost\_for\_model\(

    _model\_name : str_,     _num\_tokens : int_,     _price\_map : dict_,     _is\_completion : bool = False_, \) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/callbacks.html#get_token_cost_for_model)\#     

Get the cost in USD for a given model and number of tokens.

Parameters:     

  * **model\_name** \(_str_\) – Name of the model

  * **num\_tokens** \(_int_\) – Number of tokens.

  * **price\_map** \(_dict_\) – Map of model names to cost per 1000 tokens. Defaults to AI Foundation Endpoint pricing per <https://www.together.ai/pricing>.

  * **is\_completion** \(_bool_\) – Whether the model is used for completion or not. Defaults to False.

Returns:     

Cost in USD.

Return type:     

float

__On this page