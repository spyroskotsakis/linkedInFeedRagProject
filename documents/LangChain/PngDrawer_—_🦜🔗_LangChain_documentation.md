# PngDrawer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_png.PngDrawer.html
**Word Count:** 402
**Links Count:** 238
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# PngDrawer\#

_class _langchain\_core.runnables.graph\_png.PngDrawer\(

    _fontname : str | None = None_,     _labels : [LabelsDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.LabelsDict.html#langchain_core.runnables.graph.LabelsDict "langchain_core.runnables.graph.LabelsDict") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer)\#     

Helper class to draw a state graph into a PNG file.

It requires graphviz and pygraphviz to be installed. :param fontname: The font to use for the labels :param labels: A dictionary of label overrides. The dictionary

> should have the following format: \{ >
>> “nodes”: \{ >>      >>  >> “node1”: “CustomLabel1”, “node2”: “CustomLabel2”, “\_\_end\_\_”: “End Node” >>  >> \}, “edges”: \{ >> >>> “continue”: “ContinueLabel”, “end”: “EndLabel” >>  >> \} >  > \} The keys are the original labels, and the values are the new labels.

Usage:     

drawer = PngDrawer\(\) drawer.draw\(state\_graph, ‘graph.png’\)

Initializes the PNG drawer.

Parameters:     

  * **fontname** \(_str_ _|__None_\) – The font to use for the labels. Defaults to “arial”.

  * **labels** \([_LabelsDict_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.LabelsDict.html#langchain_core.runnables.graph.LabelsDict "langchain_core.runnables.graph.LabelsDict") _|__None_\) – 

A dictionary of label overrides. The dictionary should have the following format: \{

> ”nodes”: \{ >      >  > “node1”: “CustomLabel1”, “node2”: “CustomLabel2”, “\_\_end\_\_”: “End Node” >  > \}, “edges”: \{ >
>> ”continue”: “ContinueLabel”, “end”: “EndLabel” >  > \}

\} The keys are the original labels, and the values are the new labels. Defaults to None.

Methods

`__init__`\(\[fontname, labels\]\) | Initializes the PNG drawer.   ---|---   `add_edge`\(viz, source, target\[, label, ...\]\) | Adds an edge to the graph.   `add_edges`\(viz, graph\) | Add edges to the graph.   `add_node`\(viz, node\) | Adds a node to the graph.   `add_nodes`\(viz, graph\) | Add nodes to the graph.   `draw`\(graph\[, output\_path\]\) | Draw the given state graph into a PNG file.   `get_edge_label`\(label\) | Returns the label to use for an edge.   `get_node_label`\(label\) | Returns the label to use for a node.   `update_styles`\(viz, graph\) | Update the styles of the entrypoint and END nodes.      \_\_init\_\_\(

    _fontname : str | None = None_,     _labels : [LabelsDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.LabelsDict.html#langchain_core.runnables.graph.LabelsDict "langchain_core.runnables.graph.LabelsDict") | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer.__init__)\#     

Initializes the PNG drawer.

Parameters:     

  * **fontname** \(_str_ _|__None_\) – The font to use for the labels. Defaults to “arial”.

  * **labels** \([_LabelsDict_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.LabelsDict.html#langchain_core.runnables.graph.LabelsDict "langchain_core.runnables.graph.LabelsDict") _|__None_\) – 

A dictionary of label overrides. The dictionary should have the following format: \{

> ”nodes”: \{ >      >  > “node1”: “CustomLabel1”, “node2”: “CustomLabel2”, “\_\_end\_\_”: “End Node” >  > \}, “edges”: \{ >
>> ”continue”: “ContinueLabel”, “end”: “EndLabel” >  > \}

\} The keys are the original labels, and the values are the new labels. Defaults to None.

Return type:     

None

add\_edge\(

    _viz : Any_,     _source : str_,     _target : str_,     _label : str | None = None_,     _conditional : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer.add_edge)\#     

Adds an edge to the graph.

Parameters:     

  * **viz** \(_Any_\) – The graphviz object.

  * **source** \(_str_\) – The source node.

  * **target** \(_str_\) – The target node.

  * **label** \(_str_ _|__None_\) – The label for the edge. Defaults to None.

  * **conditional** \(_bool_\) – Whether the edge is conditional. Defaults to False.

Returns:     

None

Return type:     

None

add\_edges\(

    _viz : Any_,     _graph : [Graph](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer.add_edges)\#     

Add edges to the graph.

Parameters:     

  * **viz** \(_Any_\) – The graphviz object.

  * **graph** \([_Graph_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")\) – The graph to draw.

Return type:     

None

add\_node\(_viz : Any_, _node : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer.add_node)\#     

Adds a node to the graph.

Parameters:     

  * **viz** \(_Any_\) – The graphviz object.

  * **node** \(_str_\) – The node to add.

Returns:     

None

Return type:     

None

add\_nodes\(

    _viz : Any_,     _graph : [Graph](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer.add_nodes)\#     

Add nodes to the graph.

Parameters:     

  * **viz** \(_Any_\) – The graphviz object.

  * **graph** \([_Graph_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")\) – The graph to draw.

Return type:     

None

draw\(

    _graph : [Graph](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")_,     _output\_path : str | None = None_, \) → bytes | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer.draw)\#     

Draw the given state graph into a PNG file.

Requires graphviz and pygraphviz to be installed. :param graph: The graph to draw :param output\_path: The path to save the PNG. If None, PNG bytes are returned.

Parameters:     

  * **graph** \([_Graph_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")\)

  * **output\_path** \(_str_ _|__None_\)

Return type:     

bytes | None

get\_edge\_label\(_label : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer.get_edge_label)\#     

Returns the label to use for an edge.

Parameters:     

**label** \(_str_\) – The original label.

Returns:     

The new label.

Return type:     

str

get\_node\_label\(_label : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer.get_node_label)\#     

Returns the label to use for a node.

Parameters:     

**label** \(_str_\) – The original label.

Returns:     

The new label.

Return type:     

str

update\_styles\(

    _viz : Any_,     _graph : [Graph](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_png.html#PngDrawer.update_styles)\#     

Update the styles of the entrypoint and END nodes.

Parameters:     

  * **viz** \(_Any_\) – The graphviz object.

  * **graph** \([_Graph_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html#langchain_core.runnables.graph.Graph "langchain_core.runnables.graph.Graph")\) – The graph to draw.

Return type:     

None

__On this page