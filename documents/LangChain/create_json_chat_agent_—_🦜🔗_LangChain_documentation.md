# create_json_chat_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.json_chat.base.create_json_chat_agent.html
**Word Count:** 570
**Links Count:** 166
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# create\_json\_chat\_agent\#

langchain.agents.json\_chat.base.create\_json\_chat\_agent\(_llm: ~langchain\_core.language\_models.base.BaseLanguageModel, tools: ~collections.abc.Sequence\[~langchain\_core.tools.base.BaseTool\], prompt: ~langchain\_core.prompts.chat.ChatPromptTemplate, stop\_sequence: bool | list\[str\] = True, tools\_renderer: ~typing.Callable\[\[list\[~langchain\_core.tools.base.BaseTool\]\], str\] = <function render\_text\_description>, template\_tool\_response: str = "TOOL RESPONSE:\n---------------------\n\{observation\}\n\nUSER'S INPUT\n--------------------\n\nOkay, so what is the response to my last comment? If using information obtained from the tools you must mention it explicitly without mentioning the tool names - I have forgotten all TOOL RESPONSES\! Remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else - even if you just want to respond to the user. Do NOT respond with anything except a JSON snippet no matter what\!"_\) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/json_chat/base.html#create_json_chat_agent)\#     

Create an agent that uses JSON to format its logic, build for Chat Models.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM to use as the agent.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Tools this agent has access to.

  * **prompt** \([_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")\) – The prompt to use. See Prompt section below for more.

  * **stop\_sequence** \(_bool_ _|__list_ _\[__str_ _\]_\) – 

bool or list of str. If True, adds a stop token of “Observation:” to avoid hallucinates. If False, does not add a stop token. If a list of str, uses the provided list as the stop tokens.

Default is True. You may to set this to False if the LLM you are using does not support stop sequences.

  * **tools\_renderer** \(_Callable_ _\[__\[__list_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]__\]__,__str_ _\]_\) – This controls how the tools are converted into a string and then passed into the LLM. Default is render\_text\_description.

  * **template\_tool\_response** \(_str_\) – Template prompt that uses the tool response \(observation\) to make the LLM generate the next action to take. Default is TEMPLATE\_TOOL\_RESPONSE.

Returns:     

A Runnable sequence representing an agent. It takes as input all the same input variables as the prompt passed in does. It returns as output either an AgentAction or AgentFinish.

Raises:     

  * **ValueError** – If the prompt is missing required variables.

  * **ValueError** – If the template\_tool\_response is missing the required variable ‘observation’.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Example               from langchain import hub     from langchain_community.chat_models import ChatOpenAI     from langchain.agents import AgentExecutor, create_json_chat_agent          prompt = hub.pull("hwchase17/react-chat-json")     model = ChatOpenAI()     tools = ...          agent = create_json_chat_agent(model, tools, prompt)     agent_executor = AgentExecutor(agent=agent, tools=tools)          agent_executor.invoke({"input": "hi"})          # Using with chat history     from langchain_core.messages import AIMessage, HumanMessage     agent_executor.invoke(         {             "input": "what's my name?",             "chat_history": [                 HumanMessage(content="hi! my name is bob"),                 AIMessage(content="Hello Bob! How can I assist you today?"),             ],         }     )     

Prompt:

> The prompt must have input keys: >      >  >   * tools: contains descriptions and arguments for each tool. >  >   * tool\_names: contains all tool names. >  >   * agent\_scratchpad: must be a MessagesPlaceholder. Contains previous agent actions and tool outputs as messages. >  > 

>  > Here’s an example: >      >      >     from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder >      >     system = '''Assistant is a large language model trained by OpenAI. >      >     Assistant is designed to be able to assist with a wide range of tasks, from answering             simple questions to providing in-depth explanations and discussions on a wide range of             topics. As a language model, Assistant is able to generate human-like text based on             the input it receives, allowing it to engage in natural-sounding conversations and             provide responses that are coherent and relevant to the topic at hand. >      >     Assistant is constantly learning and improving, and its capabilities are constantly             evolving. It is able to process and understand large amounts of text, and can use this             knowledge to provide accurate and informative responses to a wide range of questions.             Additionally, Assistant is able to generate its own text based on the input it             receives, allowing it to engage in discussions and provide explanations and             descriptions on a wide range of topics. >      >     Overall, Assistant is a powerful system that can help with a wide range of tasks             and provide valuable insights and information on a wide range of topics. Whether             you need help with a specific question or just want to have a conversation about             a particular topic, Assistant is here to assist.''' >      >     human = '''TOOLS >     ------ >     Assistant can ask the user to use tools to look up information that may be helpful in             answering the users original question. The tools the human can use are: >      >     {tools} >      >     RESPONSE FORMAT INSTRUCTIONS >     ---------------------------- >      >     When responding to me, please output a response in one of two formats: >      >     **Option 1:** >     Use this if you want the human to use a tool. >     Markdown code snippet formatted in the following schema: >      >     ```json >     {{ >         "action": string, \ The action to take. Must be one of {tool_names} >         "action_input": string \ The input to the action >     }} >     ``` >      >     **Option #2:** >     Use this if you want to respond directly to the human. Markdown code snippet formatted             in the following schema: >      >     ```json >     {{ >         "action": "Final Answer", >         "action_input": string \ You should put what you want to return to use here >     }} >     ``` >      >     USER'S INPUT >     -------------------- >     Here is the user's input (remember to respond with a markdown code snippet of a json             blob with a single action, and NOTHING else): >      >     {input}''' >      >     prompt = ChatPromptTemplate.from_messages( >         [ >             ("system", system), >             MessagesPlaceholder("chat_history", optional=True), >             ("human", human), >             MessagesPlaceholder("agent_scratchpad"), >         ] >     ) >     

Examples using create\_json\_chat\_agent

  * [ZHIPU AI](https://python.langchain.com/docs/integrations/chat/zhipuai/)

__On this page