# get_openai_token_cost_for_model — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.openai_info.get_openai_token_cost_for_model.html
**Word Count:** 53
**Links Count:** 183
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# get\_openai\_token\_cost\_for\_model\#

langchain\_community.callbacks.openai\_info.get\_openai\_token\_cost\_for\_model\(

    _model\_name : str_,     _num\_tokens : int_,     _is\_completion : bool = False_,     _\*_ ,     _token\_type : [TokenType](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.openai_info.TokenType.html#langchain_community.callbacks.openai_info.TokenType "langchain_community.callbacks.openai_info.TokenType") = TokenType.PROMPT_, \) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/openai_info.html#get_openai_token_cost_for_model)\#     

Get the cost in USD for a given model and number of tokens.

Parameters:     

  * **model\_name** \(_str_\) – Name of the model

  * **num\_tokens** \(_int_\) – Number of tokens.

  * **is\_completion** \(_bool_\) – Whether the model is used for completion or not. Defaults to False. Deprecated in favor of `token_type`.

  * **token\_type** \([_TokenType_](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.openai_info.TokenType.html#langchain_community.callbacks.openai_info.TokenType "langchain_community.callbacks.openai_info.TokenType")\) – Token type. Defaults to `TokenType.PROMPT`.

Returns:     

Cost in USD.

Return type:     

float

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)