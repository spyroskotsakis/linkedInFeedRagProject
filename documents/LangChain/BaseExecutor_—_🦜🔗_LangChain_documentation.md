# BaseExecutor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.executors.base.BaseExecutor.html
**Word Count:** 45
**Links Count:** 126
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# BaseExecutor\#

_class _langchain\_experimental.plan\_and\_execute.executors.base.BaseExecutor[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/executors/base.html#BaseExecutor)\#     

Bases: `BaseModel`

Base executor.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_abstractmethod async _astep\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [StepResponse](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/executors/base.html#BaseExecutor.astep)\#     

Take async step.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_StepResponse_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")

_abstractmethod _step\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [StepResponse](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/executors/base.html#BaseExecutor.step)\#     

Take step.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_StepResponse_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")

__On this page