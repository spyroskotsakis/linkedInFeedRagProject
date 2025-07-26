# NucliaTextTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.nuclia_text_transform.NucliaTextTransformer.html
**Word Count:** 79
**Links Count:** 136
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# NucliaTextTransformer\#

_class _langchain\_community.document\_transformers.nuclia\_text\_transform.NucliaTextTransformer\(

    _nua : [NucliaUnderstandingAPI](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI.html#langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI "langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/nuclia_text_transform.html#NucliaTextTransformer)\#     

Nuclia Text Transformer.

The Nuclia Understanding API splits into paragraphs and sentences, identifies entities, provides a summary of the text and generates embeddings for all sentences.

Methods

`__init__`\(nua\) |    ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `transform_documents`\(documents, \*\*kwargs\) | Transform a list of documents.      Parameters:     

**nua** \([_NucliaUnderstandingAPI_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI.html#langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI "langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI")\)

\_\_init\_\_\(

    _nua : [NucliaUnderstandingAPI](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI.html#langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI "langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/nuclia_text_transform.html#NucliaTextTransformer.__init__)\#     

Parameters:     

**nua** \([_NucliaUnderstandingAPI_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI.html#langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI "langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI")\)

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/nuclia_text_transform.html#NucliaTextTransformer.atransform_documents)\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/nuclia_text_transform.html#NucliaTextTransformer.transform_documents)\#     

Transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using NucliaTextTransformer

  * [Nuclia](https://python.langchain.com/docs/integrations/document_transformers/nuclia_transformer/)

__On this page