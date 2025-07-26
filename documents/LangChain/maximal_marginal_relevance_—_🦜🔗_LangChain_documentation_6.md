# maximal_marginal_relevance — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/redis/vectorstores/langchain_redis.vectorstores.maximal_marginal_relevance.html
**Word Count:** 94
**Links Count:** 74
**Scraped:** 2025-07-21 08:27:44
**Status:** completed

---

# maximal\_marginal\_relevance\#

langchain\_redis.vectorstores.maximal\_marginal\_relevance\(

    _query\_embedding : ndarray_,     _embedding\_list : List\[ndarray\]_,     _lambda\_mult : float = 0.5_,     _k : int = 4_, \) → List\[int\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#maximal_marginal_relevance)\#     

Calculate maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to the query AND diversity among selected documents.

Parameters:     

  * **query\_embedding** \(_ndarray_\) – Embedding of the query text.

  * **embedding\_list** \(_List_ _\[__ndarray_ _\]_\) – List of embeddings to select from.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results, where 0 corresponds to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **k** \(_int_\) – Number of results to return. Defaults to 4.

Returns:     

List of indices of selected embeddings.

Return type:     

_List_\[int\]

Example               from langchain_redis import RedisVectorStore     from langchain_openai import OpenAIEmbeddings     import numpy as np          embeddings = OpenAIEmbeddings()     vector_store = RedisVectorStore(         index_name="langchain-demo",         embedding=embeddings,         redis_url="redis://localhost:6379",     )          query = "What is the capital of France?"     query_embedding = embeddings.embed_query(query)          # Assuming you have a list of document embeddings     doc_embeddings = [embeddings.embed_query(doc) for doc in documents]          selected_indices = vector_store.maximal_marginal_relevance(         query_embedding=np.array(query_embedding),         embedding_list=[np.array(emb) for emb in doc_embeddings],         lambda_mult=0.5,         k=2     )          for idx in selected_indices:         print(f"Selected document: {documents[idx]}")     

__On this page