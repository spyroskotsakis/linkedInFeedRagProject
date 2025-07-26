# node_data_json — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.node_data_json.html
**Word Count:** 54
**Links Count:** 192
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# node\_data\_json\#

langchain\_core.runnables.graph.node\_data\_json\(

    _node : [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")_,     _\*_ ,     _with\_schemas : bool = False_, \) → dict\[str, str | dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#node_data_json)\#     

Convert the data of a node to a JSON-serializable format.

Parameters:     

  * **node** \([_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")\) – The node to convert.

  * **with\_schemas** \(_bool_\) – Whether to include the schema of the data if it is a Pydantic model. Defaults to False.

Returns:     

A dictionary with the type of the data and the data itself.

Return type:     

dict\[str, str | dict\[str, _Any_\]\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)