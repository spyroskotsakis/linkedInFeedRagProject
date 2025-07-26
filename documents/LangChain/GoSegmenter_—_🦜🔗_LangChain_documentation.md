# GoSegmenter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.go.GoSegmenter.html
**Word Count:** 17
**Links Count:** 414
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# GoSegmenter\#

_class _langchain\_community.document\_loaders.parsers.language.go.GoSegmenter\(_code : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/go.html#GoSegmenter)\#     

Code segmenter for Go.

Methods

`__init__`\(code\) |    ---|---   `extract_functions_classes`\(\) |    `get_chunk_query`\(\) |    `get_language`\(\) |    `get_parser`\(\) |    `is_valid`\(\) |    `make_line_comment`\(text\) |    `simplify_code`\(\) |       Parameters:     

**code** \(_str_\)

\_\_init\_\_\(_code : str_\)\#     

Parameters:     

**code** \(_str_\)

extract\_functions\_classes\(\) → List\[str\]\#     

Return type:     

_List_\[str\]

get\_chunk\_query\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/go.html#GoSegmenter.get_chunk_query)\#     

Return type:     

str

get\_language\(\) → [Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/go.html#GoSegmenter.get_language)\#     

Return type:     

[Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")

get\_parser\(\) → Parser\#     

Return type:     

Parser

is\_valid\(\) → bool\#     

Return type:     

bool

make\_line\_comment\(_text : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/go.html#GoSegmenter.make_line_comment)\#     

Parameters:     

**text** \(_str_\)

Return type:     

str

simplify\_code\(\) → str\#     

Return type:     

str

__On this page