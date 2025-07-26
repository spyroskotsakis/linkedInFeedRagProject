# ToolsIntegrationTests — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/standard_tests/integration_tests/langchain_tests.integration_tests.tools.ToolsIntegrationTests.html
**Word Count:** 246
**Links Count:** 102
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# ToolsIntegrationTests\#

_class _langchain\_tests.integration\_tests.tools.ToolsIntegrationTests[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/tools.html#ToolsIntegrationTests)\#     

Base class for tools integration tests.

Attributes

`tool_constructor` | Returns a class or instance of a tool to be tested.   ---|---   `tool_constructor_params` | Returns a dictionary of parameters to pass to the tool constructor.   `tool_invoke_params_example` | Returns a dictionary representing the "args" of an example tool call.      Methods

`test_async_invoke_matches_output_schema`\(tool\) | Test async invoke matches output schema.   ---|---   `test_async_invoke_no_tool_call`\(tool\) | If ainvoked without a ToolCall, the tool can return anything but it shouldn't throw an error.   `test_invoke_matches_output_schema`\(tool\) | Test invoke matches output schema.   `test_invoke_no_tool_call`\(tool\) | If invoked without a ToolCall, the tool can return anything but it shouldn't throw an error.      _async _test\_async\_invoke\_matches\_output\_schema\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/tools.html#ToolsIntegrationTests.test_async_invoke_matches_output_schema)\#     

Test async invoke matches output schema.

If ainvoked with a ToolCall, the tool should return a valid ToolMessage content.

For debugging tips, see `test_invoke_matches_output_schema()`.

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

_async _test\_async\_invoke\_no\_tool\_call\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/tools.html#ToolsIntegrationTests.test_async_invoke_no_tool_call)\#     

If ainvoked without a ToolCall, the tool can return anything but it shouldn’t throw an error.

For debugging tips, see `test_invoke_no_tool_call()`.

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

test\_invoke\_matches\_output\_schema\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/tools.html#ToolsIntegrationTests.test_invoke_matches_output_schema)\#     

Test invoke matches output schema.

If invoked with a ToolCall, the tool should return a valid ToolMessage content.

If you have followed the [custom tool guide](https://python.langchain.com/docs/how_to/custom_tools/), this test should always pass because ToolCall inputs are handled by the `langchain_core.tools.BaseTool` class.

If you have not followed this guide, you should ensure that your tool’s invoke method returns a valid ToolMessage content when it receives a dict representing a ToolCall as input \(as opposed to distinct args\).

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

test\_invoke\_no\_tool\_call\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_tests/integration_tests/tools.html#ToolsIntegrationTests.test_invoke_no_tool_call)\#     

If invoked without a ToolCall, the tool can return anything but it shouldn’t throw an error.

If this test fails, your tool may not be handling the input you defined in tool\_invoke\_params\_example correctly, and it’s throwing an error.

This test doesn’t have any checks. It’s just to ensure that the tool doesn’t throw an error when invoked with a dictionary of kwargs.

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

None

__On this page