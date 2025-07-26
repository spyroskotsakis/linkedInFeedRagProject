# ChainManagerMixin — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.ChainManagerMixin.html
**Word Count:** 189
**Links Count:** 156
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# ChainManagerMixin\#

_class _langchain\_core.callbacks.base.ChainManagerMixin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#ChainManagerMixin)\#     

Mixin for chain callbacks.

Methods

`on_agent_action`\(action, \*, run\_id\[, ...\]\) | Run on agent action.   ---|---   `on_agent_finish`\(finish, \*, run\_id\[, ...\]\) | Run on the agent end.   `on_chain_end`\(outputs, \*, run\_id\[, parent\_run\_id\]\) | Run when chain ends running.   `on_chain_error`\(error, \*, run\_id\[, parent\_run\_id\]\) | Run when chain errors.      on\_agent\_action\(

    _action : [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#ChainManagerMixin.on_agent_action)\#     

Run on agent action.

Parameters:     

  * **action** \([_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\) – The agent action.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_agent\_finish\(

    _finish : [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#ChainManagerMixin.on_agent_finish)\#     

Run on the agent end.

Parameters:     

  * **finish** \([_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")\) – The agent finish.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_chain\_end\(

    _outputs : dict\[str, Any\]_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#ChainManagerMixin.on_chain_end)\#     

Run when chain ends running.

Parameters:     

  * **outputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The outputs of the chain.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_chain\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#ChainManagerMixin.on_chain_error)\#     

Run when chain errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)