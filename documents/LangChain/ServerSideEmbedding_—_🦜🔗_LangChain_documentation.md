# ServerSideEmbedding — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_genai/google_vector_store/langchain_google_genai.google_vector_store.ServerSideEmbedding.html
**Word Count:** 66
**Links Count:** 89
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# ServerSideEmbedding\#

_class _langchain\_google\_genai.google\_vector\_store.ServerSideEmbedding[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/google_vector_store.html#ServerSideEmbedding)\#     

Do nothing embedding model where the embedding is done by the server.

Methods

`aembed_documents`\(texts\) | Asynchronous Embed search docs.   ---|---   `aembed_query`\(text\) | Asynchronous Embed query text.   `embed_documents`\(texts\) | Embed search docs.   `embed_query`\(text\) | Embed query text.      _async _aembed\_documents\(

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/google_vector_store.html#ServerSideEmbedding.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/google_vector_store.html#ServerSideEmbedding.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

__On this page