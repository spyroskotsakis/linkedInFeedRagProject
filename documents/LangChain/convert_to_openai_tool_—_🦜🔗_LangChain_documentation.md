# convert_to_openai_tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html
**Word Count:** 195
**Links Count:** 172
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# convert\_to\_openai\_tool\#

langchain\_core.utils.function\_calling.convert\_to\_openai\_tool\(

    _tool : dict\[str, Any\] | type\[[BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\] | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_,     _\*_ ,     _strict : bool | None = None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/function_calling.html#convert_to_openai_tool)\#     

Convert a tool-like object to an OpenAI tool schema.

OpenAI tool schema reference: <https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools>

Parameters:     

  * **tool** \(_Union_ _\[__dict_ _\[__str_ _,__Any_ _\]__,__type_ _\[_[_BaseModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel") _\]__,__Callable_ _,_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Either a dictionary, a pydantic.BaseModel class, Python function, or BaseTool. If a dictionary is passed in, it is assumed to already be a valid OpenAI function, a JSON schema with top-level ‘title’ key specified, an Anthropic format tool, or an Amazon Bedrock Converse format tool.

  * **strict** \(_Optional_ _\[__bool_ _\]_\) – If True, model output is guaranteed to exactly match the JSON Schema provided in the function definition. If None, `strict` argument will not be included in tool definition.

Returns:     

A dict version of the passed in tool which is compatible with the OpenAI tool-calling API.

Return type:     

dict\[str, Any\]

Changed in version 0.2.29: `strict` arg added.

Changed in version 0.3.13: Support for Anthropic format tools added.

Changed in version 0.3.14: Support for Amazon Bedrock Converse format tools added.

Changed in version 0.3.16: ‘description’ and ‘parameters’ keys are now optional. Only ‘name’ is required and guaranteed to be part of the output.

Changed in version 0.3.44: Return OpenAI Responses API-style tools unchanged. This includes any dict with “type” in “file\_search”, “function”, “computer\_use\_preview”, “web\_search\_preview”.

Changed in version 0.3.61: Added support for OpenAI’s built-in code interpreter and remote MCP tools.

Changed in version 0.3.63: Added support for OpenAI’s image generation built-in tool.

Examples using convert\_to\_openai\_tool

  * [Llama.cpp](https://python.langchain.com/docs/integrations/chat/llamacpp/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)