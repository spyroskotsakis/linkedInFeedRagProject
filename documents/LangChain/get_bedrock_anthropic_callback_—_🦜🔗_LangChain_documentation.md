# get_bedrock_anthropic_callback — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.manager.get_bedrock_anthropic_callback.html
**Word Count:** 42
**Links Count:** 184
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# get\_bedrock\_anthropic\_callback\#

langchain\_community.callbacks.manager.get\_bedrock\_anthropic\_callback\(\) → Generator\[[BedrockAnthropicTokenUsageCallbackHandler](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.bedrock_anthropic_callback.BedrockAnthropicTokenUsageCallbackHandler.html#langchain_community.callbacks.bedrock_anthropic_callback.BedrockAnthropicTokenUsageCallbackHandler "langchain_community.callbacks.bedrock_anthropic_callback.BedrockAnthropicTokenUsageCallbackHandler"), None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/manager.html#get_bedrock_anthropic_callback)\#     

Get the Bedrock anthropic callback handler in a context manager. which conveniently exposes token and cost information.

Returns:     

The Bedrock anthropic callback handler.

Return type:     

[BedrockAnthropicTokenUsageCallbackHandler](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.bedrock_anthropic_callback.BedrockAnthropicTokenUsageCallbackHandler.html#langchain_community.callbacks.bedrock_anthropic_callback.BedrockAnthropicTokenUsageCallbackHandler "langchain_community.callbacks.bedrock_anthropic_callback.BedrockAnthropicTokenUsageCallbackHandler")

Example               >>> with get_bedrock_anthropic_callback() as cb:     ...     # Use the Bedrock anthropic callback handler     

Examples using get\_bedrock\_anthropic\_callback

  * [How to track token usage in ChatModels](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)

__On this page