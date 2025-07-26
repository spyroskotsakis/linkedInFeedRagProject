# JinaEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.jina.JinaEmbeddings.html
**Word Count:** 120
**Links Count:** 227
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# JinaEmbeddings\#

_class _langchain\_community.embeddings.jina.JinaEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/jina.html#JinaEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Jina embedding models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _jina\_api\_key _: SecretStr | None_ _ = None_\#     

_param _model\_name _: str_ _ = 'jina-embeddings-v2-base-en'_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/jina.html#JinaEmbeddings.embed_documents)\#     

Call out to Jina’s embedding endpoint. :param texts: The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_images\(

    _uris : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/jina.html#JinaEmbeddings.embed_images)\#     

Call out to Jina’s image embedding endpoint. :param uris: The list of uris to embed.

Returns:     

List of embeddings, one for each text.

Parameters:     

**uris** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(_text : str_\) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/jina.html#JinaEmbeddings.embed_query)\#     

Call out to Jina’s embedding endpoint. :param text: The text to embed.

Returns:     

Embeddings for the text.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

Examples using JinaEmbeddings

  * [Jina](https://python.langchain.com/docs/integrations/providers/jina/)

  * [Jina Reranker](https://python.langchain.com/docs/integrations/document_transformers/jina_rerank/)

__On this page