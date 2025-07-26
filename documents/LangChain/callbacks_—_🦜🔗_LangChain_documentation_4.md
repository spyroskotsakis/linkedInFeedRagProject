# callbacks — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks.html
**Word Count:** 52
**Links Count:** 76
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# `callbacks`\#

Callback Handler that prints to std out.

**Classes**

[`callbacks.UsageCallbackHandler`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler.html#langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler "langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler")\(\) | Callback Handler that tracks OpenAI info.   ---|---      **Functions**

[`callbacks.get_token_cost_for_model`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.get_token_cost_for_model.html#langchain_nvidia_ai_endpoints.callbacks.get_token_cost_for_model "langchain_nvidia_ai_endpoints.callbacks.get_token_cost_for_model")\(...\[, ...\]\) | Get the cost in USD for a given model and number of tokens.   ---|---   [`callbacks.get_usage_callback`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.get_usage_callback.html#langchain_nvidia_ai_endpoints.callbacks.get_usage_callback "langchain_nvidia_ai_endpoints.callbacks.get_usage_callback")\(\[price\_map, ...\]\) | Get the OpenAI callback handler in a context manager.   [`callbacks.standardize_model_name`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.standardize_model_name.html#langchain_nvidia_ai_endpoints.callbacks.standardize_model_name "langchain_nvidia_ai_endpoints.callbacks.standardize_model_name")\(model\_name\) | Standardize the model name to a format that can be used in the OpenAI API.