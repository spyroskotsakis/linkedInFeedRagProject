# LLMPlanner — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.planners.base.LLMPlanner.html
**Word Count:** 65
**Links Count:** 135
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# LLMPlanner\#

_class _langchain\_experimental.plan\_and\_execute.planners.base.LLMPlanner[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/planners/base.html#LLMPlanner)\#     

Bases: [`BasePlanner`](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.planners.base.BasePlanner.html#langchain_experimental.plan_and_execute.planners.base.BasePlanner "langchain_experimental.plan_and_execute.planners.base.BasePlanner")

LLM planner.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _llm\_chain _: [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")_ _\[Required\]_\#     

The LLM chain to use.

_param _output\_parser _: [PlanOutputParser](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.PlanOutputParser.html#langchain_experimental.plan_and_execute.schema.PlanOutputParser "langchain_experimental.plan_and_execute.schema.PlanOutputParser")_ _\[Required\]_\#     

The output parser to use.

_param _stop _: List | None_ _ = None_\#     

The stop list to use.

_async _aplan\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [Plan](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Plan.html#langchain_experimental.plan_and_execute.schema.Plan "langchain_experimental.plan_and_execute.schema.Plan")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/planners/base.html#LLMPlanner.aplan)\#     

Given input, asynchronously decide what to do.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Plan_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Plan.html#langchain_experimental.plan_and_execute.schema.Plan "langchain_experimental.plan_and_execute.schema.Plan")

plan\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [Plan](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Plan.html#langchain_experimental.plan_and_execute.schema.Plan "langchain_experimental.plan_and_execute.schema.Plan")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/planners/base.html#LLMPlanner.plan)\#     

Given input, decide what to do.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Plan_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Plan.html#langchain_experimental.plan_and_execute.schema.Plan "langchain_experimental.plan_and_execute.schema.Plan")

__On this page