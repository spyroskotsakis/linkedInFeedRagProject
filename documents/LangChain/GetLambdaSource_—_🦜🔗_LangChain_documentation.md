# GetLambdaSource — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.GetLambdaSource.html
**Word Count:** 59
**Links Count:** 207
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# GetLambdaSource\#

_class _langchain\_core.runnables.utils.GetLambdaSource[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#GetLambdaSource)\#     

Get the source code of a lambda function.

Initialize the visitor.

Methods

`__init__`\(\) | Initialize the visitor.   ---|---   `generic_visit`\(node\) | Called if no explicit visitor function exists for a node.   `visit`\(node\) | Visit a node.   `visit_Constant`\(node\) |    `visit_Lambda`\(node\) | Visit a lambda function.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#GetLambdaSource.__init__)\#     

Initialize the visitor.

Return type:     

None

generic\_visit\(_node_\)\#     

Called if no explicit visitor function exists for a node.

visit\(_node_\)\#     

Visit a node.

visit\_Constant\(_node_\)\#     

visit\_Lambda\(

    _node : Lambda_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#GetLambdaSource.visit_Lambda)\#     

Visit a lambda function.

Parameters:     

**node** \(_Lambda_\) – The node to visit.

Returns:     

The result of the visit.

Return type:     

Any

__On this page