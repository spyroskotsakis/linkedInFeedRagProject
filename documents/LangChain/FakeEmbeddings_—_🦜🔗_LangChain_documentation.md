# FakeEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.fake.FakeEmbeddings.html
**Word Count:** 93
**Links Count:** 228
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# FakeEmbeddings\#

_class _langchain\_community.embeddings.fake.FakeEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/fake.html#FakeEmbeddings)\#     

Bases: [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings"), `BaseModel`

Fake embedding model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _size _: int_ _\[Required\]_\#     

The size of the embedding vector.

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(_text : str_\) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/fake.html#FakeEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(_text : str_\) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/fake.html#FakeEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

Examples using FakeEmbeddings

  * [Baidu VectorDB](https://python.langchain.com/docs/integrations/vectorstores/baiduvectordb/)

  * [DocArray](https://python.langchain.com/docs/integrations/retrievers/docarray_retriever/)

  * [Fake Embeddings](https://python.langchain.com/docs/integrations/text_embedding/fake/)

  * [Google Memorystore for Redis](https://python.langchain.com/docs/integrations/vectorstores/google_memorystore_redis/)

  * [PGVecto.rs](https://python.langchain.com/docs/integrations/vectorstores/pgvecto_rs/)

  * [Relyt](https://python.langchain.com/docs/integrations/vectorstores/relyt/)

  * [Tair](https://python.langchain.com/docs/integrations/vectorstores/tair/)

  * [Tencent Cloud VectorDB](https://python.langchain.com/docs/integrations/vectorstores/tencentvectordb/)

__On this page