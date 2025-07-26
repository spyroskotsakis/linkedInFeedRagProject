# InfinityEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.infinity.InfinityEmbeddings.html
**Word Count:** 137
**Links Count:** 229
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# InfinityEmbeddings\#

_class _langchain\_community.embeddings.infinity.InfinityEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity.html#InfinityEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Self-hosted embedding models for infinity package.

See [michaelfeil/infinity](https://github.com/michaelfeil/infinity) This also works for text-embeddings-inference and other self-hosted openai-compatible servers.

Infinity is a package to interact with Embedding Models on [michaelfeil/infinity](https://github.com/michaelfeil/infinity)

Example               from langchain_community.embeddings import InfinityEmbeddings     InfinityEmbeddings(         model="BAAI/bge-small",         infinity_api_url="http://localhost:7997",     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Any_ _ = None_\#     

Infinity client.

_param _infinity\_api\_url _: str_ _ = 'http://localhost:7997'_\#     

Endpoint URL to use.

_param _model _: str_ _\[Required\]_\#     

Underlying Infinity model id.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity.html#InfinityEmbeddings.aembed_documents)\#     

Async call out to Infinity’s embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity.html#InfinityEmbeddings.aembed_query)\#     

Async call out to Infinity’s embedding endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity.html#InfinityEmbeddings.embed_documents)\#     

Call out to Infinity’s embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity.html#InfinityEmbeddings.embed_query)\#     

Call out to Infinity’s embedding endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using InfinityEmbeddings

  * [Infinity](https://python.langchain.com/docs/integrations/providers/infinity/)

__On this page