# create_vectorstore_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.vectorstore.base.create_vectorstore_agent.html
**Word Count:** 234
**Links Count:** 169
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# create\_vectorstore\_agent\#

langchain.agents.agent\_toolkits.vectorstore.base.create\_vectorstore\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _toolkit : [VectorStoreToolkit](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit.html#langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit")_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _prefix : str = 'You are an agent designed to answer questions about sets of documents.\nYou have access to tools for interacting with the documents, and the inputs to the tools are questions.\nSometimes, you will be asked to provide sources for your questions, in which case you should use the appropriate tool to do so.\nIf the question does not seem relevant to any of the tools provided, just return "I don\'t know" as the answer.\n'_,     _verbose : bool = False_,     _agent\_executor\_kwargs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_toolkits/vectorstore/base.html#create_vectorstore_agent)\#     

Deprecated since version 0.2.13: This function will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. See API reference for this function for a replacement implementation: <https://api.python.langchain.com/en/latest/agents/langchain.agents.agent_toolkits.vectorstore.base.create_vectorstore_agent.html> Read more here on how to create agents that query vector stores: <https://python.langchain.com/docs/how_to/qa_chat_history_how_to/#agents> It will not be removed until langchain==1.0.

Construct a VectorStore agent from an LLM and tools.

Note: this class is deprecated. See below for a replacement that uses tool calling methods and LangGraph. Install LangGraph with:

>  >     pip install -U langgraph >      >      >      >     from langchain_core.tools import create_retriever_tool >     from langchain_core.vectorstores import InMemoryVectorStore >     from langchain_openai import ChatOpenAI, OpenAIEmbeddings >     from langgraph.prebuilt import create_react_agent >      >     llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) >      >     vector_store = InMemoryVectorStore.from_texts( >         [ >             "Dogs are great companions, known for their loyalty and friendliness.", >             "Cats are independent pets that often enjoy their own space.", >         ], >         OpenAIEmbeddings(), >     ) >      >     tool = create_retriever_tool( >         vector_store.as_retriever(), >         "pet_information_retriever", >         "Fetches information about pets.", >     ) >      >     agent = create_react_agent(llm, [tool]) >      >     for step in agent.stream( >         {"messages": [("human", "What are dogs known for?")]}, >         stream_mode="values", >     ): >         step["messages"][-1].pretty_print() >     

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM that will be used by the agent

  * **toolkit** \([_VectorStoreToolkit_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit.html#langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreToolkit")\) – Set of tools for the agent

  * **callback\_manager** \(_Optional_ _\[_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _\]__,__optional_\) – Object to handle the callback \[ Defaults to None. \]

  * **prefix** \(_str_ _,__optional_\) – The prefix prompt for the agent. If not provided uses default PREFIX.

  * **verbose** \(_bool_ _,__optional_\) – If you want to see the content of the scratchpad. \[ Defaults to False \]

  * **agent\_executor\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – If there is any other parameter you want to send to the agent. \[ Defaults to None \]

  * **kwargs** \(_Any_\) – Additional named parameters to pass to the ZeroShotAgent.

Returns:     

Returns a callable AgentExecutor object. Either you can call it or use run method with the query to get the response

Return type:     

[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

__On this page