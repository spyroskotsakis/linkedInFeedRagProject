# ModelScopeEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.modelscope_hub.ModelScopeEmbeddings.html
**Word Count:** 80
**Links Count:** 225
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# ModelScopeEmbeddings\#

_class _langchain\_community.embeddings.modelscope\_hub.ModelScopeEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/modelscope_hub.html#ModelScopeEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

ModelScopeHub embedding models.

To use, you should have the `modelscope` python package installed.

Example               from langchain_community.embeddings import ModelScopeEmbeddings     model_id = "damo/nlp_corom_sentence-embedding_english-base"     embed = ModelScopeEmbeddings(model_id=model_id, model_revision="v1.0.0")     

Initialize the modelscope

_param _embed _: Any_ _ = None_\#     

_param _model\_id _: str_ _ = 'damo/nlp\_corom\_sentence-embedding\_english-base'_\#     

Model name to use.

_param _model\_revision _: str | None_ _ = None_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/modelscope_hub.html#ModelScopeEmbeddings.embed_documents)\#     

Compute doc embeddings using a modelscope embedding model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/modelscope_hub.html#ModelScopeEmbeddings.embed_query)\#     

Compute query embeddings using a modelscope embedding model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using ModelScopeEmbeddings

  * [ModelScope](https://python.langchain.com/docs/integrations/providers/modelscope/)

__On this page