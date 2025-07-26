# IsFunctionArgDict — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.IsFunctionArgDict.html
**Word Count:** 99
**Links Count:** 215
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# IsFunctionArgDict\#

_class _langchain\_core.runnables.utils.IsFunctionArgDict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#IsFunctionArgDict)\#     

Check if the first argument of a function is a dict.

Create a IsFunctionArgDict visitor.

Methods

`__init__`\(\) | Create a IsFunctionArgDict visitor.   ---|---   `generic_visit`\(node\) | Called if no explicit visitor function exists for a node.   `visit`\(node\) | Visit a node.   `visit_AsyncFunctionDef`\(node\) | Visit an async function definition.   `visit_Constant`\(node\) |    `visit_FunctionDef`\(node\) | Visit a function definition.   `visit_Lambda`\(node\) | Visit a lambda function.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#IsFunctionArgDict.__init__)\#     

Create a IsFunctionArgDict visitor.

Return type:     

None

generic\_visit\(_node_\)\#     

Called if no explicit visitor function exists for a node.

visit\(_node_\)\#     

Visit a node.

visit\_AsyncFunctionDef\(

    _node : AsyncFunctionDef_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#IsFunctionArgDict.visit_AsyncFunctionDef)\#     

Visit an async function definition.

Parameters:     

**node** \(_AsyncFunctionDef_\) – The node to visit.

Returns:     

The result of the visit.

Return type:     

Any

visit\_Constant\(_node_\)\#     

visit\_FunctionDef\(

    _node : FunctionDef_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#IsFunctionArgDict.visit_FunctionDef)\#     

Visit a function definition.

Parameters:     

**node** \(_FunctionDef_\) – The node to visit.

Returns:     

The result of the visit.

Return type:     

Any

visit\_Lambda\(

    _node : Lambda_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#IsFunctionArgDict.visit_Lambda)\#     

Visit a lambda function.

Parameters:     

**node** \(_Lambda_\) – The node to visit.

Returns:     

The result of the visit.

Return type:     

Any

__On this page