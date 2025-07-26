# MarkdownHeaderTextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.MarkdownHeaderTextSplitter.html
**Word Count:** 105
**Links Count:** 103
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# MarkdownHeaderTextSplitter\#

_class _langchain\_text\_splitters.markdown.MarkdownHeaderTextSplitter\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\]_,     _return\_each\_line : bool = False_,     _strip\_headers : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/markdown.html#MarkdownHeaderTextSplitter)\#     

Splitting markdown files based on specified headers.

Create a new MarkdownHeaderTextSplitter.

Parameters:     

  * **headers\_to\_split\_on** \(_list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\) – Headers we want to track

  * **return\_each\_line** \(_bool_\) – Return each line w/ associated headers

  * **strip\_headers** \(_bool_\) – Strip split headers from the content of the chunk

Methods

`__init__`\(headers\_to\_split\_on\[, ...\]\) | Create a new MarkdownHeaderTextSplitter.   ---|---   `aggregate_lines_to_chunks`\(lines\) | Combine lines with common metadata into chunks.   `split_text`\(text\) | Split markdown file.      \_\_init\_\_\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\]_,     _return\_each\_line : bool = False_,     _strip\_headers : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/markdown.html#MarkdownHeaderTextSplitter.__init__)\#     

Create a new MarkdownHeaderTextSplitter.

Parameters:     

  * **headers\_to\_split\_on** \(_list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\) – Headers we want to track

  * **return\_each\_line** \(_bool_\) – Return each line w/ associated headers

  * **strip\_headers** \(_bool_\) – Strip split headers from the content of the chunk

aggregate\_lines\_to\_chunks\(

    _lines : list\[[LineType](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.LineType.html#langchain_text_splitters.markdown.LineType "langchain_text_splitters.markdown.LineType")\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/markdown.html#MarkdownHeaderTextSplitter.aggregate_lines_to_chunks)\#     

Combine lines with common metadata into chunks.

Parameters:     

**lines** \(_list_ _\[_[_LineType_](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.LineType.html#langchain_text_splitters.markdown.LineType "langchain_text_splitters.markdown.LineType") _\]_\) – Line of text / associated header metadata

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_text\(

    _text : str_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/markdown.html#MarkdownHeaderTextSplitter.split_text)\#     

Split markdown file.

Parameters:     

**text** \(_str_\) – Markdown file

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using MarkdownHeaderTextSplitter

  * [How to split Markdown by Headers](https://python.langchain.com/docs/how_to/markdown_header_metadata_splitter/)

__On this page