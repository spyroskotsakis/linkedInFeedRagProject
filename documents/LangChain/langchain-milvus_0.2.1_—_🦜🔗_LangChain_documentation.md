# langchain-milvus: 0.2.1 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/milvus/index.html
**Word Count:** 55
**Links Count:** 84
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# langchain-milvus: 0.2.1\#

## [function](https://python.langchain.com/api_reference/milvus/function.html#langchain-milvus-function)\#

**Classes**

[`function.BM25BuiltInFunction`](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BM25BuiltInFunction.html#langchain_milvus.function.BM25BuiltInFunction "langchain_milvus.function.BM25BuiltInFunction")\(\*\[, ...\]\) | Milvus BM25 built-in function.   ---|---   [`function.BaseMilvusBuiltInFunction`](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction")\(\) | Base class for Milvus built-in functions.      ## [retrievers](https://python.langchain.com/api_reference/milvus/retrievers.html#langchain-milvus-retrievers)\#

**Classes**

[`retrievers.milvus_hybrid_search.MilvusCollectionHybridSearchRetriever`](https://python.langchain.com/api_reference/milvus/retrievers/langchain_milvus.retrievers.milvus_hybrid_search.MilvusCollectionHybridSearchRetriever.html#langchain_milvus.retrievers.milvus_hybrid_search.MilvusCollectionHybridSearchRetriever "langchain_milvus.retrievers.milvus_hybrid_search.MilvusCollectionHybridSearchRetriever") | Hybrid search retriever that uses Milvus Collection to retrieve documents based on multiple fields.   ---|---   [`retrievers.zilliz_cloud_pipeline_retriever.ZillizCloudPipelineRetriever`](https://python.langchain.com/api_reference/milvus/retrievers/langchain_milvus.retrievers.zilliz_cloud_pipeline_retriever.ZillizCloudPipelineRetriever.html#langchain_milvus.retrievers.zilliz_cloud_pipeline_retriever.ZillizCloudPipelineRetriever "langchain_milvus.retrievers.zilliz_cloud_pipeline_retriever.ZillizCloudPipelineRetriever") | Zilliz Cloud Pipeline retriever.      ## [utils](https://python.langchain.com/api_reference/milvus/utils.html#langchain-milvus-utils)\#

**Classes**

[`utils.sparse.BM25SparseEmbedding`](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BM25SparseEmbedding.html#langchain_milvus.utils.sparse.BM25SparseEmbedding "langchain_milvus.utils.sparse.BM25SparseEmbedding")\(corpus\[, ...\]\) | Sparse embedding model based on BM25.   ---|---   [`utils.sparse.BaseSparseEmbedding`](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding")\(\) | Interface for Sparse embedding models.      ## [vectorstores](https://python.langchain.com/api_reference/milvus/vectorstores.html#langchain-milvus-vectorstores)\#

**Classes**

[`vectorstores.milvus.Milvus`](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.Milvus.html#langchain_milvus.vectorstores.milvus.Milvus "langchain_milvus.vectorstores.milvus.Milvus")\(embedding\_function\) | Milvus vector store integration.   ---|---   [`vectorstores.zilliz.Zilliz`](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.zilliz.Zilliz.html#langchain_milvus.vectorstores.zilliz.Zilliz "langchain_milvus.vectorstores.zilliz.Zilliz")\(\*args, \*\*kwargs\) | Zilliz vector store.      **Functions**

[`vectorstores.milvus.cosine_similarity`](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.cosine_similarity.html#langchain_milvus.vectorstores.milvus.cosine_similarity "langchain_milvus.vectorstores.milvus.cosine_similarity")\(X, Y\) | Row-wise cosine similarity between two equal-width matrices.   ---|---   [`vectorstores.milvus.maximal_marginal_relevance`](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.maximal_marginal_relevance.html#langchain_milvus.vectorstores.milvus.maximal_marginal_relevance "langchain_milvus.vectorstores.milvus.maximal_marginal_relevance")\(...\) | Calculate maximal marginal relevance.