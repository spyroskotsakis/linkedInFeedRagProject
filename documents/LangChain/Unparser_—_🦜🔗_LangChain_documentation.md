# Unparser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.e2b_data_analysis.unparse.Unparser.html
**Word Count:** 109
**Links Count:** 431
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# Unparser\#

_class _langchain\_community.tools.e2b\_data\_analysis.unparse.Unparser\(_tree_ , _file =sys.stdout_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/e2b_data_analysis/unparse.html#Unparser)\#     

Traverse an AST and output source code for the abstract syntax; original formatting is disregarded.

Print the source for tree to file.

Attributes

`binop` |    ---|---   `boolops` |    `cmpops` |    `unop` |       Methods

`__init__`\(tree\[, file\]\) | Unparser\(tree, file=sys.stdout\) -> None.   ---|---   `dispatch`\(tree\) | Dispatcher function, dispatching tree type T to method \_T.   `enter`\(\) | Print ':', and increase the indentation.   `fill`\(\[text\]\) | Indent a piece of text, according to the current indentation level   `leave`\(\) | Decrease the indentation level.   `write`\(text\) | Append a piece of text to the current line.      \_\_init\_\_\(

    _tree_ ,     _file= <\_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/e2b_data_analysis/unparse.html#Unparser.__init__)\#     

Unparser\(tree, file=sys.stdout\) -> None. Print the source for tree to file.

dispatch\(_tree_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/e2b_data_analysis/unparse.html#Unparser.dispatch)\#     

Dispatcher function, dispatching tree type T to method \_T.

enter\(\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/e2b_data_analysis/unparse.html#Unparser.enter)\#     

Print ‘:’, and increase the indentation.

fill\(_text =''_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/e2b_data_analysis/unparse.html#Unparser.fill)\#     

Indent a piece of text, according to the current indentation level

leave\(\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/e2b_data_analysis/unparse.html#Unparser.leave)\#     

Decrease the indentation level.

write\(_text_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/e2b_data_analysis/unparse.html#Unparser.write)\#     

Append a piece of text to the current line.

__On this page