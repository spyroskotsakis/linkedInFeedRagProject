# LinkExtractorTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer.html
**Word Count:** 101
**Links Count:** 144
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# LinkExtractorTransformer\#

_class _langchain\_community.graph\_vectorstores.extractors.link\_extractor\_transformer.LinkExtractorTransformer\(

    _link\_extractors : Sequence\[[LinkExtractor](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor")\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor_transformer.html#LinkExtractorTransformer)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

DocumentTransformer for applying one or more LinkExtractors.

Example               extract_links = LinkExtractorTransformer([         HtmlLinkExtractor().as_document_extractor(),     ])     extract_links.transform_documents(docs)     

Create a DocumentTransformer which adds extracted links to each document.

Methods

`__init__`\(link\_extractors\) | Create a DocumentTransformer which adds extracted links to each document.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `transform_documents`\(documents, \*\*kwargs\) | Transform a list of documents.      Parameters:     

**link\_extractors** \(_Sequence_ _\[_[_LinkExtractor_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor") _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__\]_\)

\_\_init\_\_\(

    _link\_extractors : Sequence\[[LinkExtractor](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor")\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor_transformer.html#LinkExtractorTransformer.__init__)\#     

Create a DocumentTransformer which adds extracted links to each document.

Parameters:     

**link\_extractors** \(_Sequence_ _\[_[_LinkExtractor_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor") _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__\]_\)

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

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor_transformer.html#LinkExtractorTransformer.transform_documents)\#     

Transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page