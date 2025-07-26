# NonLocals — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.NonLocals.html
**Word Count:** 74
**Links Count:** 211
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# NonLocals\#

_class _langchain\_core.runnables.utils.NonLocals[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#NonLocals)\#     

Get nonlocal variables accessed.

Create a NonLocals visitor.

Methods

`__init__`\(\) | Create a NonLocals visitor.   ---|---   `generic_visit`\(node\) | Called if no explicit visitor function exists for a node.   `visit`\(node\) | Visit a node.   `visit_Attribute`\(node\) | Visit an attribute node.   `visit_Constant`\(node\) |    `visit_Name`\(node\) | Visit a name node.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#NonLocals.__init__)\#     

Create a NonLocals visitor.

Return type:     

None

generic\_visit\(_node_\)\#     

Called if no explicit visitor function exists for a node.

visit\(_node_\)\#     

Visit a node.

visit\_Attribute\(

    _node : Attribute_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#NonLocals.visit_Attribute)\#     

Visit an attribute node.

Parameters:     

**node** \(_Attribute_\) – The node to visit.

Returns:     

The result of the visit.

Return type:     

Any

visit\_Constant\(_node_\)\#     

visit\_Name\(_node : Name_\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#NonLocals.visit_Name)\#     

Visit a name node.

Parameters:     

**node** \(_Name_\) – The node to visit.

Returns:     

The result of the visit.

Return type:     

Any

__On this page