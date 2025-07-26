# HTMLSemanticPreservingSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/html/langchain_text_splitters.html.HTMLSemanticPreservingSplitter.html
**Word Count:** 353
**Links Count:** 108
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# HTMLSemanticPreservingSplitter\#

_class _langchain\_text\_splitters.html.HTMLSemanticPreservingSplitter\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\]_,     _\*_ ,     _max\_chunk\_size : int = 1000_,     _chunk\_overlap : int = 0_,     _separators : list\[str\] | None = None_,     _elements\_to\_preserve : list\[str\] | None = None_,     _preserve\_links : bool = False_,     _preserve\_images : bool = False_,     _preserve\_videos : bool = False_,     _preserve\_audio : bool = False_,     _custom\_handlers : dict\[str, Callable\[\[Any\], str\]\] | None = None_,     _stopword\_removal : bool = False_,     _stopword\_lang : str = 'english'_,     _normalize\_text : bool = False_,     _external\_metadata : dict\[str, str\] | None = None_,     _allowlist\_tags : list\[str\] | None = None_,     _denylist\_tags : list\[str\] | None = None_,     _preserve\_parent\_metadata : bool = False_,     _keep\_separator : bool | Literal\['start', 'end'\] = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSemanticPreservingSplitter)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Split HTML content preserving semantic structure.

Splits HTML content by headers into generalized chunks, preserving semantic structure. If chunks exceed the maximum chunk size, it uses RecursiveCharacterTextSplitter for further splitting.

The splitter preserves full HTML elements \(e.g., <table>, <ul>\) and converts links to Markdown-like links. It can also preserve images, videos, and audio elements by converting them into Markdown format. Note that some chunks may exceed the maximum size to maintain semantic integrity.

Parameters:     

  * **headers\_to\_split\_on** \(_List_ _\[__Tuple_ _\[__str_ _,__str_ _\]__\]_\) – HTML headers \(e.g., “h1”, “h2”\) that define content sections.

  * **max\_chunk\_size** \(_int_\) – Maximum size for each chunk, with allowance for exceeding this limit to preserve semantics.

  * **chunk\_overlap** \(_int_\) – Number of characters to overlap between chunks to ensure contextual continuity.

  * **separators** \(_List_ _\[__str_ _\]_\) – Delimiters used by RecursiveCharacterTextSplitter for further splitting.

  * **elements\_to\_preserve** \(_List_ _\[__str_ _\]_\) – HTML tags \(e.g., <table>, <ul>\) to remain intact during splitting.

  * **preserve\_links** \(_bool_\) – Converts <a> tags to Markdown links \(\[text\]\(url\)\).

  * **preserve\_images** \(_bool_\) – Converts <img> tags to Markdown images \(\!\[alt\]\(src\)\).

  * **preserve\_videos** \(_bool_\) – Converts <video> tags to Markdown

  * **links** \(_audio_\)

  * **preserve\_audio** \(_bool_\) – Converts <audio> tags to Markdown

  * **links**

  * **custom\_handlers** \(_Dict_ _\[__str_ _,__Callable_ _\[__\[__Any_ _\]__,__str_ _\]__\]_\) – Optional custom handlers for specific HTML tags, allowing tailored extraction or processing.

  * **stopword\_removal** \(_bool_\) – Optionally remove stopwords from the text.

  * **stopword\_lang** \(_str_\) – The language of stopwords to remove.

  * **normalize\_text** \(_bool_\) – Optionally normalize text \(e.g., lowercasing, removing punctuation\).

  * **external\_metadata** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Additional metadata to attach to the Document objects.

  * **allowlist\_tags** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Only these tags will be retained in the HTML.

  * **denylist\_tags** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – These tags will be removed from the HTML.

  * **preserve\_parent\_metadata** \(_bool_\) – Whether to pass through parent document metadata to split documents when calling `transform_documents/atransform_documents()`.

  * **keep\_separator** \(_Union_ _\[__bool_ _,__Literal_ _\[__"start"__,__"end"__\]__\]_\) – Whether separators should be at the beginning of a chunk, at the end, or not at all.

Example               from langchain_text_splitters.html import HTMLSemanticPreservingSplitter          def custom_iframe_extractor(iframe_tag):         ```         Custom handler function to extract the 'src' attribute from an <iframe> tag.         Converts the iframe to a Markdown-like link: [iframe:<src>](src).              Args:             iframe_tag (bs4.element.Tag): The <iframe> tag to be processed.              Returns:             str: A formatted string representing the iframe in Markdown-like format.         ```         iframe_src = iframe_tag.get('src', '')         return f"[iframe:{iframe_src}]({iframe_src})"          text_splitter = HTMLSemanticPreservingSplitter(         headers_to_split_on=[("h1", "Header 1"), ("h2", "Header 2")],         max_chunk_size=500,         preserve_links=True,         preserve_images=True,         custom_handlers={"iframe": custom_iframe_extractor}     )     

Initialize splitter.

Methods

`__init__`\(headers\_to\_split\_on, \*\[, ...\]\) | Initialize splitter.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `split_text`\(text\) | Splits the provided HTML text into smaller chunks based on the configuration.   `transform_documents`\(documents, \*\*kwargs\) | Transform sequence of documents by splitting them.      \_\_init\_\_\(

    _headers\_to\_split\_on : list\[tuple\[str, str\]\]_,     _\*_ ,     _max\_chunk\_size : int = 1000_,     _chunk\_overlap : int = 0_,     _separators : list\[str\] | None = None_,     _elements\_to\_preserve : list\[str\] | None = None_,     _preserve\_links : bool = False_,     _preserve\_images : bool = False_,     _preserve\_videos : bool = False_,     _preserve\_audio : bool = False_,     _custom\_handlers : dict\[str, Callable\[\[Any\], str\]\] | None = None_,     _stopword\_removal : bool = False_,     _stopword\_lang : str = 'english'_,     _normalize\_text : bool = False_,     _external\_metadata : dict\[str, str\] | None = None_,     _allowlist\_tags : list\[str\] | None = None_,     _denylist\_tags : list\[str\] | None = None_,     _preserve\_parent\_metadata : bool = False_,     _keep\_separator : bool | Literal\['start', 'end'\] = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSemanticPreservingSplitter.__init__)\#     

Initialize splitter.

Parameters:     

  * **headers\_to\_split\_on** \(_list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\)

  * **max\_chunk\_size** \(_int_\)

  * **chunk\_overlap** \(_int_\)

  * **separators** \(_list_ _\[__str_ _\]__|__None_\)

  * **elements\_to\_preserve** \(_list_ _\[__str_ _\]__|__None_\)

  * **preserve\_links** \(_bool_\)

  * **preserve\_images** \(_bool_\)

  * **preserve\_videos** \(_bool_\)

  * **preserve\_audio** \(_bool_\)

  * **custom\_handlers** \(_dict_ _\[__str_ _,__Callable_ _\[__\[__Any_ _\]__,__str_ _\]__\]__|__None_\)

  * **stopword\_removal** \(_bool_\)

  * **stopword\_lang** \(_str_\)

  * **normalize\_text** \(_bool_\)

  * **external\_metadata** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\)

  * **allowlist\_tags** \(_list_ _\[__str_ _\]__|__None_\)

  * **denylist\_tags** \(_list_ _\[__str_ _\]__|__None_\)

  * **preserve\_parent\_metadata** \(_bool_\)

  * **keep\_separator** \(_bool_ _|__Literal_ _\[__'start'__,__'end'__\]_\)

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_text\(

    _text : str_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSemanticPreservingSplitter.split_text)\#     

Splits the provided HTML text into smaller chunks based on the configuration.

Parameters:     

**text** \(_str_\) – The HTML content to be split.

Returns:     

A list of Document objects containing the split content.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/html.html#HTMLSemanticPreservingSplitter.transform_documents)\#     

Transform sequence of documents by splitting them.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)