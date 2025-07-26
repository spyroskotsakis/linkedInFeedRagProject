# create_retriever_tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.retriever.create_retriever_tool.html
**Word Count:** 159
**Links Count:** 125
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# create\_retriever\_tool\#

langchain\_core.tools.retriever.create\_retriever\_tool\(

    _retriever : [BaseRetriever](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever")_,     _name : str_,     _description : str_,     _\*_ ,     _document\_prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _document\_separator : str = '\n\n'_,     _response\_format : Literal\['content', 'content\_and\_artifact'\] = 'content'_, \) → [Tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.simple.Tool.html#langchain_core.tools.simple.Tool "langchain_core.tools.simple.Tool")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/retriever.html#create_retriever_tool)\#     

Create a tool to do retrieval of documents.

Parameters:     

  * **retriever** \([_BaseRetriever_](https://python.langchain.com/api_reference/core/retrievers/langchain_core.retrievers.BaseRetriever.html#langchain_core.retrievers.BaseRetriever "langchain_core.retrievers.BaseRetriever")\) – The retriever to use for the retrieval

  * **name** \(_str_\) – The name for the tool. This will be passed to the language model, so should be unique and somewhat descriptive.

  * **description** \(_str_\) – The description for the tool. This will be passed to the language model, so should be descriptive.

  * **document\_prompt** \(_Optional_ _\[_[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _\]_\) – The prompt to use for the document. Defaults to None.

  * **document\_separator** \(_str_\) – The separator to use between documents. Defaults to “nn”.

  * **response\_format** \(_Literal_ _\[__'content'__,__'content\_and\_artifact'__\]_\) – The tool response format. If “content” then the output of the tool is interpreted as the contents of a ToolMessage. If “content\_and\_artifact” then the output is expected to be a two-tuple corresponding to the \(content, artifact\) of a ToolMessage \(artifact being a list of documents in this case\). Defaults to “content”.

Returns:     

Tool class to pass to an agent.

Return type:     

[Tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.simple.Tool.html#langchain_core.tools.simple.Tool "langchain_core.tools.simple.Tool")

Examples using create\_retriever\_tool

  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)

  * [Build an Agent with AgentExecutor \(Legacy\)](https://python.langchain.com/docs/how_to/agent_executor/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [Xata](https://python.langchain.com/docs/integrations/memory/xata_chat_message_history/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)