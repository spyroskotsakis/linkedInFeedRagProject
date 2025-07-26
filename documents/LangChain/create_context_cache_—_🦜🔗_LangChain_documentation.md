# create_context_cache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/utils/langchain_google_vertexai.utils.create_context_cache.html
**Word Count:** 166
**Links Count:** 89
**Scraped:** 2025-07-21 08:27:18
**Status:** completed

---

# create\_context\_cache\#

langchain\_google\_vertexai.utils.create\_context\_cache\(

    _model : [ChatVertexAI](https://python.langchain.com/api_reference/google_vertexai/chat_models/langchain_google_vertexai.chat_models.ChatVertexAI.html#langchain_google_vertexai.chat_models.ChatVertexAI "langchain_google_vertexai.chat_models.ChatVertexAI")_,     _messages : List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _expire\_time : datetime | None = None_,     _time\_to\_live : timedelta | None = None_,     _tools : Sequence\[Tool | Tool | \_ToolDictLike | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") | Type\[BaseModel\] | [FunctionDescription](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription") | Callable | FunctionDeclaration | Dict\[str, Any\]\] | None = None_,     _tool\_config : \_ToolConfigDict | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/utils.html#create_context_cache)\#     

Creates a cache for content in some model.

Parameters:     

  * **model** \([_ChatVertexAI_](https://python.langchain.com/api_reference/google_vertexai/chat_models/langchain_google_vertexai.chat_models.ChatVertexAI.html#langchain_google_vertexai.chat_models.ChatVertexAI "langchain_google_vertexai.chat_models.ChatVertexAI")\) – ChatVertexAI model. Must be at least gemini-2.5-pro or gemini-2.0-flash.

  * **messages** \(_List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – List of messages to cache.

  * **expire\_time** \(_datetime_ _|__None_\) – Timestamp of when this resource is considered expired.

  * **set** \(_At most one_ _of_ _expire\_time and ttl can be set. If neither is_\) – on the API side will be used \(currently 1 hour\).

  * **TTL** \(_default_\) – on the API side will be used \(currently 1 hour\).

  * **time\_to\_live** \(_timedelta_ _|__None_\) – The TTL for this resource. If provided, the expiration time is

  * **computed** – created\_time + TTL.

  * **set** – on the API side will be used \(currently 1 hour\).

  * **TTL** – on the API side will be used \(currently 1 hour\).

  * **tools** \(_Sequence_ _\[__Tool_ _|__Tool_ _|__\_ToolDictLike_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _|__Type_ _\[__BaseModel_ _\]__|_[_FunctionDescription_](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription") _|__Callable_ _|__FunctionDeclaration_ _|__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – A list of tool definitions to bind to this chat model. Can be a pydantic model, callable, or BaseTool. Pydantic models, callables, and BaseTools will be automatically converted to their schema dictionary representation.

  * **tool\_config** \(_\_ToolConfigDict_ _|__None_\) – Optional. Immutable. Tool config. This config is shared for all tools.

Raises:     

**ValueError** – If model doesn’t support context catching.

Returns:     

String with the identificator of the created cache.

Return type:     

str

__On this page