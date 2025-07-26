# create_openai_functions_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.openai_functions_agent.base.create_openai_functions_agent.html
**Word Count:** 162
**Links Count:** 175
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# create\_openai\_functions\_agent\#

langchain.agents.openai\_functions\_agent.base.create\_openai\_functions\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _prompt : [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/base.html#create_openai_functions_agent)\#     

Create an agent that uses OpenAI function calling.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM to use as the agent. Should work with OpenAI function calling, so either be an OpenAI model that supports that or a wrapper of a different model that adds in equivalent support.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Tools this agent has access to.

  * **prompt** \([_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")\) – The prompt to use. See Prompt section below for more.

Returns:     

A Runnable sequence representing an agent. It takes as input all the same input     

variables as the prompt passed in does. It returns as output either an AgentAction or AgentFinish.

Raises:     

**ValueError** – If agent\_scratchpad is not in the prompt.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example

Creating an agent with no memory               from langchain_community.chat_models import ChatOpenAI     from langchain.agents import AgentExecutor, create_openai_functions_agent     from langchain import hub          prompt = hub.pull("hwchase17/openai-functions-agent")     model = ChatOpenAI()     tools = ...          agent = create_openai_functions_agent(model, tools, prompt)     agent_executor = AgentExecutor(agent=agent, tools=tools)          agent_executor.invoke({"input": "hi"})          # Using with chat history     from langchain_core.messages import AIMessage, HumanMessage     agent_executor.invoke(         {             "input": "what's my name?",             "chat_history": [                 HumanMessage(content="hi! my name is bob"),                 AIMessage(content="Hello Bob! How can I assist you today?"),             ],         }     )     

Prompt:

> The agent prompt must have an agent\_scratchpad key that is a >      >  > `MessagesPlaceholder`. Intermediate agent actions and tool output messages will be passed in here. >  > Here’s an example: >      >      >     from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder >      >     prompt = ChatPromptTemplate.from_messages( >         [ >             ("system", "You are a helpful assistant"), >             MessagesPlaceholder("chat_history", optional=True), >             ("human", "{input}"), >             MessagesPlaceholder("agent_scratchpad"), >         ] >     ) >     

Examples using create\_openai\_functions\_agent

  * [AskNews](https://python.langchain.com/docs/integrations/tools/asknews/)

  * [Infobip](https://python.langchain.com/docs/integrations/tools/infobip/)

  * [MultiOn Toolkit](https://python.langchain.com/docs/integrations/tools/multion/)

  * [Passio NutritionAI](https://python.langchain.com/docs/integrations/tools/passio_nutrition_ai/)

  * [Polygon IO Toolkit](https://python.langchain.com/docs/integrations/tools/polygon_toolkit/)

  * [Polygon IO Toolkit and Tools](https://python.langchain.com/docs/integrations/tools/polygon/)

  * [Semantic Scholar API Tool](https://python.langchain.com/docs/integrations/tools/semanticscholar/)

  * [You.com Search](https://python.langchain.com/docs/integrations/tools/you/)

__On this page