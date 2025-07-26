# get_usage_callback — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.get_usage_callback.html
**Word Count:** 31
**Links Count:** 80
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# get\_usage\_callback\#

langchain\_nvidia\_ai\_endpoints.callbacks.get\_usage\_callback\(

    _price\_map : dict = \{\}_,     _callback : [UsageCallbackHandler](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler.html#langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler "langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler") | None = None_, \) → Generator\[[UsageCallbackHandler](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler.html#langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler "langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler"), None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/callbacks.html#get_usage_callback)\#     

Get the OpenAI callback handler in a context manager. which conveniently exposes token and cost information.

Returns:     

The OpenAI callback handler.

Return type:     

[OpenAICallbackHandler](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.openai_info.OpenAICallbackHandler.html#langchain_community.callbacks.openai_info.OpenAICallbackHandler "langchain_community.callbacks.openai_info.OpenAICallbackHandler")

Parameters:     

  * **price\_map** \(_dict_\)

  * **callback** \([_UsageCallbackHandler_](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler.html#langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler "langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler") _|__None_\)

Example               >>> with get_openai_callback() as cb:     ...     # Use the OpenAI callback handler     

__On this page