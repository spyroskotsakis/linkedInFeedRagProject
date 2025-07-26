# Node — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html
**Word Count:** 147
**Links Count:** 206
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# Node\#

_class _langchain\_core.runnables.graph.Node\(

    _id : str_,     _name : str_,     _data : type\[[BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\] | RunnableType | None_,     _metadata : dict\[str, Any\] | None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Node)\#     

Node in a graph.

Parameters:     

  * **id** \(_str_\) – The unique identifier of the node.

  * **name** \(_str_\) – The name of the node.

  * **data** \(_Union_ _\[__type_ _\[_[_BaseModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel") _\]__,__RunnableType_ _,__None_ _\]_\) – The data of the node.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional metadata for the node. Defaults to None.

Create new instance of Node\(id, name, data, metadata\)

Attributes

`data` | Alias for field number 2   ---|---   `id` | Alias for field number 0   `metadata` | Alias for field number 3   `name` | Alias for field number 1      Methods

`copy`\(\*\[, id, name\]\) | Return a copy of the node with optional new id and name.   ---|---   `count`\(value, /\) | Return number of occurrences of value.   `index`\(value\[, start, stop\]\) | Return first index of value.      copy\(

    _\*_ ,     _id : str | None = None_,     _name : str | None = None_, \) → Node[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Node.copy)\#     

Return a copy of the node with optional new id and name.

Parameters:     

  * **id** \(_str_ _|__None_\) – The new node id. Defaults to None.

  * **name** \(_str_ _|__None_\) – The new node name. Defaults to None.

Returns:     

A copy of the node with the new id and name.

Return type:     

_Node_

count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(_value_ , _start =0_, _stop =9223372036854775807_, _/_\)\#     

Return first index of value.

Raises ValueError if the value is not present.

Examples using Node

  * [Azure Cosmos DB for Apache Gremlin](https://python.langchain.com/docs/integrations/graphs/azure_cosmosdb_gremlin/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)