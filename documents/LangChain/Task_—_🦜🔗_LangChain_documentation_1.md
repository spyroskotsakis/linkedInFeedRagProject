# Task — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.hugginggpt.task_executor.Task.html
**Word Count:** 19
**Links Count:** 148
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# Task\#

_class _langchain\_experimental.autonomous\_agents.hugginggpt.task\_executor.Task\(

    _task : str_,     _id : int_,     _dep : List\[int\]_,     _args : Dict_,     _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#Task)\#     

Task to be executed.

Methods

`__init__`\(task, id, dep, args, tool\) |    ---|---   `completed`\(\) |    `failed`\(\) |    `pending`\(\) |    `run`\(\) |    `save_product`\(\) |       Parameters:     

  * **task** \(_str_\)

  * **id** \(_int_\)

  * **dep** \(_List_ _\[__int_ _\]_\)

  * **args** \(_Dict_\)

  * **tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

\_\_init\_\_\(

    _task : str_,     _id : int_,     _dep : List\[int\]_,     _args : Dict_,     _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#Task.__init__)\#     

Parameters:     

  * **task** \(_str_\)

  * **id** \(_int_\)

  * **dep** \(_List_ _\[__int_ _\]_\)

  * **args** \(_Dict_\)

  * **tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

completed\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#Task.completed)\#     

Return type:     

bool

failed\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#Task.failed)\#     

Return type:     

bool

pending\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#Task.pending)\#     

Return type:     

bool

run\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#Task.run)\#     

Return type:     

str

save\_product\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/hugginggpt/task_executor.html#Task.save_product)\#     

Return type:     

None

__On this page