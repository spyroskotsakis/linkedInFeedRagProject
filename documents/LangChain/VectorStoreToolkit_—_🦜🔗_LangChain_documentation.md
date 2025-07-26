# VectorStoreToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit.html
**Word Count:** 51
**Links Count:** 171
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# VectorStoreToolkit\#

_class _langchain.agents.agent\_toolkits.vectorstore.toolkit.VectorStoreToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_toolkits/vectorstore/toolkit.html#VectorStoreToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with a Vector Store.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

_param _vectorstore\_info _: [VectorStoreInfo](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreInfo.html#langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreInfo "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreInfo")_ _\[Required\]_\#     

get\_tools\(\) → list\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_toolkits/vectorstore/toolkit.html#VectorStoreToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

list\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

__On this page