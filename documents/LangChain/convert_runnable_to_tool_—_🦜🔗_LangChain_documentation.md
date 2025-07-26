# convert_runnable_to_tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.convert_runnable_to_tool.html
**Word Count:** 57
**Links Count:** 118
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# convert\_runnable\_to\_tool\#

langchain\_core.tools.convert.convert\_runnable\_to\_tool\(

    _runnable : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")_,     _args\_schema : type\[BaseModel\] | None = None_,     _\*_ ,     _name : str | None = None_,     _description : str | None = None_,     _arg\_types : dict\[str, type\] | None = None_, \) → [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/convert.html#convert_runnable_to_tool)\#     

Convert a Runnable into a BaseTool.

Parameters:     

  * **runnable** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\) – The runnable to convert.

  * **args\_schema** \(_type_ _\[__BaseModel_ _\]__|__None_\) – The schema for the tool’s input arguments. Defaults to None.

  * **name** \(_str_ _|__None_\) – The name of the tool. Defaults to None.

  * **description** \(_str_ _|__None_\) – The description of the tool. Defaults to None.

  * **arg\_types** \(_dict_ _\[__str_ _,__type_ _\]__|__None_\) – The types of the arguments. Defaults to None.

Returns:     

The tool.

Return type:     

[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)