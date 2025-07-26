# get_usage_metadata_callback — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.usage.get_usage_metadata_callback.html
**Word Count:** 64
**Links Count:** 138
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# get\_usage\_metadata\_callback\#

langchain\_core.callbacks.usage.get\_usage\_metadata\_callback\(

    _name : str = 'usage\_metadata\_callback'_, \) → Generator\[[UsageMetadataCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.usage.UsageMetadataCallbackHandler.html#langchain_core.callbacks.usage.UsageMetadataCallbackHandler "langchain_core.callbacks.usage.UsageMetadataCallbackHandler"), None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/usage.html#get_usage_metadata_callback)\#     

Get usage metadata callback.

Get context manager for tracking usage metadata across chat model calls using `AIMessage.usage_metadata`.

Parameters:     

**name** \(_str_\) – The name of the context variable. Defaults to `"usage_metadata_callback"`.

Return type:     

_Generator_\[[_UsageMetadataCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.usage.UsageMetadataCallbackHandler.html#langchain_core.callbacks.usage.UsageMetadataCallbackHandler "langchain_core.callbacks.usage.UsageMetadataCallbackHandler"), None, None\]

Example               from langchain.chat_models import init_chat_model     from langchain_core.callbacks import get_usage_metadata_callback          llm_1 = init_chat_model(model="openai:gpt-4o-mini")     llm_2 = init_chat_model(model="anthropic:claude-3-5-haiku-latest")          with get_usage_metadata_callback() as cb:         llm_1.invoke("Hello")         llm_2.invoke("Hello")         print(cb.usage_metadata)                    {'gpt-4o-mini-2024-07-18': {'input_tokens': 8,       'output_tokens': 10,       'total_tokens': 18,       'input_token_details': {'audio': 0, 'cache_read': 0},       'output_token_details': {'audio': 0, 'reasoning': 0}},      'claude-3-5-haiku-20241022': {'input_tokens': 8,       'output_tokens': 21,       'total_tokens': 29,       'input_token_details': {'cache_read': 0, 'cache_creation': 0}}}     

Added in version 0.3.49.

__On this page