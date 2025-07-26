# create_vectorstore_router_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.vectorstore.base.create_vectorstore_router_agent.html
**Word Count:** 254
**Links Count:** 169
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# create\_vectorstore\_router\_agent\#

langchain.agents.agent\_toolkits.vectorstore.base.create\_vectorstore\_router\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _toolkit : [VectorStoreRouterToolkit](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit.html#langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit")_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _prefix : str = 'You are an agent designed to answer questions.\nYou have access to tools for interacting with different sources, and the inputs to the tools are questions.\nYour main task is to decide which of the tools is relevant for answering question at hand.\nFor complex questions, you can break the question down into sub questions and use tools to answers the sub questions.\n'_,     _verbose : bool = False_,     _agent\_executor\_kwargs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_toolkits/vectorstore/base.html#create_vectorstore_router_agent)\#     

Deprecated since version 0.2.13: This function will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. See API reference for this function for a replacement implementation: <https://api.python.langchain.com/en/latest/agents/langchain.agents.agent_toolkits.vectorstore.base.create_vectorstore_router_agent.html> Read more here on how to create agents that query vector stores: <https://python.langchain.com/docs/how_to/qa_chat_history_how_to/#agents> It will not be removed until langchain==1.0.

Construct a VectorStore router agent from an LLM and tools.

Note: this class is deprecated. See below for a replacement that uses tool calling methods and LangGraph. Install LangGraph with:

>  >     pip install -U langgraph >      >      >      >     from langchain_core.tools import create_retriever_tool >     from langchain_core.vectorstores import InMemoryVectorStore >     from langchain_openai import ChatOpenAI, OpenAIEmbeddings >     from langgraph.prebuilt import create_react_agent >      >     llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) >      >     pet_vector_store = InMemoryVectorStore.from_texts( >         [ >             "Dogs are great companions, known for their loyalty and friendliness.", >             "Cats are independent pets that often enjoy their own space.", >         ], >         OpenAIEmbeddings(), >     ) >      >     food_vector_store = InMemoryVectorStore.from_texts( >         [ >             "Carrots are orange and delicious.", >             "Apples are red and delicious.", >         ], >         OpenAIEmbeddings(), >     ) >      >     tools = [ >         create_retriever_tool( >             pet_vector_store.as_retriever(), >             "pet_information_retriever", >             "Fetches information about pets.", >         ), >         create_retriever_tool( >             food_vector_store.as_retriever(), >             "food_information_retriever", >             "Fetches information about food.", >         ) >     ] >      >     agent = create_react_agent(llm, tools) >      >     for step in agent.stream( >         {"messages": [("human", "Tell me about carrots.")]}, >         stream_mode="values", >     ): >         step["messages"][-1].pretty_print() >     

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM that will be used by the agent

  * **toolkit** \([_VectorStoreRouterToolkit_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit.html#langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit "langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreRouterToolkit")\) – Set of tools for the agent which have routing capability with multiple vector stores

  * **callback\_manager** \(_Optional_ _\[_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _\]__,__optional_\) – Object to handle the callback \[ Defaults to None. \]

  * **prefix** \(_str_ _,__optional_\) – The prefix prompt for the router agent. If not provided uses default ROUTER\_PREFIX.

  * **verbose** \(_bool_ _,__optional_\) – If you want to see the content of the scratchpad. \[ Defaults to False \]

  * **agent\_executor\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – If there is any other parameter you want to send to the agent. \[ Defaults to None \]

  * **kwargs** \(_Any_\) – Additional named parameters to pass to the ZeroShotAgent.

Returns:     

Returns a callable AgentExecutor object. Either you can call it or use run method with the query to get the response.

Return type:     

[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

__On this page