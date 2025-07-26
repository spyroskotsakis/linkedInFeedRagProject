# create_simple_model — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.llm.create_simple_model.html
**Word Count:** 143
**Links Count:** 111
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# create\_simple\_model\#

langchain\_experimental.graph\_transformers.llm.create\_simple\_model\(

    _node\_labels : List\[str\] | None = None_,     _rel\_types : List\[str\] | List\[Tuple\[str, str, str\]\] | None = None_,     _node\_properties : bool | List\[str\] = False_,     _llm\_type : str | None = None_,     _relationship\_properties : bool | List\[str\] = False_,     _relationship\_type : str | None = None_, \) → Type\[\_Graph\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/llm.html#create_simple_model)\#     

Create a simple graph model with optional constraints on node and relationship types.

Parameters:     

  * **node\_labels** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Specifies the allowed node types. Defaults to None, allowing all node types.

  * **rel\_types** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Specifies the allowed relationship types. Defaults to None, allowing all relationship types.

  * **node\_properties** \(_Union_ _\[__bool_ _,__List_ _\[__str_ _\]__\]_\) – Specifies if node properties should be included. If a list is provided, only properties with keys in the list will be included. If True, all properties are included. Defaults to False.

  * **relationship\_properties** \(_Union_ _\[__bool_ _,__List_ _\[__str_ _\]__\]_\) – Specifies if relationship properties should be included. If a list is provided, only properties with keys in the list will be included. If True, all properties are included. Defaults to False.

  * **llm\_type** \(_Optional_ _\[__str_ _\]_\) – The type of the language model. Defaults to None. Only openai supports enum param: openai-chat.

  * **relationship\_type** \(_str_ _|__None_\)

Returns:     

A graph model with the specified constraints.

Return type:     

Type\[\_Graph\]

Raises:     

**ValueError** – If ‘id’ is included in the node or relationship properties list.

__On this page