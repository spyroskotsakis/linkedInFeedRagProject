# BasePlanner — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.BasePlanner.html
**Word Count:** 56
**Links Count:** 138
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# BasePlanner\#

_class _langchain\_experimental.autonomous\_agents.hugginggpt.task\_planner.BasePlanner[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_planner.html#BasePlanner)\#     

Bases: `BaseModel`

Base class for a planner.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_abstractmethod async _aplan\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [Plan](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_planner.html#BasePlanner.aplan)\#     

Asynchronous Given input, decide what to do.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Plan_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")

_abstractmethod _plan\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [Plan](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_planner.html#BasePlanner.plan)\#     

Given input, decide what to do.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Plan_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")

__On this page