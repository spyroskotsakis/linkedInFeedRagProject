# create_conversational_retrieval_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.conversational_retrieval.openai_functions.create_conversational_retrieval_agent.html
**Word Count:** 147
**Links Count:** 168
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# create\_conversational\_retrieval\_agent\#

langchain.agents.agent\_toolkits.conversational\_retrieval.openai\_functions.create\_conversational\_retrieval\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tools : list\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _remember\_intermediate\_steps : bool = True_,     _memory\_key : str = 'chat\_history'_,     _system\_message : [SystemMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html#langchain_core.messages.system.SystemMessage "langchain_core.messages.system.SystemMessage") | None = None_,     _verbose : bool = False_,     _max\_token\_limit : int = 2000_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_toolkits/conversational_retrieval/openai_functions.html#create_conversational_retrieval_agent)\#     

A convenience method for creating a conversational retrieval agent.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use, should be ChatOpenAI

  * **tools** \(_list_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – A list of tools the agent has access to

  * **remember\_intermediate\_steps** \(_bool_\) – Whether the agent should remember intermediate steps or not. Intermediate steps refer to prior action/observation pairs from previous questions. The benefit of remembering these is if there is relevant information in there, the agent can use it to answer follow up questions. The downside is it will take up more tokens.

  * **memory\_key** \(_str_\) – The name of the memory key in the prompt.

  * **system\_message** \([_SystemMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html#langchain_core.messages.system.SystemMessage "langchain_core.messages.system.SystemMessage") _|__None_\) – The system message to use. By default, a basic one will be used.

  * **verbose** \(_bool_\) – Whether or not the final AgentExecutor should be verbose or not, defaults to False.

  * **max\_token\_limit** \(_int_\) – The max number of tokens to keep around in memory. Defaults to 2000.

  * **kwargs** \(_Any_\)

Returns:     

An agent executor initialized appropriately

Return type:     

[_AgentExecutor_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

Examples using create\_conversational\_retrieval\_agent

  * [Cogniswitch Toolkit](https://python.langchain.com/docs/integrations/tools/cogniswitch/)

__On this page