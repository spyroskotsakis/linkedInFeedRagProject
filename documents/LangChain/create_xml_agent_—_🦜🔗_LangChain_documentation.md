# create_xml_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.xml.base.create_xml_agent.html
**Word Count:** 295
**Links Count:** 165
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# create\_xml\_agent\#

langchain.agents.xml.base.create\_xml\_agent\(_llm: ~langchain\_core.language\_models.base.BaseLanguageModel, tools: ~collections.abc.Sequence\[~langchain\_core.tools.base.BaseTool\], prompt: ~langchain\_core.prompts.base.BasePromptTemplate, tools\_renderer: ~typing.Callable\[\[list\[~langchain\_core.tools.base.BaseTool\]\], str\] = <function render\_text\_description>, \*, stop\_sequence: bool | list\[str\] = True_\) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/xml/base.html#create_xml_agent)\#     

Create an agent that uses XML to format its logic.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM to use as the agent.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Tools this agent has access to.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – The prompt to use, must have input keys tools: contains descriptions for each tool. agent\_scratchpad: contains previous agent actions and tool outputs.

  * **tools\_renderer** \(_Callable_ _\[__\[__list_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]__\]__,__str_ _\]_\) – This controls how the tools are converted into a string and then passed into the LLM. Default is render\_text\_description.

  * **stop\_sequence** \(_bool_ _|__list_ _\[__str_ _\]_\) – 

bool or list of str. If True, adds a stop token of “</tool\_input>” to avoid hallucinates. If False, does not add a stop token. If a list of str, uses the provided list as the stop tokens.

Default is True. You may to set this to False if the LLM you are using does not support stop sequences.

Returns:     

A Runnable sequence representing an agent. It takes as input all the same input variables as the prompt passed in does. It returns as output either an AgentAction or AgentFinish.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example               from langchain import hub     from langchain_community.chat_models import ChatAnthropic     from langchain.agents import AgentExecutor, create_xml_agent          prompt = hub.pull("hwchase17/xml-agent-convo")     model = ChatAnthropic(model="claude-3-haiku-20240307")     tools = ...          agent = create_xml_agent(model, tools, prompt)     agent_executor = AgentExecutor(agent=agent, tools=tools)          agent_executor.invoke({"input": "hi"})          # Use with chat history     from langchain_core.messages import AIMessage, HumanMessage     agent_executor.invoke(         {             "input": "what's my name?",             # Notice that chat_history is a string             # since this prompt is aimed at LLMs, not chat models             "chat_history": "Human: My name is Bob\nAI: Hello Bob!",         }     )     

Prompt:

> The prompt must have input keys: >      >  >   * tools: contains descriptions for each tool. >  >   * agent\_scratchpad: contains previous agent actions and tool outputs as an XML string. >  > 

>  > Here’s an example: >      >      >     from langchain_core.prompts import PromptTemplate >      >     template = '''You are a helpful assistant. Help the user answer any questions. >      >     You have access to the following tools: >      >     {tools} >      >     In order to use a tool, you can use <tool></tool> and <tool_input></tool_input> tags. You will then get back a response in the form <observation></observation> >     For example, if you have a tool called 'search' that could run a google search, in order to search for the weather in SF you would respond: >      >     <tool>search</tool><tool_input>weather in SF</tool_input> >     <observation>64 degrees</observation> >      >     When you are done, respond with a final answer between <final_answer></final_answer>. For example: >      >     <final_answer>The weather in SF is 64 degrees</final_answer> >      >     Begin! >      >     Previous Conversation: >     {chat_history} >      >     Question: {input} >     {agent_scratchpad}''' >     prompt = PromptTemplate.from_template(template) >     

__On this page