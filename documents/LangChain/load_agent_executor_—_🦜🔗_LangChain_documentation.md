# load_agent_executor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.executors.agent_executor.load_agent_executor.html
**Word Count:** 25
**Links Count:** 114
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# load\_agent\_executor\#

langchain\_experimental.plan\_and\_execute.executors.agent\_executor.load\_agent\_executor\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tools : List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _verbose : bool = False_,     _include\_task\_in\_prompt : bool = False_, \) → [ChainExecutor](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.executors.base.ChainExecutor.html#langchain_experimental.plan_and_execute.executors.base.ChainExecutor "langchain_experimental.plan_and_execute.executors.base.ChainExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/executors/agent_executor.html#load_agent_executor)\#     

Load an agent executor.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – BaseLanguageModel

  * **tools** \(_List_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – List\[BaseTool\]

  * **verbose** \(_bool_\) – bool. Defaults to False.

  * **include\_task\_in\_prompt** \(_bool_\) – bool. Defaults to False.

Returns:     

ChainExecutor

Return type:     

[_ChainExecutor_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.executors.base.ChainExecutor.html#langchain_experimental.plan_and_execute.executors.base.ChainExecutor "langchain_experimental.plan_and_execute.executors.base.ChainExecutor")

__On this page