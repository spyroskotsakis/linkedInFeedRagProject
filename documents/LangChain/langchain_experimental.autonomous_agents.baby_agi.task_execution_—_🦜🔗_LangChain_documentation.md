# langchain_experimental.autonomous_agents.baby_agi.task_execution — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/baby_agi/task_execution.html
**Word Count:** 33
**Links Count:** 14
**Scraped:** 2025-07-21 09:19:27
**Status:** completed

---

# Source code for langchain\_experimental.autonomous\_agents.baby\_agi.task\_execution               from langchain.chains import LLMChain     from langchain_core.language_models import BaseLanguageModel     from langchain_core.prompts import PromptTemplate                              [[docs]](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.baby_agi.task_execution.TaskExecutionChain.html#langchain_experimental.autonomous_agents.baby_agi.task_execution.TaskExecutionChain)     class TaskExecutionChain(LLMChain):         """Chain to execute tasks."""                         [[docs]](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.baby_agi.task_execution.TaskExecutionChain.html#langchain_experimental.autonomous_agents.baby_agi.task_execution.TaskExecutionChain.from_llm)         @classmethod         def from_llm(cls, llm: BaseLanguageModel, verbose: bool = True) -> LLMChain:             """Get the response parser."""             execution_template = (                 "You are an AI who performs one task based on the following objective: "                 "{objective}."                 "Take into account these previously completed tasks: {context}."                 " Your task: {task}. Response:"             )             prompt = PromptTemplate(                 template=execution_template,                 input_variables=["objective", "context", "task"],             )             return cls(prompt=prompt, llm=llm, verbose=verbose)