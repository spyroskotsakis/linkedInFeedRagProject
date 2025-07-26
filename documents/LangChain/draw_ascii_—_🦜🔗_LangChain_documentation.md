# draw_ascii — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_ascii.draw_ascii.html
**Word Count:** 62
**Links Count:** 191
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# draw\_ascii\#

langchain\_core.runnables.graph\_ascii.draw\_ascii\(

    _vertices : Mapping\[str, str\]_,     _edges : Sequence\[[Edge](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Edge.html#langchain_core.runnables.graph.Edge "langchain_core.runnables.graph.Edge")\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_ascii.html#draw_ascii)\#     

Build a DAG and draw it in ASCII.

Parameters:     

  * **vertices** \(_list_\) – list of graph vertices.

  * **edges** \(_list_\) – list of graph edges.

Returns:     

ASCII representation

Return type:     

str

Example               from langchain_core.runnables.graph_ascii import draw_ascii          vertices = {1: "1", 2: "2", 3: "3", 4: "4"}     edges = [         (source, target, None, None)         for source, target in [(1, 2), (2, 3), (2, 4), (1, 4)]     ]               print(draw_ascii(vertices, edges))                         +---+          | 1 |          +---+          *    *         *     *        *       *     +---+       *     | 2 |       *     +---+**     *       *    **   *       *      ** *       *        **     +---+     +---+     | 3 |     | 4 |     +---+     +---+     

__On this page