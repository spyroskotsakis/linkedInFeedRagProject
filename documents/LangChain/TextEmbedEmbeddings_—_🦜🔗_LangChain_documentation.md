# TextEmbedEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.textembed.TextEmbedEmbeddings.html
**Word Count:** 166
**Links Count:** 238
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# TextEmbedEmbeddings\#

_class _langchain\_community.embeddings.textembed.TextEmbedEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/textembed.html#TextEmbedEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

A class to handle embedding requests to the TextEmbed API.

model\#     

The TextEmbed model ID to use for embeddings.

api\_url\#     

The base URL for the TextEmbed API.

api\_key\#     

The API key for authenticating with the TextEmbed API.

client\#     

The TextEmbed client instance.

Example               from langchain_community.embeddings import TextEmbedEmbeddings          embeddings = TextEmbedEmbeddings(         model="sentence-transformers/clip-ViT-B-32",         api_url="http://localhost:8000/v1",         api_key="<API_KEY>"     )     

For more information: [kevaldekivadiya2415/textembed](https://github.com/kevaldekivadiya2415/textembed/blob/main/docs/setup.md)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_key _: SecretStr_ _\[Optional\]_\#     

API Key for authentication

_param _api\_url _: str_ _\[Optional\]_\#     

Endpoint URL to use.

_param _client _: Any_ _ = None_\#     

TextEmbed client.

_param _model _: str_ _\[Required\]_\#     

Underlying TextEmbed model id.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/textembed.html#TextEmbedEmbeddings.aembed_documents)\#     

Async call out to TextEmbed’s embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

List\[List\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/textembed.html#TextEmbedEmbeddings.aembed_query)\#     

Async call out to TextEmbed’s embedding endpoint for a single query.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

List\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/textembed.html#TextEmbedEmbeddings.embed_documents)\#     

Call out to TextEmbed’s embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

List\[List\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/textembed.html#TextEmbedEmbeddings.embed_query)\#     

Call out to TextEmbed’s embedding endpoint for a single query.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

List\[float\]

Examples using TextEmbedEmbeddings

  * [TextEmbed - Embedding Inference Server](https://python.langchain.com/docs/integrations/text_embedding/textembed/)

__On this page