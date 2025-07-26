# HTMLHeaderTextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/html/langchain_text_splitters.html.HTMLHeaderTextSplitter.html
**Word Count:** 510
**Links Count:** 107
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# HTMLHeaderTextSplitter\#

_class _langchain\_text\_splitters.html.HTMLHeaderTextSplitter\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\]_,     _return\_each\_element : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLHeaderTextSplitter)\#     

Split HTML content into structured Documents based on specified headers.

Splits HTML content by detecting specified header tags \(e.g., <h1>, <h2>\) and creating hierarchical Document objects that reflect the semantic structure of the original content. For each identified section, the splitter associates the extracted text with metadata corresponding to the encountered headers.

If no specified headers are found, the entire content is returned as a single Document. This allows for flexible handling of HTML input, ensuring that information is organized according to its semantic headers.

The splitter provides the option to return each HTML element as a separate Document or aggregate them into semantically meaningful chunks. It also gracefully handles multiple levels of nested headers, creating a rich, hierarchical representation of the content.

Parameters:     

  * **headers\_to\_split\_on** \(_List_ _\[__Tuple_ _\[__str_ _,__str_ _\]__\]_\) – A list of \(header\_tag, header\_name\) pairs representing the headers that define splitting boundaries. For example, \[\(“h1”, “Header 1”\), \(“h2”, “Header 2”\)\] will split content by <h1> and <h2> tags, assigning their textual content to the Document metadata.

  * **return\_each\_element** \(_bool_\) – If True, every HTML element encountered \(including headers, paragraphs, etc.\) is returned as a separate Document. If False, content under the same header hierarchy is aggregated into fewer Documents.

Returns:     

A list of Document objects. Each Document contains page\_content holding the extracted text and metadata that maps the header hierarchy to their corresponding titles.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Example               from langchain_text_splitters.html_header_text_splitter import (         HTMLHeaderTextSplitter,     )          # Define headers for splitting on h1 and h2 tags.     headers_to_split_on = [("h1", "Main Topic"), ("h2", "Sub Topic")]          splitter = HTMLHeaderTextSplitter(         headers_to_split_on=headers_to_split_on,         return_each_element=False     )          html_content = """     <html>       <body>         <h1>Introduction</h1>         <p>Welcome to the introduction section.</p>         <h2>Background</h2>         <p>Some background details here.</p>         <h1>Conclusion</h1>         <p>Final thoughts.</p>       </body>     </html>     """          documents = splitter.split_text(html_content)          # 'documents' now contains Document objects reflecting the hierarchy:     # - Document with metadata={"Main Topic": "Introduction"} and     #   content="Introduction"     # - Document with metadata={"Main Topic": "Introduction"} and     #   content="Welcome to the introduction section."     # - Document with metadata={"Main Topic": "Introduction",     #   "Sub Topic": "Background"} and content="Background"     # - Document with metadata={"Main Topic": "Introduction",     #   "Sub Topic": "Background"} and content="Some background details here."     # - Document with metadata={"Main Topic": "Conclusion"} and     #   content="Conclusion"     # - Document with metadata={"Main Topic": "Conclusion"} and     #   content="Final thoughts."     

Initialize with headers to split on.

Parameters:     

  * **headers\_to\_split\_on** \(_list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\) – A list of tuples where each tuple contains a header tag and its corresponding value.

  * **return\_each\_element** \(_bool_\) – Whether to return each HTML element as a separate Document. Defaults to False.

Methods

`__init__`\(headers\_to\_split\_on\[, ...\]\) | Initialize with headers to split on.   ---|---   `split_text`\(text\) | Split the given text into a list of Document objects.   `split_text_from_file`\(file\) | Split HTML content from a file into a list of Document objects.   `split_text_from_url`\(url\[, timeout\]\) | Fetch text content from a URL and split it into documents.      \_\_init\_\_\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\]_,     _return\_each\_element : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLHeaderTextSplitter.__init__)\#     

Initialize with headers to split on.

Parameters:     

  * **headers\_to\_split\_on** \(_list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\) – A list of tuples where each tuple contains a header tag and its corresponding value.

  * **return\_each\_element** \(_bool_\) – Whether to return each HTML element as a separate Document. Defaults to False.

Return type:     

None

split\_text\(

    _text : str_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLHeaderTextSplitter.split_text)\#     

Split the given text into a list of Document objects.

Parameters:     

**text** \(_str_\) – The HTML text to split.

Returns:     

A list of split Document objects.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_text\_from\_file\(

    _file : Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLHeaderTextSplitter.split_text_from_file)\#     

Split HTML content from a file into a list of Document objects.

Parameters:     

**file** \(_Any_\) – A file path or a file-like object containing HTML content.

Returns:     

A list of split Document objects.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_text\_from\_url\(

    _url : str_,     _timeout : int = 10_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLHeaderTextSplitter.split_text_from_url)\#     

Fetch text content from a URL and split it into documents.

Parameters:     

  * **url** \(_str_\) – The URL to fetch content from.

  * **timeout** \(_int_\) – Timeout for the request. Defaults to 10.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments for the request.

Returns:     

A list of split Document objects.

Raises:     

**requests.RequestException** – If the HTTP request fails.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using HTMLHeaderTextSplitter

  * [How to split by HTML header ](https://python.langchain.com/docs/how_to/HTML_header_metadata_splitter/)

__On this page