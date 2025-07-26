# NetworkxEntityGraph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.NetworkxEntityGraph.html
**Word Count:** 289
**Links Count:** 209
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# NetworkxEntityGraph\#

_class _langchain\_community.graphs.networkx\_graph.NetworkxEntityGraph\(_graph : Any | None = None_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph)\#     

Networkx wrapper for entity graph operations.

_Security note_ : Make sure that the database connection uses credentials     

that are narrowly-scoped to only include necessary permissions. Failure to do so may result in data corruption or loss, since the calling code may attempt commands that would result in deletion, mutation of data if appropriately prompted or reading sensitive data if such data is present in the database. The best way to guard against such negative outcomes is to \(as appropriate\) limit the permissions granted to the credentials used with this tool.

See <https://python.langchain.com/docs/security> for more information.

Create a new graph.

Methods

`__init__`\(\[graph\]\) | Create a new graph.   ---|---   `add_node`\(node\) | Add node in the graph.   `add_triple`\(knowledge\_triple\) | Add a triple to the graph.   `clear`\(\) | Clear the graph.   `clear_edges`\(\) | Clear the graph edges.   `delete_triple`\(knowledge\_triple\) | Delete a triple from the graph.   `draw_graphviz`\(\*\*kwargs\) | Provides better drawing   `from_gml`\(gml\_path\) |    `get_entity_knowledge`\(entity\[, depth\]\) | Get information about an entity.   `get_neighbors`\(node\) | Return the neighbor nodes of the given node.   `get_number_of_nodes`\(\) | Get number of nodes in the graph.   `get_topological_sort`\(\) | Get a list of entity names in the graph sorted by causal dependence.   `get_triples`\(\) | Get all triples in the graph.   `has_edge`\(source\_node, destination\_node\) | Return if graph has an edge between the given nodes.   `has_node`\(node\) | Return if graph has the given node.   `remove_edge`\(source\_node, destination\_node\) | Remove edge from the graph.   `remove_node`\(node\) | Remove node from the graph.   `write_to_gml`\(path\) |       Parameters:     

**graph** \(_Optional_ _\[__Any_ _\]_\)

\_\_init\_\_\(

    _graph : Any | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.__init__)\#     

Create a new graph.

Parameters:     

**graph** \(_Any_ _|__None_\)

Return type:     

None

add\_node\(_node : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.add_node)\#     

Add node in the graph.

Parameters:     

**node** \(_str_\)

Return type:     

None

add\_triple\(

    _knowledge\_triple : [KnowledgeTriple](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.KnowledgeTriple.html#langchain_community.graphs.networkx_graph.KnowledgeTriple "langchain_community.graphs.networkx_graph.KnowledgeTriple")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.add_triple)\#     

Add a triple to the graph.

Parameters:     

**knowledge\_triple** \([_KnowledgeTriple_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.KnowledgeTriple.html#langchain_community.graphs.networkx_graph.KnowledgeTriple "langchain_community.graphs.networkx_graph.KnowledgeTriple")\)

Return type:     

None

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.clear)\#     

Clear the graph.

Return type:     

None

clear\_edges\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.clear_edges)\#     

Clear the graph edges.

Return type:     

None

delete\_triple\(

    _knowledge\_triple : [KnowledgeTriple](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.KnowledgeTriple.html#langchain_community.graphs.networkx_graph.KnowledgeTriple "langchain_community.graphs.networkx_graph.KnowledgeTriple")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.delete_triple)\#     

Delete a triple from the graph.

Parameters:     

**knowledge\_triple** \([_KnowledgeTriple_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.networkx_graph.KnowledgeTriple.html#langchain_community.graphs.networkx_graph.KnowledgeTriple "langchain_community.graphs.networkx_graph.KnowledgeTriple")\)

Return type:     

None

draw\_graphviz\(

    _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.draw_graphviz)\#     

Provides better drawing

Usage in a jupyter notebook:               >>> from IPython.display import SVG     >>> self.draw_graphviz_svg(layout="dot", filename="web.svg")     >>> SVG('web.svg')     

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_classmethod _from\_gml\(

    _gml\_path : str_, \) → NetworkxEntityGraph[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.from_gml)\#     

Parameters:     

**gml\_path** \(_str_\)

Return type:     

_NetworkxEntityGraph_

get\_entity\_knowledge\(

    _entity : str_,     _depth : int = 1_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.get_entity_knowledge)\#     

Get information about an entity.

Parameters:     

  * **entity** \(_str_\)

  * **depth** \(_int_\)

Return type:     

_List_\[str\]

get\_neighbors\(

    _node : str_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.get_neighbors)\#     

Return the neighbor nodes of the given node.

Parameters:     

**node** \(_str_\)

Return type:     

_List_\[str\]

get\_number\_of\_nodes\(\) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.get_number_of_nodes)\#     

Get number of nodes in the graph.

Return type:     

int

get\_topological\_sort\(\) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.get_topological_sort)\#     

Get a list of entity names in the graph sorted by causal dependence.

Return type:     

_List_\[str\]

get\_triples\(\) → List\[Tuple\[str, str, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.get_triples)\#     

Get all triples in the graph.

Return type:     

_List_\[_Tuple_\[str, str, str\]\]

has\_edge\(

    _source\_node : str_,     _destination\_node : str_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.has_edge)\#     

Return if graph has an edge between the given nodes.

Parameters:     

  * **source\_node** \(_str_\)

  * **destination\_node** \(_str_\)

Return type:     

bool

has\_node\(_node : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.has_node)\#     

Return if graph has the given node.

Parameters:     

**node** \(_str_\)

Return type:     

bool

remove\_edge\(

    _source\_node : str_,     _destination\_node : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.remove_edge)\#     

Remove edge from the graph.

Parameters:     

  * **source\_node** \(_str_\)

  * **destination\_node** \(_str_\)

Return type:     

None

remove\_node\(_node : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.remove_node)\#     

Remove node from the graph.

Parameters:     

**node** \(_str_\)

Return type:     

None

write\_to\_gml\(_path : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graphs/networkx_graph.html#NetworkxEntityGraph.write_to_gml)\#     

Parameters:     

**path** \(_str_\)

Return type:     

None

Examples using NetworkxEntityGraph

  * [NetworkX](https://python.langchain.com/docs/integrations/graphs/networkx/)

__On this page