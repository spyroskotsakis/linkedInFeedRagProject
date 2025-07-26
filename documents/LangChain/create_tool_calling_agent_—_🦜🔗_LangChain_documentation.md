# create_tool_calling_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.tool_calling_agent.base.create_tool_calling_agent.html
**Word Count:** 183
**Links Count:** 177
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# create\_tool\_calling\_agent\#

langchain.agents.tool\_calling\_agent.base.create\_tool\_calling\_agent\(_llm: ~langchain\_core.language\_models.base.BaseLanguageModel, tools: ~collections.abc.Sequence\[~langchain\_core.tools.base.BaseTool\], prompt: ~langchain\_core.prompts.chat.ChatPromptTemplate, \*, message\_formatter: ~typing.Callable\[\[~collections.abc.Sequence\[tuple\[~langchain\_core.agents.AgentAction, str\]\]\], list\[~langchain\_core.messages.base.BaseMessage\]\] = <function format\_to\_tool\_messages>_\) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/tool_calling_agent/base.html#create_tool_calling_agent)\#     

Create an agent that uses tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM to use as the agent.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Tools this agent has access to.

  * **prompt** \([_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")\) – The prompt to use. See Prompt section below for more on the expected input variables.

  * **message\_formatter** \(_Callable_ _\[__\[__Sequence_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]__\]__,__list_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]__\]_\) – Formatter function to convert \(AgentAction, tool output\) tuples into FunctionMessages.

Returns:     

A Runnable sequence representing an agent. It takes as input all the same input variables as the prompt passed in does. It returns as output either an AgentAction or AgentFinish.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example               from langchain.agents import AgentExecutor, create_tool_calling_agent, tool     from langchain_anthropic import ChatAnthropic     from langchain_core.prompts import ChatPromptTemplate          prompt = ChatPromptTemplate.from_messages(         [             ("system", "You are a helpful assistant"),             ("placeholder", "{chat_history}"),             ("human", "{input}"),             ("placeholder", "{agent_scratchpad}"),         ]     )     model = ChatAnthropic(model="claude-3-opus-20240229")          @tool     def magic_function(input: int) -> int:         """Applies a magic function to an input."""         return input + 2          tools = [magic_function]          agent = create_tool_calling_agent(model, tools, prompt)     agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)          agent_executor.invoke({"input": "what is the value of magic_function(3)?"})          # Using with chat history     from langchain_core.messages import AIMessage, HumanMessage     agent_executor.invoke(         {             "input": "what's my name?",             "chat_history": [                 HumanMessage(content="hi! my name is bob"),                 AIMessage(content="Hello Bob! How can I assist you today?"),             ],         }     )     

Prompt:

> The agent prompt must have an agent\_scratchpad key that is a >      >  > `MessagesPlaceholder`. Intermediate agent actions and tool output messages will be passed in here.

Examples using create\_tool\_calling\_agent

  * [Azure Container Apps dynamic sessions](https://python.langchain.com/docs/integrations/tools/azure_dynamic_sessions/)

  * [Bing Search](https://python.langchain.com/docs/integrations/tools/bing_search/)

  * [Build an Agent with AgentExecutor \(Legacy\)](https://python.langchain.com/docs/how_to/agent_executor/)

  * [Databricks Unity Catalog \(UC\)](https://python.langchain.com/docs/integrations/tools/databricks/)

  * [FinancialDatasets Toolkit](https://python.langchain.com/docs/integrations/tools/financial_datasets/)

  * [How to add tools to chatbots](https://python.langchain.com/docs/how_to/chatbots_tools/)

  * [How to debug your LLM apps](https://python.langchain.com/docs/how_to/debugging/)

  * [How to migrate from legacy LangChain agents to LangGraph](https://python.langchain.com/docs/how_to/migrate_agent/)

  * [How to track token usage in ChatModels](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)

  * [How to use tools in a chain](https://python.langchain.com/docs/how_to/tools_chain/)

  * [Riza Code Interpreter](https://python.langchain.com/docs/integrations/tools/riza/)

__On this page