# ChainExecutor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.executors.base.ChainExecutor.html
**Word Count:** 47
**Links Count:** 130
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# ChainExecutor\#

_class _langchain\_experimental.plan\_and\_execute.executors.base.ChainExecutor[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/executors/base.html#ChainExecutor)\#     

Bases: [`BaseExecutor`](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.executors.base.BaseExecutor.html#langchain_experimental.plan_and_execute.executors.base.BaseExecutor "langchain_experimental.plan_and_execute.executors.base.BaseExecutor")

Chain executor.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _chain _: [Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")_ _\[Required\]_\#     

The chain to use.

_async _astep\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [StepResponse](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/executors/base.html#ChainExecutor.astep)\#     

Take step.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_StepResponse_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")

step\(

    _inputs : dict_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [StepResponse](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/executors/base.html#ChainExecutor.step)\#     

Take step.

Parameters:     

  * **inputs** \(_dict_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_StepResponse_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html#langchain_experimental.plan_and_execute.schema.StepResponse "langchain_experimental.plan_and_execute.schema.StepResponse")

__On this page