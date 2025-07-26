# BearlyInterpreterTool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.bearly.tool.BearlyInterpreterTool.html
**Word Count:** 25
**Links Count:** 430
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# BearlyInterpreterTool\#

_class _langchain\_community.tools.bearly.tool.BearlyInterpreterTool\(_api\_key : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/bearly/tool.html#BearlyInterpreterTool)\#     

Tool for evaluating python code in a sandbox environment.

Attributes

`description` |    ---|---   `endpoint` |    `file_description` |    `files` |    `name` |       Methods

`__init__`\(api\_key\) |    ---|---   `add_file`\(source\_path, target\_path, description\) |    `as_tool`\(\) |    `clear_files`\(\) |    `make_input_files`\(\) |       Parameters:     

**api\_key** \(_str_\)

\_\_init\_\_\(_api\_key : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/bearly/tool.html#BearlyInterpreterTool.__init__)\#     

Parameters:     

**api\_key** \(_str_\)

add\_file\(

    _source\_path : str_,     _target\_path : str_,     _description : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/bearly/tool.html#BearlyInterpreterTool.add_file)\#     

Parameters:     

  * **source\_path** \(_str_\)

  * **target\_path** \(_str_\)

  * **description** \(_str_\)

Return type:     

None

as\_tool\(\) → [Tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.simple.Tool.html#langchain_core.tools.simple.Tool "langchain_core.tools.simple.Tool")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/bearly/tool.html#BearlyInterpreterTool.as_tool)\#     

Return type:     

[_Tool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.simple.Tool.html#langchain_core.tools.simple.Tool "langchain_core.tools.simple.Tool")

clear\_files\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/bearly/tool.html#BearlyInterpreterTool.clear_files)\#     

Return type:     

None

make\_input\_files\(\) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/bearly/tool.html#BearlyInterpreterTool.make_input_files)\#     

Return type:     

_List_\[dict\]

Examples using BearlyInterpreterTool

  * [Bearly Code Interpreter](https://python.langchain.com/docs/integrations/tools/bearly/)

__On this page