# HTMLSectionSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/html/langchain_text_splitters.html.HTMLSectionSplitter.html
**Word Count:** 341
**Links Count:** 122
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# HTMLSectionSplitter\#

_class _langchain\_text\_splitters.html.HTMLSectionSplitter\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\]_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSectionSplitter)\#     

Splitting HTML files based on specified tag and font sizes.

Requires lxml package.

Create a new HTMLSectionSplitter.

Parameters:     

  * **headers\_to\_split\_on** \(_list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\) – list of tuples of headers we want to track mapped to \(arbitrary\) keys for metadata. Allowed header values: h1, h2, h3, h4, h5, h6 e.g. \[\(“h1”, “Header 1”\), \(“h2”, “Header 2”\].

  * **\*\*kwargs** \(_Any_\) – Additional optional arguments for customizations.

Methods

`__init__`\(headers\_to\_split\_on, \*\*kwargs\) | Create a new HTMLSectionSplitter.   ---|---   `convert_possible_tags_to_header`\(html\_content\) | Convert specific HTML tags to headers using an XSLT transformation.   `create_documents`\(texts\[, metadatas\]\) | Create documents from a list of texts.   `split_documents`\(documents\) | Split documents.   `split_html_by_headers`\(html\_doc\) | Split an HTML document into sections based on specified header tags.   `split_text`\(text\) | Split HTML text string.   `split_text_from_file`\(file\) | Split HTML content from a file into a list of Document objects.      \_\_init\_\_\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSectionSplitter.__init__)\#     

Create a new HTMLSectionSplitter.

Parameters:     

  * **headers\_to\_split\_on** \(_list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\) – list of tuples of headers we want to track mapped to \(arbitrary\) keys for metadata. Allowed header values: h1, h2, h3, h4, h5, h6 e.g. \[\(“h1”, “Header 1”\), \(“h2”, “Header 2”\].

  * **\*\*kwargs** \(_Any_\) – Additional optional arguments for customizations.

Return type:     

None

convert\_possible\_tags\_to\_header\(

    _html\_content : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSectionSplitter.convert_possible_tags_to_header)\#     

Convert specific HTML tags to headers using an XSLT transformation.

This method uses an XSLT file to transform the HTML content, converting certain tags into headers for easier parsing. If no XSLT path is provided, the HTML content is returned unchanged.

Parameters:     

**html\_content** \(_str_\) – The HTML content to be transformed.

Returns:     

The transformed HTML content as a string.

Return type:     

str

create\_documents\(

    _texts : list\[str\]_,     _metadatas : list\[dict\[Any, Any\]\] | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSectionSplitter.create_documents)\#     

Create documents from a list of texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\[__Any_ _,__Any_ _\]__\]__|__None_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_documents\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSectionSplitter.split_documents)\#     

Split documents.

Parameters:     

**documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_html\_by\_headers\(

    _html\_doc : str_, \) → list\[dict\[str, str | None\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSectionSplitter.split_html_by_headers)\#     

Split an HTML document into sections based on specified header tags.

This method uses BeautifulSoup to parse the HTML content and divides it into sections based on headers defined in headers\_to\_split\_on. Each section contains the header text, content under the header, and the tag name.

Parameters:     

**html\_doc** \(_str_\) – The HTML document to be split into sections.

Returns:     

A list of dictionaries representing sections.

> Each dictionary contains: \- ‘header’: The header text or a default title for the first section. \- ‘content’: The content under the header. \- ‘tag\_name’: The name of the header tag \(e.g., “h1”, “h2”\).

Return type:     

List\[Dict\[str, Optional\[str\]\]\]

split\_text\(

    _text : str_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSectionSplitter.split_text)\#     

Split HTML text string.

Parameters:     

**text** \(_str_\) – HTML text

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_text\_from\_file\(

    _file : Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSectionSplitter.split_text_from_file)\#     

Split HTML content from a file into a list of Document objects.

Parameters:     

**file** \(_Any_\) – A file path or a file-like object containing HTML content.

Returns:     

A list of split Document objects.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using HTMLSectionSplitter

  * [How to split by HTML sections](https://python.langchain.com/docs/how_to/HTML_section_aware_splitter/)

__On this page