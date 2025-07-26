# DeterministicFakeEmbedding — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.fake.DeterministicFakeEmbedding.html
**Word Count:** 144
**Links Count:** 115
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# DeterministicFakeEmbedding\#

_class _langchain\_core.embeddings.fake.DeterministicFakeEmbedding[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/embeddings/fake.html#DeterministicFakeEmbedding)\#     

Bases: [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings"), `BaseModel`

Deterministic fake embedding model for unit testing purposes.

This embedding model creates embeddings by sampling from a normal distribution with a seed based on the hash of the text.

Do not use this outside of testing, as it is not a real embedding model.

Instantiate:                    from langchain_core.embeddings import DeterministicFakeEmbedding     embed = DeterministicFakeEmbedding(size=100)     

Embed single text:                    input_text = "The meaning of life is 42"     vector = embed.embed_query(input_text)     print(vector[:3])                    [-0.700234640213188, -0.581266257710429, -1.1328482266445354]     

Embed multiple texts:                    input_texts = ["Document 1...", "Document 2..."]     vectors = embed.embed_documents(input_texts)     print(len(vectors))     # The first 3 coordinates for the first vector     print(vectors[0][:3])                    2     [-0.5670477847544458, -0.31403828652395727, -0.5840547508955257]     

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

_async _aembed\_query\(

    _text : str_, \) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/embeddings/fake.html#DeterministicFakeEmbedding.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

embed\_query\(

    _text : str_, \) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/embeddings/fake.html#DeterministicFakeEmbedding.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

Examples using DeterministicFakeEmbedding

  * [ElasticsearchRetriever](https://python.langchain.com/docs/integrations/retrievers/elasticsearch_retriever/)

__On this page