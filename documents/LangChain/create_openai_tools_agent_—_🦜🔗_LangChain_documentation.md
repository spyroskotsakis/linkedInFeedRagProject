# create_openai_tools_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.openai_tools.base.create_openai_tools_agent.html
**Word Count:** 130
**Links Count:** 170
**Scraped:** 2025-07-21 07:49:02
**Status:** completed

---

# create\_openai\_tools\_agent\#

langchain.agents.openai\_tools.base.create\_openai\_tools\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _prompt : [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")_,     _strict : bool | None = None_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_tools/base.html#create_openai_tools_agent)\#     

Create an agent that uses OpenAI tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM to use as the agent.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Tools this agent has access to.

  * **prompt** \([_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")\) – The prompt to use. See Prompt section below for more on the expected input variables.

  * **strict** \(_bool_ _|__None_\)

Returns:     

A Runnable sequence representing an agent. It takes as input all the same input variables as the prompt passed in does. It returns as output either an AgentAction or AgentFinish.

Raises:     

**ValueError** – If the prompt is missing required variables.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example               from langchain import hub     from langchain_community.chat_models import ChatOpenAI     from langchain.agents import AgentExecutor, create_openai_tools_agent          prompt = hub.pull("hwchase17/openai-tools-agent")     model = ChatOpenAI()     tools = ...          agent = create_openai_tools_agent(model, tools, prompt)     agent_executor = AgentExecutor(agent=agent, tools=tools)          agent_executor.invoke({"input": "hi"})          # Using with chat history     from langchain_core.messages import AIMessage, HumanMessage     agent_executor.invoke(         {             "input": "what's my name?",             "chat_history": [                 HumanMessage(content="hi! my name is bob"),                 AIMessage(content="Hello Bob! How can I assist you today?"),             ],         }     )     

Prompt:

> The agent prompt must have an agent\_scratchpad key that is a >      >  > `MessagesPlaceholder`. Intermediate agent actions and tool output messages will be passed in here. >  > Here’s an example: >      >      >     from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder >      >     prompt = ChatPromptTemplate.from_messages( >         [ >             ("system", "You are a helpful assistant"), >             MessagesPlaceholder("chat_history", optional=True), >             ("human", "{input}"), >             MessagesPlaceholder("agent_scratchpad"), >         ] >     ) >     

Examples using create\_openai\_tools\_agent

  * [Cassandra Database Toolkit](https://python.langchain.com/docs/integrations/tools/cassandra_database/)

  * [Log, Trace, and Monitor](https://python.langchain.com/docs/integrations/providers/portkey/logging_tracing_portkey/)

  * [Portkey](https://python.langchain.com/docs/integrations/providers/portkey/index/)

__On this page