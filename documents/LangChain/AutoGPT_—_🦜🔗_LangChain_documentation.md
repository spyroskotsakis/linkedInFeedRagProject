# AutoGPT — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.autogpt.agent.AutoGPT.html
**Word Count:** 20
**Links Count:** 168
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# AutoGPT\#

_class _langchain\_experimental.autonomous\_agents.autogpt.agent.AutoGPT\(

    _ai\_name : str_,     _memory : [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_,     _chain : [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")_,     _output\_parser : [BaseAutoGPTOutputParser](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser.html#langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser "langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser")_,     _tools : List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _feedback\_tool : [HumanInputRun](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.human.tool.HumanInputRun.html#langchain_community.tools.human.tool.HumanInputRun "langchain_community.tools.human.tool.HumanInputRun") | None = None_,     _chat\_history\_memory : [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/agent.html#AutoGPT)\#     

Agent for interacting with AutoGPT.

Methods

`__init__`\(ai\_name, memory, chain, ...\[, ...\]\) |    ---|---   `from_llm_and_tools`\(ai\_name, ai\_role, memory, ...\) |    `run`\(goals\) |       Parameters:     

  * **ai\_name** \(_str_\)

  * **memory** \([_VectorStoreRetriever_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")\)

  * **chain** \([_LLMChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")\)

  * **output\_parser** \([_BaseAutoGPTOutputParser_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser.html#langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser "langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser")\)

  * **tools** \(_List_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\)

  * **feedback\_tool** \(_Optional_ _\[_[_HumanInputRun_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.human.tool.HumanInputRun.html#langchain_community.tools.human.tool.HumanInputRun "langchain_community.tools.human.tool.HumanInputRun") _\]_\)

  * **chat\_history\_memory** \(_Optional_ _\[_[_BaseChatMessageHistory_](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory") _\]_\)

\_\_init\_\_\(

    _ai\_name : str_,     _memory : [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_,     _chain : [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")_,     _output\_parser : [BaseAutoGPTOutputParser](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser.html#langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser "langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser")_,     _tools : List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _feedback\_tool : [HumanInputRun](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.human.tool.HumanInputRun.html#langchain_community.tools.human.tool.HumanInputRun "langchain_community.tools.human.tool.HumanInputRun") | None = None_,     _chat\_history\_memory : [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/agent.html#AutoGPT.__init__)\#     

Parameters:     

  * **ai\_name** \(_str_\)

  * **memory** \([_VectorStoreRetriever_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")\)

  * **chain** \([_LLMChain_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")\)

  * **output\_parser** \([_BaseAutoGPTOutputParser_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser.html#langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser "langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser")\)

  * **tools** \(_List_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\)

  * **feedback\_tool** \([_HumanInputRun_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.human.tool.HumanInputRun.html#langchain_community.tools.human.tool.HumanInputRun "langchain_community.tools.human.tool.HumanInputRun") _|__None_\)

  * **chat\_history\_memory** \([_BaseChatMessageHistory_](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory") _|__None_\)

_classmethod _from\_llm\_and\_tools\(

    _ai\_name : str_,     _ai\_role : str_,     _memory : [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_,     _tools : List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _llm : [BaseChatModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")_,     _human\_in\_the\_loop : bool = False_,     _output\_parser : [BaseAutoGPTOutputParser](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser.html#langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser "langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser") | None = None_,     _chat\_history\_memory : [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory") | None = None_, \) → AutoGPT[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/agent.html#AutoGPT.from_llm_and_tools)\#     

Parameters:     

  * **ai\_name** \(_str_\)

  * **ai\_role** \(_str_\)

  * **memory** \([_VectorStoreRetriever_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")\)

  * **tools** \(_List_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\)

  * **llm** \([_BaseChatModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel "langchain_core.language_models.chat_models.BaseChatModel")\)

  * **human\_in\_the\_loop** \(_bool_\)

  * **output\_parser** \([_BaseAutoGPTOutputParser_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser.html#langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser "langchain_experimental.autonomous_agents.autogpt.output_parser.BaseAutoGPTOutputParser") _|__None_\)

  * **chat\_history\_memory** \([_BaseChatMessageHistory_](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory") _|__None_\)

Return type:     

_AutoGPT_

run\(_goals : List\[str\]_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/agent.html#AutoGPT.run)\#     

Parameters:     

**goals** \(_List_ _\[__str_ _\]_\)

Return type:     

str

__On this page