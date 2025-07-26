# standardize_model_name — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.openai_info.standardize_model_name.html
**Word Count:** 51
**Links Count:** 183
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# standardize\_model\_name\#

langchain\_community.callbacks.openai\_info.standardize\_model\_name\(

    _model\_name : str_,     _is\_completion : bool = False_,     _\*_ ,     _token\_type : [TokenType](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.openai_info.TokenType.html#langchain_community.callbacks.openai_info.TokenType "langchain_community.callbacks.openai_info.TokenType") = TokenType.PROMPT_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/openai_info.html#standardize_model_name)\#     

Standardize the model name to a format that can be used in the OpenAI API.

Parameters:     

  * **model\_name** \(_str_\) – Model name to standardize.

  * **is\_completion** \(_bool_\) – Whether the model is used for completion or not. Defaults to False. Deprecated in favor of `token_type`.

  * **token\_type** \([_TokenType_](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.openai_info.TokenType.html#langchain_community.callbacks.openai_info.TokenType "langchain_community.callbacks.openai_info.TokenType")\) – Token type. Defaults to `TokenType.PROMPT`.

Returns:     

Standardized model name.

Return type:     

str

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)