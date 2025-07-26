# TensorflowHubEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.tensorflow_hub.TensorflowHubEmbeddings.html
**Word Count:** 83
**Links Count:** 221
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# TensorflowHubEmbeddings\#

_class _langchain\_community.embeddings.tensorflow\_hub.TensorflowHubEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/tensorflow_hub.html#TensorflowHubEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

TensorflowHub embedding models.

To use, you should have the `tensorflow_text` python package installed.

Example               from langchain_community.embeddings import TensorflowHubEmbeddings     url = "https://tfhub.dev/google/universal-sentence-encoder-multilingual/3"     tf = TensorflowHubEmbeddings(model_url=url)     

Initialize the tensorflow\_hub and tensorflow\_text.

_param _model\_url _: str_ _ = 'https://tfhub.dev/google/universal-sentence-encoder-multilingual/3'_\#     

Model name to use.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/tensorflow_hub.html#TensorflowHubEmbeddings.embed_documents)\#     

Compute doc embeddings using a TensorflowHub embedding model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/tensorflow_hub.html#TensorflowHubEmbeddings.embed_query)\#     

Compute query embeddings using a TensorflowHub embedding model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using TensorflowHubEmbeddings

  * [TensorFlow Hub](https://python.langchain.com/docs/integrations/text_embedding/tensorflowhub/)

__On this page