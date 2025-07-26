# NeMoEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.nemo.NeMoEmbeddings.html
**Word Count:** 148
**Links Count:** 230
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# NeMoEmbeddings\#

_class _langchain\_community.embeddings.nemo.NeMoEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nemo.html#NeMoEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.0.37: Directly instantiating a NeMoEmbeddings from langchain-community is deprecated. Please use langchain-nvidia-ai-endpoints NVIDIAEmbeddings interface. It will not be removed until langchain-community==1.0.0.

NeMo embedding models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_endpoint\_url _: str_ _ = 'http://localhost:8088/v1/embeddings'_\#     

_param _batch\_size _: int_ _ = 16_\#     

_param _model _: str_ _ = 'NV-Embed-QA-003'_\#     

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nemo.html#NeMoEmbeddings.validate_environment)\#     

Validate that the end point is alive using the values that are provided.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nemo.html#NeMoEmbeddings.aembed_documents)\#     

Call out to NeMo’s embedding endpoint async for embedding search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nemo.html#NeMoEmbeddings.aembed_query)\#     

Call out to NeMo’s embedding endpoint async for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _documents : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nemo.html#NeMoEmbeddings.embed_documents)\#     

Embed a list of document texts.

Parameters:     

  * **texts** – The list of texts to embed.

  * **documents** \(_List_ _\[__str_ _\]_\)

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(_text : str_\) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nemo.html#NeMoEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

Examples using NeMoEmbeddings

  * [NVIDIA NeMo embeddings](https://python.langchain.com/docs/integrations/text_embedding/nemo/)

__On this page