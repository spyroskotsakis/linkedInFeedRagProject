# TaskExecutor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_executor.TaskExecutor.html
**Word Count:** 18
**Links Count:** 160
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# TaskExecutor\#

_class _langchain\_experimental.autonomous\_agents.hugginggpt.task\_executor.TaskExecutor\(

    _plan : [Plan](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#TaskExecutor)\#     

Load tools and execute tasks.

Methods

`__init__`\(plan\) |    ---|---   `check_dependency`\(task\) |    `completed`\(\) |    `describe`\(\) |    `failed`\(\) |    `pending`\(\) |    `run`\(\) |    `update_args`\(task\) |       Parameters:     

**plan** \([_Plan_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")\)

\_\_init\_\_\(

    _plan : [Plan](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#TaskExecutor.__init__)\#     

Parameters:     

**plan** \([_Plan_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan.html#langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan "langchain_experimental.autonomous_agents.hugginggpt.task_planner.Plan")\)

check\_dependency\(

    _task : [Task](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task.html#langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task "langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task")_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#TaskExecutor.check_dependency)\#     

Parameters:     

**task** \([_Task_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task.html#langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task "langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task")\)

Return type:     

bool

completed\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#TaskExecutor.completed)\#     

Return type:     

bool

describe\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#TaskExecutor.describe)\#     

Return type:     

str

failed\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#TaskExecutor.failed)\#     

Return type:     

bool

pending\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#TaskExecutor.pending)\#     

Return type:     

bool

run\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#TaskExecutor.run)\#     

Return type:     

str

update\_args\(

    _task : [Task](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task.html#langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task "langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#TaskExecutor.update_args)\#     

Parameters:     

**task** \([_Task_](https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task.html#langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task "langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task")\)

Return type:     

None

__On this page