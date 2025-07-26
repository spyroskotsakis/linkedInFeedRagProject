# load_chat_planner — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.planners.chat_planner.load_chat_planner.html
**Word Count:** 17
**Links Count:** 112
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# load\_chat\_planner\#

langchain\_experimental.plan\_and\_execute.planners.chat\_planner.load\_chat\_planner\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _system\_prompt : str = "Let's first understand the problem and devise a plan to solve the problem. Please output the plan starting with the header 'Plan:' and then followed by a numbered list of steps. Please make the plan the minimum number of steps required to accurately complete the task. If the task is a question, the final step should almost always be 'Given the above steps taken, please respond to the users original question'. At the end of your plan, say '<END\_OF\_PLAN>'"_, \) → [LLMPlanner](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.planners.base.LLMPlanner.html#langchain_experimental.plan_and_execute.planners.base.LLMPlanner "langchain_experimental.plan_and_execute.planners.base.LLMPlanner")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/planners/chat_planner.html#load_chat_planner)\#     

Load a chat planner.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model.

  * **system\_prompt** \(_str_\) – System prompt.

Returns:     

LLMPlanner

Return type:     

[_LLMPlanner_](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.planners.base.LLMPlanner.html#langchain_experimental.plan_and_execute.planners.base.LLMPlanner "langchain_experimental.plan_and_execute.planners.base.LLMPlanner")

__On this page