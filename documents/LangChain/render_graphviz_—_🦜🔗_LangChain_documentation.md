# render_graphviz — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.visualize.render_graphviz.html
**Word Count:** 115
**Links Count:** 123
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# render\_graphviz\#

langchain\_community.graph\_vectorstores.visualize.render\_graphviz\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _engine : str | None = None_,     _node\_color : str | None = None_,     _node\_colors : Dict\[str, str | None\] | None = None_,     _skip\_tags : Iterable\[Tuple\[str, str\]\] = \(\)_, \) → graphviz.Digraph[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/visualize.html#render_graphviz)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Render a collection of GraphVectorStore documents to GraphViz format.

Parameters:     

  * **documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The documents to render.

  * **engine** \(_str_ _|__None_\) – GraphViz layout engine to use. None uses the default.

  * **node\_color** \(_str_ _|__None_\) – Default node color.

  * **node\_colors** \(_Dict_ _\[__str_ _,__str_ _|__None_ _\]__|__None_\) – Dictionary specifying colors of specific nodes. Useful for emphasizing nodes that were selected by MMR, or differ from other results.

  * **skip\_tags** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__str_ _\]__\]_\) – Set of tags to skip when rendering the graph. Specified as tuples containing the kind and tag.

Returns:     

The “graphviz.Digraph” representing the nodes. May be printed to source, or rendered using dot.

Return type:     

graphviz.Digraph

Note

To render the generated DOT source code, you also need to install Graphviz\_ \([download page](https://www.graphviz.org/download/), [archived versions](https://www2.graphviz.org/Archive/stable/), [installation procedure for Windows](https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224)\).

__On this page