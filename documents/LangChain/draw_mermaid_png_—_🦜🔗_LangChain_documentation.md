# draw_mermaid_png — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph_mermaid.draw_mermaid_png.html
**Word Count:** 82
**Links Count:** 192
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# draw\_mermaid\_png\#

langchain\_core.runnables.graph\_mermaid.draw\_mermaid\_png\(

    _mermaid\_syntax : str_,     _output\_file\_path : str | None = None_,     _draw\_method : [MermaidDrawMethod](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.MermaidDrawMethod.html#langchain_core.runnables.graph.MermaidDrawMethod "langchain_core.runnables.graph.MermaidDrawMethod") = MermaidDrawMethod.API_,     _background\_color : str | None = 'white'_,     _padding : int = 10_,     _max\_retries : int = 1_,     _retry\_delay : float = 1.0_, \) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph_mermaid.html#draw_mermaid_png)\#     

Draws a Mermaid graph as PNG using provided syntax.

Parameters:     

  * **mermaid\_syntax** \(_str_\) – Mermaid graph syntax.

  * **output\_file\_path** \(_str_ _,__optional_\) – Path to save the PNG image. Defaults to None.

  * **draw\_method** \([_MermaidDrawMethod_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.MermaidDrawMethod.html#langchain_core.runnables.graph.MermaidDrawMethod "langchain_core.runnables.graph.MermaidDrawMethod") _,__optional_\) – Method to draw the graph. Defaults to MermaidDrawMethod.API.

  * **background\_color** \(_str_ _,__optional_\) – Background color of the image. Defaults to “white”.

  * **padding** \(_int_ _,__optional_\) – Padding around the image. Defaults to 10.

  * **max\_retries** \(_int_ _,__optional_\) – Maximum number of retries \(MermaidDrawMethod.API\). Defaults to 1.

  * **retry\_delay** \(_float_ _,__optional_\) – Delay between retries \(MermaidDrawMethod.API\). Defaults to 1.0.

Returns:     

PNG image bytes.

Return type:     

bytes

Raises:     

**ValueError** – If an invalid draw method is provided.

__On this page