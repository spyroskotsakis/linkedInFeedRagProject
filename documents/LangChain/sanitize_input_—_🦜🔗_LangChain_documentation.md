# sanitize_input — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/tools/langchain_experimental.tools.python.tool.sanitize_input.html
**Word Count:** 31
**Links Count:** 98
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# sanitize\_input\#

langchain\_experimental.tools.python.tool.sanitize\_input\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tools/python/tool.html#sanitize_input)\#     

Sanitize input to the python REPL.

Remove whitespace, backtick & python \(if llm mistakes python console as terminal\)

Parameters:     

**query** \(_str_\) – The query to sanitize

Returns:     

The sanitized query

Return type:     

str

__On this page