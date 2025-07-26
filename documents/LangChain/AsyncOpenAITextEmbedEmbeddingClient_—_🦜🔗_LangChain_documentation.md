# AsyncOpenAITextEmbedEmbeddingClient — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.textembed.AsyncOpenAITextEmbedEmbeddingClient.html
**Word Count:** 106
**Links Count:** 227
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# AsyncOpenAITextEmbedEmbeddingClient\#

_class _langchain\_community.embeddings.textembed.AsyncOpenAITextEmbedEmbeddingClient\(

    _host : str = 'http://localhost:8000/v1'_,     _api\_key : str | None = None_,     _aiosession : ClientSession | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/textembed.html#AsyncOpenAITextEmbedEmbeddingClient)\#     

A client to handle synchronous and asynchronous requests to the TextEmbed API.

Parameters:     

  * **host** \(_str_\)

  * **api\_key** \(_str_ _|__None_\)

  * **aiosession** \(_ClientSession_ _|__None_\)

host\#     

The base URL for the TextEmbed API.

Type:     

str

api\_key\#     

The API key for authenticating with the TextEmbed API.

Type:     

str

aiosession\#     

The aiohttp session for async requests.

Type:     

Optional\[aiohttp.ClientSession\]

\_batch\_size\#     

Maximum batch size for a single request.

Type:     

int

Methods

`__init__`\(\[host, api\_key, aiosession\]\) |    ---|---   `aembed`\(model, texts\) | Embeds a list of texts asynchronously.   `embed`\(model, texts\) | Embeds a list of texts synchronously.      \_\_init\_\_\(

    _host : str = 'http://localhost:8000/v1'_,     _api\_key : str | None = None_,     _aiosession : ClientSession | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/textembed.html#AsyncOpenAITextEmbedEmbeddingClient.__init__)\#     

Parameters:     

  * **host** \(_str_\)

  * **api\_key** \(_str_ _|__None_\)

  * **aiosession** \(_ClientSession_ _|__None_\)

Return type:     

None

_async _aembed\(

    _model : str_,     _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/textembed.html#AsyncOpenAITextEmbedEmbeddingClient.aembed)\#     

Embeds a list of texts asynchronously.

Parameters:     

  * **model** \(_str_\) – The model to use for embedding.

  * **texts** \(_List_ _\[__str_ _\]_\) – List of texts to embed.

Returns:     

List of embeddings for the texts.

Return type:     

List\[List\[float\]\]

embed\(

    _model : str_,     _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/textembed.html#AsyncOpenAITextEmbedEmbeddingClient.embed)\#     

Embeds a list of texts synchronously.

Parameters:     

  * **model** \(_str_\) – The model to use for embedding.

  * **texts** \(_List_ _\[__str_ _\]_\) – List of texts to embed.

Returns:     

List of embeddings for the texts.

Return type:     

List\[List\[float\]\]

__On this page