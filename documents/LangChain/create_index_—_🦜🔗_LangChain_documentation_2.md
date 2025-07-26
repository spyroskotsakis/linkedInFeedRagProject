# create_index — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.pinecone_hybrid_search.create_index.html
**Word Count:** 64
**Links Count:** 174
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# create\_index\#

langchain\_community.retrievers.pinecone\_hybrid\_search.create\_index\(

    _contexts : List\[str\]_,     _index : Any_,     _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _sparse\_encoder : Any_,     _ids : List\[str\] | None = None_,     _metadatas : List\[dict\] | None = None_,     _namespace : str | None = None_,     _text\_key : str = 'context'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/pinecone_hybrid_search.html#create_index)\#     

Create an index from a list of contexts.

It modifies the index argument in-place\!

Parameters:     

  * **contexts** \(_List_ _\[__str_ _\]_\) – List of contexts to embed.

  * **index** \(_Any_\) – Index to use.

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embeddings model to use.

  * **sparse\_encoder** \(_Any_\) – Sparse encoder to use.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to use for the documents.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – List of metadata to use for the documents.

  * **namespace** \(_str_ _|__None_\) – Namespace value for index partition.

  * **text\_key** \(_str_\)

Return type:     

None

__On this page