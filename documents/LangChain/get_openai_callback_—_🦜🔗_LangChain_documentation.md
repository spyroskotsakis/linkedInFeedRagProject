# get_openai_callback — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.manager.get_openai_callback.html
**Word Count:** 49
**Links Count:** 187
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# get\_openai\_callback\#

langchain\_community.callbacks.manager.get\_openai\_callback\(\) → Generator\[[OpenAICallbackHandler](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.openai_info.OpenAICallbackHandler.html#langchain_community.callbacks.openai_info.OpenAICallbackHandler "langchain_community.callbacks.openai_info.OpenAICallbackHandler"), None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/manager.html#get_openai_callback)\#     

Get the OpenAI callback handler in a context manager. which conveniently exposes token and cost information.

Returns:     

The OpenAI callback handler.

Return type:     

[OpenAICallbackHandler](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.openai_info.OpenAICallbackHandler.html#langchain_community.callbacks.openai_info.OpenAICallbackHandler "langchain_community.callbacks.openai_info.OpenAICallbackHandler")

Example               >>> with get_openai_callback() as cb:     ...     # Use the OpenAI callback handler     

Examples using get\_openai\_callback

  * [AzureChatOpenAI](https://python.langchain.com/docs/integrations/chat/azure_chat_openai/)

  * [How to run custom functions](https://python.langchain.com/docs/how_to/functions/)

  * [How to track token usage for LLMs](https://python.langchain.com/docs/how_to/llm_token_usage_tracking/)

  * [How to track token usage in ChatModels](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)

__On this page