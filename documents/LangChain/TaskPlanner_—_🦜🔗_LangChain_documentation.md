# TaskPlanner — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.TaskPlanner.html
**Word Count:** 54
**Links Count:** 147
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# TaskPlanner\#

_class _langchain\_experimental.autonomous\_agents.hugginggpt.task\_planner.TaskPlanner[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_planner.html#TaskPlanner)\#     

Bases: [`BasePlanner`](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.BasePlanner.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.BasePlanner "langchain_experimental.autonomous_agents.hugginggpt.task_planner.BasePlanner")

Planner for tasks.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _llm\_chain _: [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")_ _\[Required\]_\#     

_param _output\_parser _: [PlanningOutputParser](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.PlanningOutputParser.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.PlanningOutputParser "langchain_experimental.autonomous_agents.hugginggpt.task_planner.PlanningOutputParser")_ _\[Required\]_\#     

_param _stop _: List | None_ _ = None_\#     

_async _aplan\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [Plan](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_planner.html#TaskPlanner.aplan)\#     

Asynchronous Given input, decided what to do.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Plan_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")

plan\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [Plan](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_planner.html#TaskPlanner.plan)\#     

Given input, decided what to do.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Plan_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")

__On this page