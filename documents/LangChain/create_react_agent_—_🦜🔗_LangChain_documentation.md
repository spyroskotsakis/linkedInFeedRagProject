# create_react_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.react.agent.create_react_agent.html
**Word Count:** 335
**Links Count:** 174
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# create\_react\_agent\#

langchain.agents.react.agent.create\_react\_agent\(_llm: ~langchain\_core.language\_models.base.BaseLanguageModel, tools: ~collections.abc.Sequence\[~langchain\_core.tools.base.BaseTool\], prompt: ~langchain\_core.prompts.base.BasePromptTemplate, output\_parser: ~langchain.agents.agent.AgentOutputParser | None = None, tools\_renderer: ~typing.Callable\[\[list\[~langchain\_core.tools.base.BaseTool\]\], str\] = <function render\_text\_description>, \*, stop\_sequence: bool | list\[str\] = True_\) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/react/agent.html#create_react_agent)\#     

Create an agent that uses ReAct prompting.

Based on paper “ReAct: Synergizing Reasoning and Acting in Language Models” \(<https://arxiv.org/abs/2210.03629>\)

Warning

This implementation is based on the foundational ReAct paper but is older and not well-suited for production applications. For a more robust and feature-rich implementation, we recommend using the create\_react\_agent function from the LangGraph library. See the \[reference doc\]\(<https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent>\) for more information.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM to use as the agent.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Tools this agent has access to.

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – The prompt to use. See Prompt section below for more.

  * **output\_parser** \([_AgentOutputParser_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser") _|__None_\) – AgentOutputParser for parse the LLM output.

  * **tools\_renderer** \(_Callable_ _\[__\[__list_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]__\]__,__str_ _\]_\) – This controls how the tools are converted into a string and then passed into the LLM. Default is render\_text\_description.

  * **stop\_sequence** \(_bool_ _|__list_ _\[__str_ _\]_\) – 

bool or list of str. If True, adds a stop token of “Observation:” to avoid hallucinates. If False, does not add a stop token. If a list of str, uses the provided list as the stop tokens.

Default is True. You may to set this to False if the LLM you are using does not support stop sequences.

Returns:     

A Runnable sequence representing an agent. It takes as input all the same input variables as the prompt passed in does. It returns as output either an AgentAction or AgentFinish.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Examples               from langchain import hub     from langchain_community.llms import OpenAI     from langchain.agents import AgentExecutor, create_react_agent          prompt = hub.pull("hwchase17/react")     model = OpenAI()     tools = ...          agent = create_react_agent(model, tools, prompt)     agent_executor = AgentExecutor(agent=agent, tools=tools)          agent_executor.invoke({"input": "hi"})          # Use with chat history     from langchain_core.messages import AIMessage, HumanMessage     agent_executor.invoke(         {             "input": "what's my name?",             # Notice that chat_history is a string             # since this prompt is aimed at LLMs, not chat models             "chat_history": "Human: My name is Bob\nAI: Hello Bob!",         }     )     

Prompt:

> The prompt must have input keys: >      >  >   * tools: contains descriptions and arguments for each tool. >  >   * tool\_names: contains all tool names. >  >   * agent\_scratchpad: contains previous agent actions and tool outputs as a string. >  > 

>  > Here’s an example: >      >      >     from langchain_core.prompts import PromptTemplate >      >     template = '''Answer the following questions as best you can. You have access to the following tools: >      >     {tools} >      >     Use the following format: >      >     Question: the input question you must answer >     Thought: you should always think about what to do >     Action: the action to take, should be one of [{tool_names}] >     Action Input: the input to the action >     Observation: the result of the action >     ... (this Thought/Action/Action Input/Observation can repeat N times) >     Thought: I now know the final answer >     Final Answer: the final answer to the original input question >      >     Begin! >      >     Question: {input} >     Thought:{agent_scratchpad}''' >      >     prompt = PromptTemplate.from_template(template) >     

Examples using create\_react\_agent

  * [Amadeus Toolkit](https://python.langchain.com/docs/integrations/tools/amadeus/)

  * [ArXiv](https://python.langchain.com/docs/integrations/tools/arxiv/)

  * [Bittensor](https://python.langchain.com/docs/integrations/llms/bittensor/)

  * [Dataherald](https://python.langchain.com/docs/integrations/providers/dataherald/)

  * [Ionic Shopping Tool](https://python.langchain.com/docs/integrations/tools/ionic_shopping/)

  * [Streamlit](https://python.langchain.com/docs/integrations/callbacks/streamlit/)

__On this page