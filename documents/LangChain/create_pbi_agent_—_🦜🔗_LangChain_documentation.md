# create_pbi_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.base.create_pbi_agent.html
**Word Count:** 141
**Links Count:** 170
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# create\_pbi\_agent\#

langchain\_community.agent\_toolkits.powerbi.base.create\_pbi\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _toolkit : [PowerBIToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit.html#langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit "langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit") | None = None_,     _powerbi : [PowerBIDataset](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.powerbi.PowerBIDataset.html#langchain_community.utilities.powerbi.PowerBIDataset "langchain_community.utilities.powerbi.PowerBIDataset") | None = None_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _prefix : str = 'You are an agent designed to help users interact with a PowerBI Dataset.\n\nAgent has access to a tool that can write a query based on the question and then run those against PowerBI, Microsofts business intelligence tool. The questions from the users should be interpreted as related to the dataset that is available and not general questions about the world. If the question does not seem related to the dataset, return "This does not appear to be part of this dataset." as the answer.\n\nGiven an input question, ask to run the questions against the dataset, then look at the results and return the answer, the answer should be a complete sentence that answers the question, if multiple rows are asked find a way to write that in a easily readable format for a human, also make sure to represent numbers in readable ways, like 1M instead of 1000000. Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most \{top\_k\} results.\n'_,     _suffix : str = 'Begin\!\n\nQuestion: \{input\}\nThought: I can first ask which tables I have, then how each table is defined and then ask the query tool the question I need, and finally create a nice sentence that answers the question.\n\{agent\_scratchpad\}'_,     _format\_instructions : str | None = None_,     _examples : str | None = None_,     _input\_variables : List\[str\] | None = None_,     _top\_k : int = 10_,     _verbose : bool = False_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/powerbi/base.html#create_pbi_agent)\#     

Construct a Power BI agent from an LLM and tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **toolkit** \(_Optional_ _\[_[_PowerBIToolkit_](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit.html#langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit "langchain_community.agent_toolkits.powerbi.toolkit.PowerBIToolkit") _\]_\) – Optional. The Power BI toolkit. Default is None.

  * **powerbi** \(_Optional_ _\[_[_PowerBIDataset_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.powerbi.PowerBIDataset.html#langchain_community.utilities.powerbi.PowerBIDataset "langchain_community.utilities.powerbi.PowerBIDataset") _\]_\) – Optional. The Power BI dataset. Default is None.

  * **callback\_manager** \(_Optional_ _\[_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _\]_\) – Optional. The callback manager. Default is None.

  * **prefix** \(_str_\) – Optional. The prefix for the prompt. Default is POWERBI\_PREFIX.

  * **suffix** \(_str_\) – Optional. The suffix for the prompt. Default is POWERBI\_SUFFIX.

  * **format\_instructions** \(_Optional_ _\[__str_ _\]_\) – Optional. The format instructions for the prompt. Default is None.

  * **examples** \(_Optional_ _\[__str_ _\]_\) – Optional. The examples for the prompt. Default is None.

  * **input\_variables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. The input variables for the prompt. Default is None.

  * **top\_k** \(_int_\) – Optional. The top k for the prompt. Default is 10.

  * **verbose** \(_bool_\) – Optional. Whether to print verbose output. Default is False.

  * **agent\_executor\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional. The agent executor kwargs. Default is None.

  * **kwargs** \(_Any_\) – Any. Additional keyword arguments.

Returns:     

The agent executor.

Return type:     

[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

Examples using create\_pbi\_agent

  * [PowerBI Toolkit](https://python.langchain.com/docs/integrations/tools/powerbi/)

__On this page