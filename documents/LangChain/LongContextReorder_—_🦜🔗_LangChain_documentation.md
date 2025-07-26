# LongContextReorder — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.long_context_reorder.LongContextReorder.html
**Word Count:** 95
**Links Count:** 129
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# LongContextReorder\#

_class _langchain\_community.document\_transformers.long\_context\_reorder.LongContextReorder[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/long_context_reorder.html#LongContextReorder)\#     

Bases: [`BaseDocumentTransformer`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.transformers.BaseDocumentTransformer.html#langchain_core.documents.transformers.BaseDocumentTransformer "langchain_core.documents.transformers.BaseDocumentTransformer"), `BaseModel`

Reorder long context.

Lost in the middle: Performance degrades when models must access relevant information in the middle of long contexts. See: <https://arxiv.org/abs//2307.03172>

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/long_context_reorder.html#LongContextReorder.atransform_documents)\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/long_context_reorder.html#LongContextReorder.transform_documents)\#     

Reorders documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using LongContextReorder

  * [How to reorder retrieved results to mitigate the “lost in the middle” effect](https://python.langchain.com/docs/how_to/long_context_reorder/)

  * [LOTR \(Merger Retriever\)](https://python.langchain.com/docs/integrations/retrievers/merger_retriever/)

__On this page