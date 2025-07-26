# RunLog — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.RunLog.html
**Word Count:** 48
**Links Count:** 143
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# RunLog\#

_class _langchain\_core.tracers.log\_stream.RunLog\(

    _\* ops: dict\[str, Any\]_,     _state : [RunState](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.RunState.html#langchain_core.tracers.log_stream.RunState "langchain_core.tracers.log_stream.RunState")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#RunLog)\#     

Run log.

Create a RunLog.

Parameters:     

  * **\*ops** \(_list_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – The operations to apply to the state.

  * **state** \([_RunState_](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.RunState.html#langchain_core.tracers.log_stream.RunState "langchain_core.tracers.log_stream.RunState")\) – The initial state of the run log.

Attributes

Methods

`__init__`\(\*ops, state\) | Create a RunLog.   ---|---      \_\_init\_\_\(

    _\* ops: dict\[str, Any\]_,     _state : [RunState](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.RunState.html#langchain_core.tracers.log_stream.RunState "langchain_core.tracers.log_stream.RunState")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tracers/log_stream.html#RunLog.__init__)\#     

Create a RunLog.

Parameters:     

  * **\*ops** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The operations to apply to the state.

  * **state** \([_RunState_](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.log_stream.RunState.html#langchain_core.tracers.log_stream.RunState "langchain_core.tracers.log_stream.RunState")\) – The initial state of the run log.

Return type:     

None

__On this page