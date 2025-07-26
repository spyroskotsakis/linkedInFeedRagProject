# add_last_line_print — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.e2b_data_analysis.tool.add_last_line_print.html
**Word Count:** 58
**Links Count:** 407
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# add\_last\_line\_print\#

langchain\_community.tools.e2b\_data\_analysis.tool.add\_last\_line\_print\(_code : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/e2b_data_analysis/tool.html#add_last_line_print)\#     

Add print statement to the last line if it’s missing.

Sometimes, the LLM-generated code doesn’t have print\(variable\_name\), instead the     

LLM tries to print the variable only by writing variable\_name \(as you would in REPL, for example\).

This methods checks the AST of the generated Python code and adds the print     

statement to the last line if it’s missing.

Parameters:     

**code** \(_str_\)

Return type:     

str

__On this page