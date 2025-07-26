# langchain-qdrant: 0.2.0 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/qdrant/index.html
**Word Count:** 49
**Links Count:** 83
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# langchain-qdrant: 0.2.0\#

## [fastembed\_sparse](https://python.langchain.com/api_reference/qdrant/fastembed_sparse.html#langchain-qdrant-fastembed-sparse)\#

**Classes**

[`fastembed_sparse.FastEmbedSparse`](https://python.langchain.com/api_reference/qdrant/fastembed_sparse/langchain_qdrant.fastembed_sparse.FastEmbedSparse.html#langchain_qdrant.fastembed_sparse.FastEmbedSparse "langchain_qdrant.fastembed_sparse.FastEmbedSparse")\(\[...\]\) | An interface for sparse embedding models to use with Qdrant.   ---|---      ## [qdrant](https://python.langchain.com/api_reference/qdrant/qdrant.html#langchain-qdrant-qdrant)\#

**Classes**

[`qdrant.QdrantVectorStore`](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.QdrantVectorStore.html#langchain_qdrant.qdrant.QdrantVectorStore "langchain_qdrant.qdrant.QdrantVectorStore")\(client, collection\_name\) | Qdrant vector store integration.   ---|---   [`qdrant.QdrantVectorStoreError`](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.QdrantVectorStoreError.html#langchain_qdrant.qdrant.QdrantVectorStoreError "langchain_qdrant.qdrant.QdrantVectorStoreError") | QdrantVectorStore related exceptions.   [`qdrant.RetrievalMode`](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode")\(value\) |       ## [sparse\_embeddings](https://python.langchain.com/api_reference/qdrant/sparse_embeddings.html#langchain-qdrant-sparse-embeddings)\#

**Classes**

[`sparse_embeddings.SparseEmbeddings`](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings")\(\) | An interface for sparse embedding models to use with Qdrant.   ---|---   [`sparse_embeddings.SparseVector`](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html#langchain_qdrant.sparse_embeddings.SparseVector "langchain_qdrant.sparse_embeddings.SparseVector") | Sparse vector structure      ## [vectorstores](https://python.langchain.com/api_reference/qdrant/vectorstores.html#langchain-qdrant-vectorstores)\#

**Classes**

[`vectorstores.QdrantException`](https://python.langchain.com/api_reference/qdrant/vectorstores/langchain_qdrant.vectorstores.QdrantException.html#langchain_qdrant.vectorstores.QdrantException "langchain_qdrant.vectorstores.QdrantException") | Qdrant related exceptions.   ---|---      **Functions**

[`vectorstores.sync_call_fallback`](https://python.langchain.com/api_reference/qdrant/vectorstores/langchain_qdrant.vectorstores.sync_call_fallback.html#langchain_qdrant.vectorstores.sync_call_fallback "langchain_qdrant.vectorstores.sync_call_fallback")\(method\) | Decorator to call the synchronous method of the class if the async method is not implemented.   ---|---      **Deprecated classes**

[`vectorstores.Qdrant`](https://python.langchain.com/api_reference/qdrant/vectorstores/langchain_qdrant.vectorstores.Qdrant.html#langchain_qdrant.vectorstores.Qdrant "langchain_qdrant.vectorstores.Qdrant")\(client, collection\_name\) |    ---|---