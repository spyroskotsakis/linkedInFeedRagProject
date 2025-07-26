# create_self_ask_with_search_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.self_ask_with_search.base.create_self_ask_with_search_agent.html
**Word Count:** 352
**Links Count:** 167
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# create\_self\_ask\_with\_search\_agent\#

langchain.agents.self\_ask\_with\_search.base.create\_self\_ask\_with\_search\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/self_ask_with_search/base.html#create_self_ask_with_search_agent)\#     

Create an agent that uses self-ask with search prompting.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – LLM to use as the agent.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – List of tools. Should just be of length 1, with that tool having name Intermediate Answer

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")\) – The prompt to use, must have input key agent\_scratchpad which will contain agent actions and tool outputs.

Returns:     

A Runnable sequence representing an agent. It takes as input all the same input variables as the prompt passed in does. It returns as output either an AgentAction or AgentFinish.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

Examples               from langchain import hub     from langchain_community.chat_models import ChatAnthropic     from langchain.agents import (         AgentExecutor, create_self_ask_with_search_agent     )          prompt = hub.pull("hwchase17/self-ask-with-search")     model = ChatAnthropic(model="claude-3-haiku-20240307")     tools = [...]  # Should just be one tool with name `Intermediate Answer`          agent = create_self_ask_with_search_agent(model, tools, prompt)     agent_executor = AgentExecutor(agent=agent, tools=tools)          agent_executor.invoke({"input": "hi"})     

Prompt:

> The prompt must have input key agent\_scratchpad which will >      >  > contain agent actions and tool outputs as a string. >  > Here’s an example: >      >      >     from langchain_core.prompts import PromptTemplate >      >     template = '''Question: Who lived longer, Muhammad Ali or Alan Turing? >     Are follow up questions needed here: Yes. >     Follow up: How old was Muhammad Ali when he died? >     Intermediate answer: Muhammad Ali was 74 years old when he died. >     Follow up: How old was Alan Turing when he died? >     Intermediate answer: Alan Turing was 41 years old when he died. >     So the final answer is: Muhammad Ali >      >     Question: When was the founder of craigslist born? >     Are follow up questions needed here: Yes. >     Follow up: Who was the founder of craigslist? >     Intermediate answer: Craigslist was founded by Craig Newmark. >     Follow up: When was Craig Newmark born? >     Intermediate answer: Craig Newmark was born on December 6, 1952. >     So the final answer is: December 6, 1952 >      >     Question: Who was the maternal grandfather of George Washington? >     Are follow up questions needed here: Yes. >     Follow up: Who was the mother of George Washington? >     Intermediate answer: The mother of George Washington was Mary Ball Washington. >     Follow up: Who was the father of Mary Ball Washington? >     Intermediate answer: The father of Mary Ball Washington was Joseph Ball. >     So the final answer is: Joseph Ball >      >     Question: Are both the directors of Jaws and Casino Royale from the same country? >     Are follow up questions needed here: Yes. >     Follow up: Who is the director of Jaws? >     Intermediate answer: The director of Jaws is Steven Spielberg. >     Follow up: Where is Steven Spielberg from? >     Intermediate answer: The United States. >     Follow up: Who is the director of Casino Royale? >     Intermediate answer: The director of Casino Royale is Martin Campbell. >     Follow up: Where is Martin Campbell from? >     Intermediate answer: New Zealand. >     So the final answer is: No >      >     Question: {input} >     Are followup questions needed here:{agent_scratchpad}''' >      >     prompt = PromptTemplate.from_template(template) >     

__On this page