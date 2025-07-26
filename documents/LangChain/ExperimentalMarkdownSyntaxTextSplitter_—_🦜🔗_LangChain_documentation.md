# ExperimentalMarkdownSyntaxTextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.ExperimentalMarkdownSyntaxTextSplitter.html
**Word Count:** 403
**Links Count:** 96
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# ExperimentalMarkdownSyntaxTextSplitter\#

_class _langchain\_text\_splitters.markdown.ExperimentalMarkdownSyntaxTextSplitter\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\] | None = None_,     _return\_each\_line : bool = False_,     _strip\_headers : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/markdown.html#ExperimentalMarkdownSyntaxTextSplitter)\#     

An experimental text splitter for handling Markdown syntax.

This splitter aims to retain the exact whitespace of the original text while extracting structured metadata, such as headers. It is a re-implementation of the MarkdownHeaderTextSplitter with notable changes to the approach and additional features.

Key Features: \- Retains the original whitespace and formatting of the Markdown text. \- Extracts headers, code blocks, and horizontal rules as metadata. \- Splits out code blocks and includes the language in the “Code” metadata key. \- Splits text on horizontal rules \(—\) as well. \- Defaults to sensible splitting behavior, which can be overridden using the

> headers\_to\_split\_on parameter.

## Parameters:\#

headers\_to\_split\_onList\[Tuple\[str, str\]\], optional     

Headers to split on, defaulting to common Markdown headers if not specified.

return\_each\_linebool, optional     

When set to True, returns each line as a separate chunk. Default is False.

## Usage example:\#               >>> headers_to_split_on = [     >>>     ("#", "Header 1"),     >>>     ("##", "Header 2"),     >>> ]     >>> splitter = ExperimentalMarkdownSyntaxTextSplitter(     >>>     headers_to_split_on=headers_to_split_on     >>> )     >>> chunks = splitter.split(text)     >>> for chunk in chunks:     >>>     print(chunk)     

This class is currently experimental and subject to change based on feedback and further development.

Initialize the text splitter with header splitting and formatting options.

This constructor sets up the required configuration for splitting text into chunks based on specified headers and formatting preferences.

param headers\_to\_split\_on:     

A list of tuples, where each tuple contains a header tag \(e.g., “h1”\) and its corresponding metadata key. If None, default headers are used.

type headers\_to\_split\_on:     

Union\[List\[Tuple\[str, str\]\], None\]

param return\_each\_line:     

Whether to return each line as an individual chunk. Defaults to False, which aggregates lines into larger chunks.

type return\_each\_line:     

bool

param strip\_headers:     

Whether to exclude headers from the resulting chunks. Defaults to True.

type strip\_headers:     

bool

Attributes

`DEFAULT_HEADER_KEYS` |    ---|---      Methods

`__init__`\(\[headers\_to\_split\_on, ...\]\) | Initialize the text splitter with header splitting and formatting options.   ---|---   `split_text`\(text\) | Split the input text into structured chunks.      \_\_init\_\_\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\] | None = None_,     _return\_each\_line : bool = False_,     _strip\_headers : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/markdown.html#ExperimentalMarkdownSyntaxTextSplitter.__init__)\#     

Initialize the text splitter with header splitting and formatting options.

This constructor sets up the required configuration for splitting text into chunks based on specified headers and formatting preferences.

Parameters:     

  * **headers\_to\_split\_on** \(_Union_ _\[__List_ _\[__Tuple_ _\[__str_ _,__str_ _\]__\]__,__None_ _\]_\) – A list of tuples, where each tuple contains a header tag \(e.g., “h1”\) and its corresponding metadata key. If None, default headers are used.

  * **return\_each\_line** \(_bool_\) – Whether to return each line as an individual chunk. Defaults to False, which aggregates lines into larger chunks.

  * **strip\_headers** \(_bool_\) – Whether to exclude headers from the resulting chunks. Defaults to True.

split\_text\(

    _text : str_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/markdown.html#ExperimentalMarkdownSyntaxTextSplitter.split_text)\#     

Split the input text into structured chunks.

This method processes the input text line by line, identifying and handling specific patterns such as headers, code blocks, and horizontal rules to split it into structured chunks based on headers, code blocks, and horizontal rules.

Parameters:     

**text** \(_str_\) – The input text to be split into chunks.

Returns:     

A list of Document objects representing the structured chunks of the input text. If return\_each\_line is enabled, each line is returned as a separate Document.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Parameters:     

  * **headers\_to\_split\_on** \(_Union_ _\[__list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]__,__None_ _\]_\)

  * **return\_each\_line** \(_bool_\)

  * **strip\_headers** \(_bool_\)

__On this page