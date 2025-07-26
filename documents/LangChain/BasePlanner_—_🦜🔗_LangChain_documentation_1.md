# BasePlanner — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.planners.base.BasePlanner.html
**Word Count:** 53
**Links Count:** 126
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# BasePlanner\#

_class _langchain\_experimental.plan\_and\_execute.planners.base.BasePlanner[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/planners/base.html#BasePlanner)\#     

Bases: `BaseModel`

Base planner.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_abstractmethod async _aplan\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [Plan](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Plan.html#langchain_experimental.plan_and_execute.schema.Plan "langchain_experimental.plan_and_execute.schema.Plan")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/planners/base.html#BasePlanner.aplan)\#     

Given input, asynchronously decide what to do.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Plan_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Plan.html#langchain_experimental.plan_and_execute.schema.Plan "langchain_experimental.plan_and_execute.schema.Plan")

_abstractmethod _plan\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [Plan](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Plan.html#langchain_experimental.plan_and_execute.schema.Plan "langchain_experimental.plan_and_execute.schema.Plan")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/planners/base.html#BasePlanner.plan)\#     

Given input, decide what to do.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Plan_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Plan.html#langchain_experimental.plan_and_execute.schema.Plan "langchain_experimental.plan_and_execute.schema.Plan")

__On this page