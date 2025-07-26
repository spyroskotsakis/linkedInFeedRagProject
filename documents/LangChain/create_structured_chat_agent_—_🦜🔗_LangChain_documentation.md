# create_structured_chat_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.structured_chat.base.create_structured_chat_agent.html
**Word Count:** 309
**Links Count:** 166
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# create\_structured\_chat\_agent\#

langchain.agents.structured\_chat.base.create\_structured\_chat\_agent\(_llm: ~langchain\_core.language\_models.base.BaseLanguageModel, tools: ~collections.abc.Sequence\[~langchain\_core.tools.base.BaseTool\], prompt: ~langchain\_core.prompts.chat.ChatPromptTemplate, tools\_renderer: ~typing.Callable\[\[list\[~langchain\_core.tools.base.BaseTool\]\], str\] = <function render\_text\_description\_and\_args>, \*, stop\_sequence: bool | list\[str\] = True_\) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/structured_chat/base.html#create_structured_chat_agent)\#     

Create an agent aimed at supporting tools with multiple inputs.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM to use as the agent.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Tools this agent has access to.

  * **prompt** \([_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")\) – The prompt to use. See Prompt section below for more.

  * **stop\_sequence** \(_bool_ _|__list_ _\[__str_ _\]_\) – 

bool or list of str. If True, adds a stop token of “Observation:” to avoid hallucinates. If False, does not add a stop token. If a list of str, uses the provided list as the stop tokens.

Default is True. You may to set this to False if the LLM you are using does not support stop sequences.

  * **tools\_renderer** \(_Callable_ _\[__\[__list_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]__\]__,__str_ _\]_\) – This controls how the tools are converted into a string and then passed into the LLM. Default is render\_text\_description.

Returns:     

A Runnable sequence representing an agent. It takes as input all the same input variables as the prompt passed in does. It returns as output either an AgentAction or AgentFinish.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Examples               from langchain import hub     from langchain_community.chat_models import ChatOpenAI     from langchain.agents import AgentExecutor, create_structured_chat_agent          prompt = hub.pull("hwchase17/structured-chat-agent")     model = ChatOpenAI()     tools = ...          agent = create_structured_chat_agent(model, tools, prompt)     agent_executor = AgentExecutor(agent=agent, tools=tools)          agent_executor.invoke({"input": "hi"})          # Using with chat history     from langchain_core.messages import AIMessage, HumanMessage     agent_executor.invoke(         {             "input": "what's my name?",             "chat_history": [                 HumanMessage(content="hi! my name is bob"),                 AIMessage(content="Hello Bob! How can I assist you today?"),             ],         }     )     

Prompt:

> The prompt must have input keys: >      >  >   * tools: contains descriptions and arguments for each tool. >  >   * tool\_names: contains all tool names. >  >   * agent\_scratchpad: contains previous agent actions and tool outputs as a string. >  > 

>  > Here’s an example: >      >      >     from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder >      >     system = '''Respond to the human as helpfully and accurately as possible. You have access to the following tools: >      >     {tools} >      >     Use a json blob to specify a tool by providing an action key (tool name) and an action_input key (tool input). >      >     Valid "action" values: "Final Answer" or {tool_names} >      >     Provide only ONE action per $JSON_BLOB, as shown: >      >     ``` >     {{ >       "action": $TOOL_NAME, >       "action_input": $INPUT >     }} >     ``` >      >     Follow this format: >      >     Question: input question to answer >     Thought: consider previous and subsequent steps >     Action: >     ``` >     $JSON_BLOB >     ``` >     Observation: action result >     ... (repeat Thought/Action/Observation N times) >     Thought: I know what to respond >     Action: >     ``` >     {{ >       "action": "Final Answer", >       "action_input": "Final response to human" >     }} >      >     Begin! Reminder to ALWAYS respond with a valid json blob of a single action. Use tools if necessary. Respond directly if appropriate. Format is Action:```$JSON_BLOB```then Observation''' >      >     human = '''{input} >      >     {agent_scratchpad} >      >     (reminder to respond in a JSON blob no matter what)''' >      >     prompt = ChatPromptTemplate.from_messages( >         [ >             ("system", system), >             MessagesPlaceholder("chat_history", optional=True), >             ("human", human), >         ] >     ) >     

Examples using create\_structured\_chat\_agent

  * [Azure AI Services Toolkit](https://python.langchain.com/docs/integrations/tools/azure_ai_services/)

__On this page