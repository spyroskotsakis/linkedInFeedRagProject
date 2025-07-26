# BaseDocumentTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/documents/langchain_core.documents.transformers.BaseDocumentTransformer.html
**Word Count:** 72
**Links Count:** 119
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# BaseDocumentTransformer\#

_class _langchain\_core.documents.transformers.BaseDocumentTransformer[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/transformers.html#BaseDocumentTransformer)\#     

Abstract base class for document transformation.

A document transformation takes a sequence of Documents and returns a sequence of transformed Documents.

Example               class EmbeddingsRedundantFilter(BaseDocumentTransformer, BaseModel):         embeddings: Embeddings         similarity_fn: Callable = cosine_similarity         similarity_threshold: float = 0.95              class Config:             arbitrary_types_allowed = True              def transform_documents(             self, documents: Sequence[Document], **kwargs: Any         ) -> Sequence[Document]:             stateful_documents = get_stateful_documents(documents)             embedded_documents = _get_embeddings_from_stateful_docs(                 self.embeddings, stateful_documents             )             included_idxs = _filter_similar_embeddings(                 embedded_documents, self.similarity_fn, self.similarity_threshold             )             return [stateful_documents[i] for i in sorted(included_idxs)]              async def atransform_documents(             self, documents: Sequence[Document], **kwargs: Any         ) -> Sequence[Document]:             raise NotImplementedError     

Methods

`atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   ---|---   `transform_documents`\(documents, \*\*kwargs\) | Transform a list of documents.      _async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/transformers.html#BaseDocumentTransformer.atransform_documents)\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_abstractmethod _transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/transformers.html#BaseDocumentTransformer.transform_documents)\#     

Transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page