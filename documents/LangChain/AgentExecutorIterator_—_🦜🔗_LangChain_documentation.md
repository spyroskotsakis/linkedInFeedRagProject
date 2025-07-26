# AgentExecutorIterator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_iterator.AgentExecutorIterator.html
**Word Count:** 277
**Links Count:** 185
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# AgentExecutorIterator\#

_class _langchain.agents.agent\_iterator.AgentExecutorIterator\(

    _agent\_executor : [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")_,     _inputs : Any_,     _callbacks : Callbacks = None_,     _\*_ ,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _run\_name : str | None = None_,     _run\_id : UUID | None = None_,     _include\_run\_info : bool = False_,     _yield\_actions : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_iterator.html#AgentExecutorIterator)\#     

Iterator for AgentExecutor.

Initialize the AgentExecutorIterator with the given AgentExecutor, inputs, and optional callbacks.

Parameters:     

  * **agent\_executor** \([_AgentExecutor_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")\) – The AgentExecutor to iterate over.

  * **inputs** \(_Any_\) – The inputs to the AgentExecutor.

  * **callbacks** \(_Callbacks_ _,__optional_\) – The callbacks to use during iteration. Defaults to None.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – The tags to use during iteration. Defaults to None.

  * **metadata** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – The metadata to use during iteration. Defaults to None.

  * **run\_name** \(_Optional_ _\[__str_ _\]__,__optional_\) – The name of the run. Defaults to None.

  * **run\_id** \(_Optional_ _\[__UUID_ _\]__,__optional_\) – The ID of the run. Defaults to None.

  * **include\_run\_info** \(_bool_ _,__optional_\) – Whether to include run info in the output. Defaults to False.

  * **yield\_actions** \(_bool_ _,__optional_\) – Whether to yield actions as they are generated. Defaults to False.

Attributes

`agent_executor` | The AgentExecutor to iterate over.   ---|---   `color_mapping` | A mapping of tool names to colors.   `inputs` | The inputs to the AgentExecutor.   `name_to_tool_map` | A mapping of tool names to tools.      Methods

`__init__`\(agent\_executor, inputs\[, ...\]\) | Initialize the AgentExecutorIterator with the given AgentExecutor, inputs, and optional callbacks.   ---|---   `make_final_outputs`\(outputs, run\_manager\) |    `reset`\(\) | Reset the iterator to its initial state, clearing intermediate steps, iterations, and time elapsed.   `update_iterations`\(\) | Increment the number of iterations and update the time elapsed.      \_\_init\_\_\(

    _agent\_executor : [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")_,     _inputs : Any_,     _callbacks : Callbacks = None_,     _\*_ ,     _tags : list\[str\] | None = None_,     _metadata : dict\[str, Any\] | None = None_,     _run\_name : str | None = None_,     _run\_id : UUID | None = None_,     _include\_run\_info : bool = False_,     _yield\_actions : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_iterator.html#AgentExecutorIterator.__init__)\#     

Initialize the AgentExecutorIterator with the given AgentExecutor, inputs, and optional callbacks.

Parameters:     

  * **agent\_executor** \([_AgentExecutor_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")\) – The AgentExecutor to iterate over.

  * **inputs** \(_Any_\) – The inputs to the AgentExecutor.

  * **callbacks** \(_Callbacks_ _,__optional_\) – The callbacks to use during iteration. Defaults to None.

  * **tags** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – The tags to use during iteration. Defaults to None.

  * **metadata** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – The metadata to use during iteration. Defaults to None.

  * **run\_name** \(_Optional_ _\[__str_ _\]__,__optional_\) – The name of the run. Defaults to None.

  * **run\_id** \(_Optional_ _\[__UUID_ _\]__,__optional_\) – The ID of the run. Defaults to None.

  * **include\_run\_info** \(_bool_ _,__optional_\) – Whether to include run info in the output. Defaults to False.

  * **yield\_actions** \(_bool_ _,__optional_\) – Whether to yield actions as they are generated. Defaults to False.

make\_final\_outputs\(

    _outputs : dict\[str, Any\]_,     _run\_manager : [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") | [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")_, \) → [AddableDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.AddableDict.html#langchain_core.runnables.utils.AddableDict "langchain_core.runnables.utils.AddableDict")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_iterator.html#AgentExecutorIterator.make_final_outputs)\#     

Parameters:     

  * **outputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **run\_manager** \([_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") _|_[_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")\)

Return type:     

[_AddableDict_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.AddableDict.html#langchain_core.runnables.utils.AddableDict "langchain_core.runnables.utils.AddableDict")

reset\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_iterator.html#AgentExecutorIterator.reset)\#     

Reset the iterator to its initial state, clearing intermediate steps, iterations, and time elapsed.

Return type:     

None

update\_iterations\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_iterator.html#AgentExecutorIterator.update_iterations)\#     

Increment the number of iterations and update the time elapsed.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)