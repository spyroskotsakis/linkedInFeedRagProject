# AwaEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.awa.AwaEmbeddings.html
**Word Count:** 135
**Links Count:** 228
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# AwaEmbeddings\#

_class _langchain\_community.embeddings.awa.AwaEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/awa.html#AwaEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Embedding documents and queries with Awa DB.

client\#     

The AwaEmbedding client.

model\#     

The name of the model used for embedding. Default is “all-mpnet-base-v2”.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _model _: str_ _ = 'all-mpnet-base-v2'_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/awa.html#AwaEmbeddings.embed_documents)\#     

Embed a list of documents using AwaEmbedding.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts need to be embedded

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(_text : str_\) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/awa.html#AwaEmbeddings.embed_query)\#     

Compute query embeddings using AwaEmbedding.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

set\_model\(_model\_name : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/awa.html#AwaEmbeddings.set_model)\#     

Set the model used for embedding. The default model used is all-mpnet-base-v2

Parameters:     

**model\_name** \(_str_\) – A string which represents the name of model.

Return type:     

None

Examples using AwaEmbeddings

  * [AwaDB](https://python.langchain.com/docs/integrations/providers/awadb/)

__On this page