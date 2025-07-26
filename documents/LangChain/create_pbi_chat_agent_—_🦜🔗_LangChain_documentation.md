# create_pbi_chat_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.chat_base.create_pbi_chat_agent.html
**Word Count:** 160
**Links Count:** 173
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# create\_pbi\_chat\_agent\#

langchain\_community.agent\_toolkits.powerbi.chat\_base.create\_pbi\_chat\_agent\(

    _llm : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _toolkit : [PowerBIToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit.html#langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit "langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit") | None = None_,     _powerbi : [PowerBIDataset](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.powerbi.PowerBIDataset.html#langchain_community.utilities.powerbi.PowerBIDataset "langchain_community.utilities.powerbi.PowerBIDataset") | None = None_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _output\_parser : [AgentOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser") | None = None_,     _prefix : str = 'Assistant is a large language model built to help users interact with a PowerBI Dataset.\n\nAssistant should try to create a correct and complete answer to the question from the user. If the user asks a question not related to the dataset it should return "This does not appear to be part of this dataset." as the answer. The user might make a mistake with the spelling of certain values, if you think that is the case, ask the user to confirm the spelling of the value and then run the query again. Unless the user specifies a specific number of examples they wish to obtain, and the results are too large, limit your query to at most \{top\_k\} results, but make it clear when answering which field was used for the filtering. The user has access to these tables: \{\{tables\}\}.\n\nThe answer should be a complete sentence that answers the question, if multiple rows are asked find a way to write that in a easily readable format for a human, also make sure to represent numbers in readable ways, like 1M instead of 1000000. \n'_,     _suffix : str = "TOOLS\n------\nAssistant can ask the user to use tools to look up information that may be helpful in answering the users original question. The tools the human can use are:\n\n\{\{tools\}\}\n\n\{format\_instructions\}\n\nUSER'S INPUT\n--------------------\nHere is the user's input \(remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else\):\n\n\{\{\{\{input\}\}\}\}\n"_,     _examples : str | None = None_,     _input\_variables : List\[str\] | None = None_,     _memory : [BaseChatMemory](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory") | None = None_,     _top\_k : int = 10_,     _verbose : bool = False_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/powerbi/chat_base.html#create_pbi_chat_agent)\#     

Construct a Power BI agent from a Chat LLM and tools.

If you supply only a toolkit and no Power BI dataset, the same LLM is used for both.

Parameters:     

  * **llm** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\) – The language model to use.

  * **toolkit** \(_Optional_ _\[_[_PowerBIToolkit_](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit.html#langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit "langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit") _\]_\) – Optional. The Power BI toolkit. Default is None.

  * **powerbi** \(_Optional_ _\[_[_PowerBIDataset_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.powerbi.PowerBIDataset.html#langchain_community.utilities.powerbi.PowerBIDataset "langchain_community.utilities.powerbi.PowerBIDataset") _\]_\) – Optional. The Power BI dataset. Default is None.

  * **callback\_manager** \(_Optional_ _\[_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _\]_\) – Optional. The callback manager. Default is None.

  * **output\_parser** \(_Optional_ _\[_[_AgentOutputParser_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser") _\]_\) – Optional. The output parser. Default is None.

  * **prefix** \(_str_\) – Optional. The prefix for the prompt. Default is POWERBI\_CHAT\_PREFIX.

  * **suffix** \(_str_\) – Optional. The suffix for the prompt. Default is POWERBI\_CHAT\_SUFFIX.

  * **examples** \(_Optional_ _\[__str_ _\]_\) – Optional. The examples for the prompt. Default is None.

  * **input\_variables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. The input variables for the prompt. Default is None.

  * **memory** \(_Optional_ _\[_[_BaseChatMemory_](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory") _\]_\) – Optional. The memory. Default is None.

  * **top\_k** \(_int_\) – Optional. The top k for the prompt. Default is 10.

  * **verbose** \(_bool_\) – Optional. Whether to print verbose output. Default is False.

  * **agent\_executor\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional. The agent executor kwargs. Default is None.

  * **kwargs** \(_Any_\) – Any. Additional keyword arguments.

Returns:     

The agent executor.

Return type:     

[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

__On this page