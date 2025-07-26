# draw_mermaid — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_mermaid.draw_mermaid.html
**Word Count:** 130
**Links Count:** 198
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# draw\_mermaid\#

langchain\_core.runnables.graph\_mermaid.draw\_mermaid\(

    _nodes : dict\[str, [Node](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Node.html#langchain_core.runnables.graph.Node "langchain_core.runnables.graph.Node")\]_,     _edges : list\[[Edge](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Edge.html#langchain_core.runnables.graph.Edge "langchain_core.runnables.graph.Edge")\]_,     _\*_ ,     _first\_node : str | None = None_,     _last\_node : str | None = None_,     _with\_styles : bool = True_,     _curve\_style : [CurveStyle](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.CurveStyle.html#langchain_core.runnables.graph.CurveStyle "langchain_core.runnables.graph.CurveStyle") = CurveStyle.LINEAR_,     _node\_styles : [NodeStyles](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.NodeStyles.html#langchain_core.runnables.graph.NodeStyles "langchain_core.runnables.graph.NodeStyles") | None = None_,     _wrap\_label\_n\_words : int = 9_,     _frontmatter\_config : dict\[str, Any\] | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_mermaid.html#draw_mermaid)\#     

Draws a Mermaid graph using the provided graph data.

Parameters:     

  * **nodes** \(_dict_ _\[__str_ _,__str_ _\]_\) – List of node ids.

  * **edges** \(_list_ _\[_[_Edge_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Edge.html#langchain_core.runnables.graph.Edge "langchain_core.runnables.graph.Edge") _\]_\) – List of edges, object with a source, target and data.

  * **first\_node** \(_str_ _,__optional_\) – Id of the first node. Defaults to None.

  * **last\_node** \(_str_ _,__optional_\) – Id of the last node. Defaults to None.

  * **with\_styles** \(_bool_ _,__optional_\) – Whether to include styles in the graph. Defaults to True.

  * **curve\_style** \([_CurveStyle_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.CurveStyle.html#langchain_core.runnables.graph.CurveStyle "langchain_core.runnables.graph.CurveStyle") _,__optional_\) – Curve style for the edges. Defaults to CurveStyle.LINEAR.

  * **node\_styles** \([_NodeStyles_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.NodeStyles.html#langchain_core.runnables.graph.NodeStyles "langchain_core.runnables.graph.NodeStyles") _,__optional_\) – Node colors for different types. Defaults to NodeStyles\(\).

  * **wrap\_label\_n\_words** \(_int_ _,__optional_\) – Words to wrap the edge labels. Defaults to 9.

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

Mermaid graph syntax.

Return type:     

str

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)