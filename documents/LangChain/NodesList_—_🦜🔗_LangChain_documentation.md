# NodesList — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.diffbot.NodesList.html
**Word Count:** 132
**Links Count:** 127
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# NodesList\#

_class _langchain\_experimental.graph\_transformers.diffbot.NodesList[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#NodesList)\#     

List of nodes with associated properties.

nodes\#     

Stores nodes as keys and their properties as values. Each key is a tuple where the first element is the node ID and the second is the node type.

Type:     

Dict\[Tuple, Any\]

Methods

`__init__`\(\) |    ---|---   `add_node_property`\(node, properties\) | Adds or updates node properties.   `return_node_list`\(\) | Returns the nodes as a list of Node objects.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#NodesList.__init__)\#     

Return type:     

None

add\_node\_property\(

    _node : Tuple\[str | int, str\]_,     _properties : Dict\[str, Any\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#NodesList.add_node_property)\#     

Adds or updates node properties.

If the node does not exist in the list, it’s added along with its properties. If the node already exists, its properties are updated with the new values.

Parameters:     

  * **node** \(_Tuple_\) – A tuple containing the node ID and node type.

  * **properties** \(_Dict_\) – A dictionary of properties to add or update for the node.

Return type:     

None

return\_node\_list\(\) → List\[[Node](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.Node.html#langchain_community.graphs.graph_document.Node "langchain_community.graphs.graph_document.Node")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#NodesList.return_node_list)\#     

Returns the nodes as a list of Node objects.

Each Node object will have its ID, type, and properties populated.

Returns:     

A list of Node objects.

Return type:     

List\[[Node](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.Node.html#langchain_neo4j.graphs.graph_document.Node "langchain_neo4j.graphs.graph_document.Node")\]

__On this page