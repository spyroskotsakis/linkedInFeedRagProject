# PlanningOutputParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.PlanningOutputParser.html
**Word Count:** 64
**Links Count:** 127
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# PlanningOutputParser\#

_class _langchain\_experimental.autonomous\_agents.hugginggpt.task\_planner.PlanningOutputParser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_planner.html#PlanningOutputParser)\#     

Bases: `BaseModel`

Parses the output of the planning stage.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

parse\(

    _text : str_,     _hf\_tools : List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_, \) → [Plan](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_planner.html#PlanningOutputParser.parse)\#     

Parse the output of the planning stage.

Parameters:     

  * **text** \(_str_\) – The output of the planning stage.

  * **hf\_tools** \(_List_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – The tools available.

Returns:     

The plan.

Return type:     

[_Plan_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")

__On this page