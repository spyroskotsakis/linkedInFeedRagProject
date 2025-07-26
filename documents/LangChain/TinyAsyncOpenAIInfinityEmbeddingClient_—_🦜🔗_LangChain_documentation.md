# TinyAsyncOpenAIInfinityEmbeddingClient — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.infinity.TinyAsyncOpenAIInfinityEmbeddingClient.html
**Word Count:** 79
**Links Count:** 219
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# TinyAsyncOpenAIInfinityEmbeddingClient\#

_class _langchain\_community.embeddings.infinity.TinyAsyncOpenAIInfinityEmbeddingClient\(

    _host : str = 'http://localhost:7797/v1'_,     _aiosession : ClientSession | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity.html#TinyAsyncOpenAIInfinityEmbeddingClient)\#     

Helper tool to embed Infinity.

It is not a part of Langchain’s stable API, direct use discouraged.

Example               mini_client = TinyAsyncInfinityEmbeddingClient(     )     embeds = mini_client.embed(         model="BAAI/bge-small",         text=["doc1", "doc2"]     )     # or     embeds = await mini_client.aembed(         model="BAAI/bge-small",         text=["doc1", "doc2"]     )     

Methods

`__init__`\(\[host, aiosession\]\) |    ---|---   `aembed`\(model, texts\) | call the embedding of model, async method   `embed`\(model, texts\) | call the embedding of model      Parameters:     

  * **host** \(_str_\)

  * **aiosession** \(_ClientSession_ _|__None_\)

\_\_init\_\_\(

    _host : str = 'http://localhost:7797/v1'_,     _aiosession : ClientSession | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity.html#TinyAsyncOpenAIInfinityEmbeddingClient.__init__)\#     

Parameters:     

  * **host** \(_str_\)

  * **aiosession** \(_ClientSession_ _|__None_\)

Return type:     

None

_async _aembed\(

    _model : str_,     _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity.html#TinyAsyncOpenAIInfinityEmbeddingClient.aembed)\#     

call the embedding of model, async method

Parameters:     

  * **model** \(_str_\) – to embedding model

  * **texts** \(_List_ _\[__str_ _\]_\) – List of sentences to embed.

Returns:     

List of vectors for each sentence

Return type:     

List\[List\[float\]\]

embed\(

    _model : str_,     _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity.html#TinyAsyncOpenAIInfinityEmbeddingClient.embed)\#     

call the embedding of model

Parameters:     

  * **model** \(_str_\) – to embedding model

  * **texts** \(_List_ _\[__str_ _\]_\) – List of sentences to embed.

Returns:     

List of vectors for each sentence

Return type:     

List\[List\[float\]\]

__On this page