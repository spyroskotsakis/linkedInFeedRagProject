# Html2TextTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.html2text.Html2TextTransformer.html
**Word Count:** 90
**Links Count:** 134
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# Html2TextTransformer\#

_class _langchain\_community.document\_transformers.html2text.Html2TextTransformer\(

    _ignore\_links : bool = True_,     _ignore\_images : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/html2text.html#Html2TextTransformer)\#     

Replace occurrences of a particular search pattern with a replacement string

Parameters:     

  * **ignore\_links** \(_bool_\) – Whether links should be ignored; defaults to True.

  * **ignore\_images** \(_bool_\) – Whether images should be ignored; defaults to True.

Example

Methods

`__init__`\(\[ignore\_links, ignore\_images\]\) |    ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `transform_documents`\(documents, \*\*kwargs\) | Transform a list of documents.      \_\_init\_\_\(

    _ignore\_links : bool = True_,     _ignore\_images : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/html2text.html#Html2TextTransformer.__init__)\#     

Parameters:     

  * **ignore\_links** \(_bool_\)

  * **ignore\_images** \(_bool_\)

Return type:     

None

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/html2text.html#Html2TextTransformer.atransform_documents)\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/html2text.html#Html2TextTransformer.transform_documents)\#     

Transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using Html2TextTransformer

  * [Activeloop Deep Memory](https://python.langchain.com/docs/integrations/retrievers/activeloop/)

  * [Async Chromium](https://python.langchain.com/docs/integrations/document_loaders/async_chromium/)

  * [HTML to text](https://python.langchain.com/docs/integrations/document_transformers/html2text/)

__On this page