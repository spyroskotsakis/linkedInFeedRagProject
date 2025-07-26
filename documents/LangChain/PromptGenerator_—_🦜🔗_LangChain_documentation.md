# PromptGenerator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.autogpt.prompt_generator.PromptGenerator.html
**Word Count:** 123
**Links Count:** 146
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# PromptGenerator\#

_class _langchain\_experimental.autonomous\_agents.autogpt.prompt\_generator.PromptGenerator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/prompt_generator.html#PromptGenerator)\#     

Generator of custom prompt strings.

Does this based on constraints, commands, resources, and performance evaluations.

Initialize the PromptGenerator object.

Starts with empty lists of constraints, commands, resources, and performance evaluations.

Methods

`__init__`\(\) | Initialize the PromptGenerator object.   ---|---   `add_constraint`\(constraint\) | Add a constraint to the constraints list.   `add_performance_evaluation`\(evaluation\) | Add a performance evaluation item to the performance\_evaluation list.   `add_resource`\(resource\) | Add a resource to the resources list.   `add_tool`\(tool\) |    `generate_prompt_string`\(\) | Generate a prompt string.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/prompt_generator.html#PromptGenerator.__init__)\#     

Initialize the PromptGenerator object.

Starts with empty lists of constraints, commands, resources, and performance evaluations.

Return type:     

None

add\_constraint\(_constraint : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/prompt_generator.html#PromptGenerator.add_constraint)\#     

Add a constraint to the constraints list.

Parameters:     

**constraint** \(_str_\) – The constraint to be added.

Return type:     

None

add\_performance\_evaluation\(

    _evaluation : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/prompt_generator.html#PromptGenerator.add_performance_evaluation)\#     

Add a performance evaluation item to the performance\_evaluation list.

Parameters:     

**evaluation** \(_str_\) – The evaluation item to be added.

Return type:     

None

add\_resource\(_resource : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/prompt_generator.html#PromptGenerator.add_resource)\#     

Add a resource to the resources list.

Parameters:     

**resource** \(_str_\) – The resource to be added.

Return type:     

None

add\_tool\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/prompt_generator.html#PromptGenerator.add_tool)\#     

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

generate\_prompt\_string\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/prompt_generator.html#PromptGenerator.generate_prompt_string)\#     

Generate a prompt string.

Returns:     

The generated prompt string.

Return type:     

str

__On this page