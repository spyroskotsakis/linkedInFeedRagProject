# ToolManagerMixin — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.ToolManagerMixin.html
**Word Count:** 103
**Links Count:** 144
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# ToolManagerMixin\#

_class _langchain\_core.callbacks.base.ToolManagerMixin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#ToolManagerMixin)\#     

Mixin for tool callbacks.

Methods

`on_tool_end`\(output, \*, run\_id\[, parent\_run\_id\]\) | Run when the tool ends running.   ---|---   `on_tool_error`\(error, \*, run\_id\[, parent\_run\_id\]\) | Run when tool errors.      on\_tool\_end\(

    _output : Any_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#ToolManagerMixin.on_tool_end)\#     

Run when the tool ends running.

Parameters:     

  * **output** \(_Any_\) – The output of the tool.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_tool\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#ToolManagerMixin.on_tool_error)\#     

Run when tool errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)