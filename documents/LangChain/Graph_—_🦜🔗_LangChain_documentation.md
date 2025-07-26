# Graph — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Graph.html
**Word Count:** 855
**Links Count:** 301
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# Graph\#

_class _langchain\_core.runnables.graph.Graph\(

    _nodes: dict\[str_,     _~langchain\_core.runnables.graph.Node\] = <factory>_,     _edges: list\[~langchain\_core.runnables.graph.Edge\] = <factory>_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph)\#     

Graph of nodes and edges.

Parameters:     

  * **nodes** \(_dict_ _\[__str_ _,_[_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") _\]_\) – Dictionary of nodes in the graph. Defaults to an empty dictionary.

  * **edges** \(_list_ _\[_[_Edge_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Edge.html#langchain_core.runnables.graph.Edge "langchain_core.runnables.graph.Edge") _\]_\) – List of edges in the graph. Defaults to an empty list.

Attributes

Methods

`__init__`\(\[nodes, edges\]\) |    ---|---   `add_edge`\(source, target\[, data, conditional\]\) | Add an edge to the graph and return it.   `add_node`\(data\[, id, metadata\]\) | Add a node to the graph and return it.   `draw_ascii`\(\) | Draw the graph as an ASCII art string.   `draw_mermaid`\(\*\[, with\_styles, curve\_style, ...\]\) | Draw the graph as a Mermaid syntax string.   `draw_mermaid_png`\(\*\[, curve\_style, ...\]\) | Draw the graph as a PNG image using Mermaid.   `draw_png`\(\) | Draw the graph as a PNG image.   `extend`\(graph, \*\[, prefix\]\) | Add all nodes and edges from another graph.   `first_node`\(\) | Find the single node that is not a target of any edge.   `last_node`\(\) | Find the single node that is not a source of any edge.   `next_id`\(\) | Return a new unique node identifier.   `print_ascii`\(\) | Print the graph as an ASCII art string.   `reid`\(\) | Return a new graph with all nodes re-identified.   `remove_node`\(node\) | Remove a node from the graph and all edges connected to it.   `to_json`\(\*\[, with\_schemas\]\) | Convert the graph to a JSON-serializable format.   `trim_first_node`\(\) | Remove the first node if it exists and has a single outgoing edge.   `trim_last_node`\(\) | Remove the last node if it exists and has a single incoming edge.      \_\_init\_\_\(

    _nodes: dict\[str_,     _~langchain\_core.runnables.graph.Node\] = <factory>_,     _edges: list\[~langchain\_core.runnables.graph.Edge\] = <factory>_, \) → None\#     

Parameters:     

  * **nodes** \(_dict_ _\[__str_ _,_[_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") _\]_\)

  * **edges** \(_list_ _\[_[_Edge_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Edge.html#langchain_core.runnables.graph.Edge "langchain_core.runnables.graph.Edge") _\]_\)

Return type:     

None

add\_edge\(

    _source : [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")_,     _target : [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")_,     _data : [Stringifiable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Stringifiable.html#langchain_core.runnables.graph.Stringifiable "langchain_core.runnables.graph.Stringifiable") | None = None_,     _conditional : bool = False_, \) → [Edge](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Edge.html#langchain_core.runnables.graph.Edge "langchain_core.runnables.graph.Edge")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.add_edge)\#     

Add an edge to the graph and return it.

Parameters:     

  * **source** \([_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")\) – The source node of the edge.

  * **target** \([_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")\) – The target node of the edge.

  * **data** \([_Stringifiable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Stringifiable.html#langchain_core.runnables.graph.Stringifiable "langchain_core.runnables.graph.Stringifiable") _|__None_\) – Optional data associated with the edge. Defaults to None.

  * **conditional** \(_bool_\) – Whether the edge is conditional. Defaults to False.

Returns:     

The edge that was added to the graph.

Raises:     

**ValueError** – If the source or target node is not in the graph.

Return type:     

[_Edge_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Edge.html#langchain_core.runnables.graph.Edge "langchain_core.runnables.graph.Edge")

add\_node\(

    _data : type\[[BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\] | RunnableType | None_,     _id : str | None = None_,     _\*_ ,     _metadata : dict\[str, Any\] | None = None_, \) → [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.add_node)\#     

Add a node to the graph and return it.

Parameters:     

  * **data** \(_Union_ _\[__type_ _\[_[_BaseModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel") _\]__,__RunnableType_ _,__None_ _\]_\) – The data of the node.

  * **id** \(_Optional_ _\[__str_ _\]_\) – The id of the node. Defaults to None.

  * **metadata** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional metadata for the node. Defaults to None.

Returns:     

The node that was added to the graph.

Raises:     

**ValueError** – If a node with the same id already exists.

Return type:     

[Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")

draw\_ascii\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.draw_ascii)\#     

Draw the graph as an ASCII art string.

Return type:     

str

draw\_mermaid\(

    _\*_ ,     _with\_styles : bool = True_,     _curve\_style : [CurveStyle](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.CurveStyle.html#langchain_core.runnables.graph.CurveStyle "langchain_core.runnables.graph.CurveStyle") = CurveStyle.LINEAR_,     _node\_colors : [NodeStyles](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.NodeStyles.html#langchain_core.runnables.graph.NodeStyles "langchain_core.runnables.graph.NodeStyles") | None = None_,     _wrap\_label\_n\_words : int = 9_,     _frontmatter\_config : dict\[str, Any\] | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.draw_mermaid)\#     

Draw the graph as a Mermaid syntax string.

Parameters:     

  * **with\_styles** \(_bool_\) – Whether to include styles in the syntax. Defaults to True.

  * **curve\_style** \([_CurveStyle_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.CurveStyle.html#langchain_core.runnables.graph.CurveStyle "langchain_core.runnables.graph.CurveStyle")\) – The style of the edges. Defaults to CurveStyle.LINEAR.

  * **node\_colors** \([_NodeStyles_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.NodeStyles.html#langchain_core.runnables.graph.NodeStyles "langchain_core.runnables.graph.NodeStyles") _|__None_\) – The colors of the nodes. Defaults to NodeStyles\(\).

  * **wrap\_label\_n\_words** \(_int_\) – The number of words to wrap the node labels at. Defaults to 9.

  * **frontmatter\_config** \(_dict_ _\[__str_ _,__Any_ _\]__,__optional_\) – 

Mermaid frontmatter config. Can be used to customize theme and styles. Will be converted to YAML and added to the beginning of the mermaid graph. Defaults to None.

See more here: <https://mermaid.js.org/config/configuration.html>.

Example config:                  

\{     

“config”: \{     

“theme”: “neutral”, “look”: “handDrawn”, “themeVariables”: \{ “primaryColor”: “\#e2e2e2”\},

\}

\}

Returns:     

The Mermaid syntax string.

Return type:     

str

draw\_mermaid\_png\(

    _\*_ ,     _curve\_style : [CurveStyle](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.CurveStyle.html#langchain_core.runnables.graph.CurveStyle "langchain_core.runnables.graph.CurveStyle") = CurveStyle.LINEAR_,     _node\_colors : [NodeStyles](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.NodeStyles.html#langchain_core.runnables.graph.NodeStyles "langchain_core.runnables.graph.NodeStyles") | None = None_,     _wrap\_label\_n\_words : int = 9_,     _output\_file\_path : str | None = None_,     _draw\_method : [MermaidDrawMethod](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.MermaidDrawMethod.html#langchain_core.runnables.graph.MermaidDrawMethod "langchain_core.runnables.graph.MermaidDrawMethod") = MermaidDrawMethod.API_,     _background\_color : str = 'white'_,     _padding : int = 10_,     _max\_retries : int = 1_,     _retry\_delay : float = 1.0_,     _frontmatter\_config : dict\[str, Any\] | None = None_, \) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.draw_mermaid_png)\#     

Draw the graph as a PNG image using Mermaid.

Parameters:     

  * **curve\_style** \([_CurveStyle_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.CurveStyle.html#langchain_core.runnables.graph.CurveStyle "langchain_core.runnables.graph.CurveStyle")\) – The style of the edges. Defaults to CurveStyle.LINEAR.

  * **node\_colors** \([_NodeStyles_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.NodeStyles.html#langchain_core.runnables.graph.NodeStyles "langchain_core.runnables.graph.NodeStyles") _|__None_\) – The colors of the nodes. Defaults to NodeStyles\(\).

  * **wrap\_label\_n\_words** \(_int_\) – The number of words to wrap the node labels at. Defaults to 9.

  * **output\_file\_path** \(_str_ _|__None_\) – The path to save the image to. If None, the image is not saved. Defaults to None.

  * **draw\_method** \([_MermaidDrawMethod_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.MermaidDrawMethod.html#langchain_core.runnables.graph.MermaidDrawMethod "langchain_core.runnables.graph.MermaidDrawMethod")\) – The method to use to draw the graph. Defaults to MermaidDrawMethod.API.

  * **background\_color** \(_str_\) – The color of the background. Defaults to “white”.

  * **padding** \(_int_\) – The padding around the graph. Defaults to 10.

  * **max\_retries** \(_int_\) – The maximum number of retries \(MermaidDrawMethod.API\). Defaults to 1.

  * **retry\_delay** \(_float_\) – The delay between retries \(MermaidDrawMethod.API\). Defaults to 1.0.

  * **frontmatter\_config** \(_dict_ _\[__str_ _,__Any_ _\]__,__optional_\) – 

Mermaid frontmatter config. Can be used to customize theme and styles. Will be converted to YAML and added to the beginning of the mermaid graph. Defaults to None.

See more here: <https://mermaid.js.org/config/configuration.html>.

Example config:                  

\{     

“config”: \{     

“theme”: “neutral”, “look”: “handDrawn”, “themeVariables”: \{ “primaryColor”: “\#e2e2e2”\},

\}

\}

Returns:     

The PNG image as bytes.

Return type:     

bytes

draw\_png\(

    _output\_file\_path : str_,     _fontname : str | None = None_,     _labels : [LabelsDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.LabelsDict.html#langchain_core.runnables.graph.LabelsDict "langchain_core.runnables.graph.LabelsDict") | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.draw_png)\# draw\_png\(

    _output\_file\_path : None_,     _fontname : str | None = None_,     _labels : [LabelsDict](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.LabelsDict.html#langchain_core.runnables.graph.LabelsDict "langchain_core.runnables.graph.LabelsDict") | None = None_, \) → bytes     

Draw the graph as a PNG image.

Parameters:     

  * **output\_file\_path** – The path to save the image to. If None, the image is not saved. Defaults to None.

  * **fontname** – The name of the font to use. Defaults to None.

  * **labels** – Optional labels for nodes and edges in the graph. Defaults to None.

Returns:     

The PNG image as bytes if output\_file\_path is None, None otherwise.

extend\(

    _graph : Graph_,     _\*_ ,     _prefix : str = ''_, \) → tuple\[[Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") | None, [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.extend)\#     

Add all nodes and edges from another graph.

Note this doesn’t check for duplicates, nor does it connect the graphs.

Parameters:     

  * **graph** \(_Graph_\) – The graph to add.

  * **prefix** \(_str_\) – The prefix to add to the node ids. Defaults to “”.

Returns:     

A tuple of the first and last nodes of the subgraph.

Return type:     

tuple\[[_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") | None, [_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") | None\]

first\_node\(\) → [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.first_node)\#     

Find the single node that is not a target of any edge.

If there is no such node, or there are multiple, return None. When drawing the graph, this node would be the origin.

Return type:     

[_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") | None

last\_node\(\) → [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.last_node)\#     

Find the single node that is not a source of any edge.

If there is no such node, or there are multiple, return None. When drawing the graph, this node would be the destination.

Return type:     

[_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node") | None

next\_id\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.next_id)\#     

Return a new unique node identifier.

It that can be used to add a node to the graph.

Return type:     

str

print\_ascii\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.print_ascii)\#     

Print the graph as an ASCII art string.

Return type:     

None

reid\(\) → Graph[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.reid)\#     

Return a new graph with all nodes re-identified.

Uses their unique, readable names where possible.

Return type:     

_Graph_

remove\_node\(

    _node : [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.remove_node)\#     

Remove a node from the graph and all edges connected to it.

Parameters:     

**node** \([_Node_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")\) – The node to remove.

Return type:     

None

to\_json\(

    _\*_ ,     _with\_schemas : bool = False_, \) → dict\[str, list\[dict\[str, Any\]\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.to_json)\#     

Convert the graph to a JSON-serializable format.

Parameters:     

**with\_schemas** \(_bool_\) – Whether to include the schemas of the nodes if they are Pydantic models. Defaults to False.

Returns:     

A dictionary with the nodes and edges of the graph.

Return type:     

dict\[str, list\[dict\[str, _Any_\]\]\]

trim\_first\_node\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.trim_first_node)\#     

Remove the first node if it exists and has a single outgoing edge.

i.e., if removing it would not leave the graph without a “first” node.

Return type:     

None

trim\_last\_node\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Graph.trim_last_node)\#     

Remove the last node if it exists and has a single incoming edge.

i.e., if removing it would not leave the graph without a “last” node.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)