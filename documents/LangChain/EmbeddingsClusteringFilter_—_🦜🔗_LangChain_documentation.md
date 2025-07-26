# EmbeddingsClusteringFilter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.embeddings_redundant_filter.EmbeddingsClusteringFilter.html
**Word Count:** 214
**Links Count:** 139
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# EmbeddingsClusteringFilter\#

_class _langchain\_community.document\_transformers.embeddings\_redundant\_filter.EmbeddingsClusteringFilter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/embeddings_redundant_filter.html#EmbeddingsClusteringFilter)\#     

Bases: [`BaseDocumentTransformer`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.transformers.BaseDocumentTransformer.html#langchain_core.documents.transformers.BaseDocumentTransformer "langchain_core.documents.transformers.BaseDocumentTransformer"), `BaseModel`

Perform K-means clustering on document vectors. Returns an arbitrary number of documents closest to center.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _embeddings _: [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_ _\[Required\]_\#     

Embeddings to use for embedding document contents.

_param _num\_closest _: int_ _ = 1_\#     

The number of closest vectors to return for each cluster center.

_param _num\_clusters _: int_ _ = 5_\#     

Number of clusters. Groups of documents with similar meaning.

_param _random\_state _: int_ _ = 42_\#     

Controls the random number generator used to initialize the cluster centroids. If you set the random\_state parameter to None, the KMeans algorithm will use a random number generator that is seeded with the current time. This means that the results of the KMeans algorithm will be different each time you run it.

_param _remove\_duplicates _: bool_ _ = False_\#     

By default duplicated results are skipped and replaced by the next closest vector in the cluster. If remove\_duplicates is true no replacement will be done: This could dramatically reduce results when there is a lot of overlap between clusters.

_param _sorted _: bool_ _ = False_\#     

By default results are re-ordered “grouping” them by cluster, if sorted is true result will be ordered by the original position from the retriever

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

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/embeddings_redundant_filter.html#EmbeddingsClusteringFilter.transform_documents)\#     

Filter down documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using EmbeddingsClusteringFilter

  * [LOTR \(Merger Retriever\)](https://python.langchain.com/docs/integrations/retrievers/merger_retriever/)

__On this page