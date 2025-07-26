# render_text_description — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.render.render_text_description.html
**Word Count:** 55
**Links Count:** 118
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# render\_text\_description\#

langchain\_core.tools.render.render\_text\_description\(

    _tools : list\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/render.html#render_text_description)\#     

Render the tool name and description in plain text.

Parameters:     

**tools** \(_list_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – The tools to render.

Returns:     

The rendered text.

Return type:     

str

Output will be in the format of:               search: This tool is used for search     calculator: This tool is used for math     

Examples using render\_text\_description

  * [How to add ad-hoc tool calling capability to LLMs and Chat Models](https://python.langchain.com/docs/how_to/tools_prompting/)

  * [MLX](https://python.langchain.com/docs/integrations/chat/mlx/)

__On this page