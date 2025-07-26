# SQLSegmenter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.sql.SQLSegmenter.html
**Word Count:** 126
**Links Count:** 416
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# SQLSegmenter\#

_class _langchain\_community.document\_loaders.parsers.language.sql.SQLSegmenter\(_code : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/sql.html#SQLSegmenter)\#     

Code segmenter for SQL. This class uses Tree-sitter to segment SQL code into its constituent statements \(e.g., SELECT, CREATE TABLE\). It also provides functionality to extract these statements and simplify the code into commented descriptions.

Methods

`__init__`\(code\) |    ---|---   `extract_functions_classes`\(\) | Extract SQL statements from the code.   `get_chunk_query`\(\) | Return the Tree-sitter query for SQL segmentation.   `get_language`\(\) | Return the SQL language grammar for Tree-sitter.   `get_parser`\(\) |    `is_valid`\(\) |    `make_line_comment`\(text\) | Create a line comment in SQL style.   `simplify_code`\(\) | Simplify the extracted SQL code into comments.      Parameters:     

**code** \(_str_\)

\_\_init\_\_\(_code : str_\)\#     

Parameters:     

**code** \(_str_\)

extract\_functions\_classes\(\) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/sql.html#SQLSegmenter.extract_functions_classes)\#     

Extract SQL statements from the code. Ensures that all SQL statements end with a semicolon for consistency.

Return type:     

list\[str\]

get\_chunk\_query\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/sql.html#SQLSegmenter.get_chunk_query)\#     

Return the Tree-sitter query for SQL segmentation.

Return type:     

str

get\_language\(\) → [Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/sql.html#SQLSegmenter.get_language)\#     

Return the SQL language grammar for Tree-sitter.

Return type:     

[Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")

get\_parser\(\) → Parser\#     

Return type:     

Parser

is\_valid\(\) → bool\#     

Return type:     

bool

make\_line\_comment\(_text : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/sql.html#SQLSegmenter.make_line_comment)\#     

Create a line comment in SQL style.

Parameters:     

**text** \(_str_\)

Return type:     

str

simplify\_code\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/sql.html#SQLSegmenter.simplify_code)\#     

Simplify the extracted SQL code into comments. Converts SQL statements into commented descriptions for easy readability.

Return type:     

str

__On this page