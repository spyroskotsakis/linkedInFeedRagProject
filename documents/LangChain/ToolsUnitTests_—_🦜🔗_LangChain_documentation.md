# ToolsUnitTests — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/unit_tests/langchain_tests.unit_tests.tools.ToolsUnitTests.html
**Word Count:** 175
**Links Count:** 100
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# ToolsUnitTests\#

_class _langchain\_tests.unit\_tests.tools.ToolsUnitTests[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/tools.html#ToolsUnitTests)\#     

Base class for tools unit tests.

Attributes

`init_from_env_params` | Return env vars, init args, and expected instance attrs for initializing from env vars.   ---|---   `tool_constructor` | Returns a class or instance of a tool to be tested.   `tool_constructor_params` | Returns a dictionary of parameters to pass to the tool constructor.   `tool_invoke_params_example` | Returns a dictionary representing the "args" of an example tool call.      Methods

`test_has_input_schema`\(tool\) | Tests that the tool has an input schema.   ---|---   `test_has_name`\(tool\) | Tests that the tool has a name attribute to pass to chat models.   `test_init`\(\) | Test that the tool can be initialized with `tool_constructor` and `tool_constructor_params`.   `test_init_from_env`\(\) |    `test_input_schema_matches_invoke_params`\(tool\) | Tests that the provided example params match the declared input schema.      test\_has\_input\_schema\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/tools.html#ToolsUnitTests.test_has_input_schema)\#     

Tests that the tool has an input schema.

If this fails, add an args\_schema to your tool.

See [this guide](https://python.langchain.com/docs/how_to/custom_tools/#subclass-basetool) and see how CalculatorInput is configured in the CustomCalculatorTool.args\_schema attribute

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

test\_has\_name\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/tools.html#ToolsUnitTests.test_has_name)\#     

Tests that the tool has a name attribute to pass to chat models.

If this fails, add a name parameter to your tool.

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

test\_init\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/tools.html#ToolsUnitTests.test_init)\#     

Test that the tool can be initialized with `tool_constructor` and `tool_constructor_params`. If this fails, check that the keyword args defined in `tool_constructor_params` are valid.

Return type:     

None

test\_init\_from\_env\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/tools.html#ToolsUnitTests.test_init_from_env)\#     

Return type:     

None

test\_input\_schema\_matches\_invoke\_params\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/unit_tests/tools.html#ToolsUnitTests.test_input_schema_matches_invoke_params)\#     

Tests that the provided example params match the declared input schema.

If this fails, update the tool\_invoke\_params\_example attribute to match the input schema \(args\_schema\) of the tool.

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

__On this page