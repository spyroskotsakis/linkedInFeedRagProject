# MarkdownifyTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.markdownify.MarkdownifyTransformer.html
**Word Count:** 176
**Links Count:** 132
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# MarkdownifyTransformer\#

_class _langchain\_community.document\_transformers.markdownify.MarkdownifyTransformer\(

    _strip : str | List\[str\] | None = None_,     _convert : str | List\[str\] | None = None_,     _autolinks : bool = True_,     _heading\_style : str = 'ATX'_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/markdownify.html#MarkdownifyTransformer)\#     

Converts HTML documents to Markdown format with customizable options for handling links, images, other tags and heading styles using the markdownify library.

Parameters:     

  * **strip** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – A list of tags to strip. This option can’t be used with the convert option.

  * **convert** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – A list of tags to convert. This option can’t be used with the strip option.

  * **autolinks** \(_bool_\) – A boolean indicating whether the “automatic link” style should be used when a a tag’s contents match its href. Defaults to True.

  * **heading\_style** \(_str_\) – Defines how headings should be converted. Accepted values are ATX, ATX\_CLOSED, SETEXT, and UNDERLINED \(which is an alias for SETEXT\). Defaults to ATX.

  * **kwargs** \(_Any_\) – Additional options to pass to markdownify.

Example

More configuration options can be found at the markdownify GitHub page: [matthewwithanm/python-markdownify](https://github.com/matthewwithanm/python-markdownify)

Methods

`__init__`\(\[strip, convert, autolinks, ...\]\) |    ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `transform_documents`\(documents, \*\*kwargs\) | Transform a list of documents.      \_\_init\_\_\(

    _strip : str | List\[str\] | None = None_,     _convert : str | List\[str\] | None = None_,     _autolinks : bool = True_,     _heading\_style : str = 'ATX'_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/markdownify.html#MarkdownifyTransformer.__init__)\#     

Parameters:     

  * **strip** \(_str_ _|__List_ _\[__str_ _\]__|__None_\)

  * **convert** \(_str_ _|__List_ _\[__str_ _\]__|__None_\)

  * **autolinks** \(_bool_\)

  * **heading\_style** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

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

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/markdownify.html#MarkdownifyTransformer.transform_documents)\#     

Transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using MarkdownifyTransformer

  * [Markdownify](https://python.langchain.com/docs/integrations/document_transformers/markdownify/)

__On this page