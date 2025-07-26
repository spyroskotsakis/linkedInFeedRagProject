# IsLocalDict — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.IsLocalDict.html
**Word Count:** 96
**Links Count:** 211
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# IsLocalDict\#

_class _langchain\_core.runnables.utils.IsLocalDict\(_name : str_, _keys : set\[str\]_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#IsLocalDict)\#     

Check if a name is a local dict.

Initialize the visitor.

Parameters:     

  * **name** \(_str_\) – The name to check.

  * **keys** \(_set_ _\[__str_ _\]_\) – The keys to populate.

Methods

`__init__`\(name, keys\) | Initialize the visitor.   ---|---   `generic_visit`\(node\) | Called if no explicit visitor function exists for a node.   `visit`\(node\) | Visit a node.   `visit_Call`\(node\) | Visit a call node.   `visit_Constant`\(node\) |    `visit_Subscript`\(node\) | Visit a subscript node.      \_\_init\_\_\(_name : str_, _keys : set\[str\]_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#IsLocalDict.__init__)\#     

Initialize the visitor.

Parameters:     

  * **name** \(_str_\) – The name to check.

  * **keys** \(_set_ _\[__str_ _\]_\) – The keys to populate.

Return type:     

None

generic\_visit\(_node_\)\#     

Called if no explicit visitor function exists for a node.

visit\(_node_\)\#     

Visit a node.

visit\_Call\(_node : Call_\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#IsLocalDict.visit_Call)\#     

Visit a call node.

Parameters:     

**node** \(_Call_\) – The node to visit.

Returns:     

The result of the visit.

Return type:     

Any

visit\_Constant\(_node_\)\#     

visit\_Subscript\(

    _node : Subscript_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#IsLocalDict.visit_Subscript)\#     

Visit a subscript node.

Parameters:     

**node** \(_Subscript_\) – The node to visit.

Returns:     

The result of the visit.

Return type:     

Any

__On this page