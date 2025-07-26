# TreeSitterSegmenter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.tree_sitter_segmenter.TreeSitterSegmenter.html
**Word Count:** 21
**Links Count:** 420
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# TreeSitterSegmenter\#

_class _langchain\_community.document\_loaders.parsers.language.tree\_sitter\_segmenter.TreeSitterSegmenter\(_code : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/tree_sitter_segmenter.html#TreeSitterSegmenter)\#     

Abstract class for \`CodeSegmenter\`s that use the tree-sitter library.

Methods

`__init__`\(code\) |    ---|---   `extract_functions_classes`\(\) |    `get_chunk_query`\(\) |    `get_language`\(\) |    `get_parser`\(\) |    `is_valid`\(\) |    `make_line_comment`\(text\) |    `simplify_code`\(\) |       Parameters:     

**code** \(_str_\)

\_\_init\_\_\(_code : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/tree_sitter_segmenter.html#TreeSitterSegmenter.__init__)\#     

Parameters:     

**code** \(_str_\)

extract\_functions\_classes\(\) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/tree_sitter_segmenter.html#TreeSitterSegmenter.extract_functions_classes)\#     

Return type:     

_List_\[str\]

_abstractmethod _get\_chunk\_query\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/tree_sitter_segmenter.html#TreeSitterSegmenter.get_chunk_query)\#     

Return type:     

str

_abstractmethod _get\_language\(\) → [Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/tree_sitter_segmenter.html#TreeSitterSegmenter.get_language)\#     

Return type:     

[Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")

get\_parser\(\) → Parser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/tree_sitter_segmenter.html#TreeSitterSegmenter.get_parser)\#     

Return type:     

Parser

is\_valid\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/tree_sitter_segmenter.html#TreeSitterSegmenter.is_valid)\#     

Return type:     

bool

_abstractmethod _make\_line\_comment\(_text : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/tree_sitter_segmenter.html#TreeSitterSegmenter.make_line_comment)\#     

Parameters:     

**text** \(_str_\)

Return type:     

str

simplify\_code\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/tree_sitter_segmenter.html#TreeSitterSegmenter.simplify_code)\#     

Return type:     

str

__On this page