# render_text_description_and_args — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.render.render_text_description_and_args.html
**Word Count:** 54
**Links Count:** 117
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# render\_text\_description\_and\_args\#

langchain\_core.tools.render.render\_text\_description\_and\_args\(

    _tools : list\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/render.html#render_text_description_and_args)\#     

Render the tool name, description, and args in plain text.

Parameters:     

**tools** \(_list_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – The tools to render.

Returns:     

The rendered text.

Return type:     

str

Output will be in the format of:               search: This tool is used for search, args: {"query": {"type": "string"}}     calculator: This tool is used for math, args: {"expression": {"type": "string"}}     

Examples using render\_text\_description\_and\_args

  * [Amadeus Toolkit](https://python.langchain.com/docs/integrations/tools/amadeus/)

__On this page