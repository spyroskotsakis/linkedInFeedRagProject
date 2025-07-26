# CodeSegmenter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.code_segmenter.CodeSegmenter.html
**Word Count:** 15
**Links Count:** 401
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# CodeSegmenter\#

_class _langchain\_community.document\_loaders.parsers.language.code\_segmenter.CodeSegmenter\(_code : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/code_segmenter.html#CodeSegmenter)\#     

Abstract class for the code segmenter.

Methods

`__init__`\(code\) |    ---|---   `extract_functions_classes`\(\) |    `is_valid`\(\) |    `simplify_code`\(\) |       Parameters:     

**code** \(_str_\)

\_\_init\_\_\(_code : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/code_segmenter.html#CodeSegmenter.__init__)\#     

Parameters:     

**code** \(_str_\)

_abstractmethod _extract\_functions\_classes\(\) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/code_segmenter.html#CodeSegmenter.extract_functions_classes)\#     

Return type:     

_List_\[str\]

is\_valid\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/code_segmenter.html#CodeSegmenter.is_valid)\#     

Return type:     

bool

_abstractmethod _simplify\_code\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/code_segmenter.html#CodeSegmenter.simplify_code)\#     

Return type:     

str

__On this page