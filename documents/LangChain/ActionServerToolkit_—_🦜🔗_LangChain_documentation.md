# ActionServerToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/sema4/toolkits/langchain_sema4.toolkits.ActionServerToolkit.html
**Word Count:** 94
**Links Count:** 90
**Scraped:** 2025-07-21 07:58:35
**Status:** completed

---

# ActionServerToolkit\#

_class _langchain\_sema4.toolkits.ActionServerToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sema4/toolkits.html#ActionServerToolkit)\#     

Bases: `BaseModel`

Toolkit exposing Robocorp Action Server provided actions as individual tools.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _additional\_headers _: dict_ _\[Optional\]_\#     

Additional headers to be passed to the Action Server

_param _api\_key _: str_ _ = ''_\#     

Action Server request API key

_param _report\_trace _: bool_ _ = False_\#     

Enable reporting Langsmith trace to Action Server runs

_param _url _: str_ _\[Required\]_\#     

Action Server URL

get\_tools\(

    _llm : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel") | None = None_,     _callback\_manager : [CallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager") | None = None_, \) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sema4/toolkits.html#ActionServerToolkit.get_tools)\#     

Get Action Server actions as a toolkit

Parameters:     

  * **llm** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel") _|__None_\) – Optionally pass a model to return single input tools

  * **callback\_manager** \([_CallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManager.html#langchain_core.callbacks.manager.CallbackManager "langchain_core.callbacks.manager.CallbackManager") _|__None_\) – Callback manager to be passed to tools

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

__On this page