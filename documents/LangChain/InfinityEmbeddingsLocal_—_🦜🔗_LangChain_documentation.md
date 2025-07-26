# InfinityEmbeddingsLocal — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.infinity_local.InfinityEmbeddingsLocal.html
**Word Count:** 151
**Links Count:** 237
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# InfinityEmbeddingsLocal\#

_class _langchain\_community.embeddings.infinity\_local.InfinityEmbeddingsLocal[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity_local.html#InfinityEmbeddingsLocal)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Optimized Infinity embedding models.

[michaelfeil/infinity](https://github.com/michaelfeil/infinity) This class deploys a local Infinity instance to embed text. The class requires async usage.

Infinity is a class to interact with Embedding Models on [michaelfeil/infinity](https://github.com/michaelfeil/infinity)

Example               from langchain_community.embeddings import InfinityEmbeddingsLocal     async with InfinityEmbeddingsLocal(         model="BAAI/bge-small-en-v1.5",         revision=None,         device="cpu",     ) as embedder:         embeddings = await engine.aembed_documents(["text1", "text2"])     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _backend _: str_ _ = 'torch'_\#     

Backend for inference, e.g. ‘torch’ \(recommended for ROCm/Nvidia\)

_param _batch\_size _: int_ _ = 32_\#     

Internal batch size for inference, e.g. 32

_param _device _: str_ _ = 'auto'_\#     

Device to use for inference, e.g. ‘cpu’ or ‘cuda’, or ‘mps’

_param _engine _: Any_ _ = None_\#     

Infinity’s AsyncEmbeddingEngine.

_param _model _: str_ _\[Required\]_\#     

Underlying model id from huggingface, e.g. BAAI/bge-small-en-v1.5

_param _model\_warmup _: bool_ _ = True_\#     

Warmup the model with the max batch size.

_param _revision _: str | None_ _ = None_\#     

Model version, the commit hash from huggingface

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity_local.html#InfinityEmbeddingsLocal.aembed_documents)\#     

Async call out to Infinity’s embedding endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity_local.html#InfinityEmbeddingsLocal.aembed_query)\#     

Async call out to Infinity’s embedding endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity_local.html#InfinityEmbeddingsLocal.embed_documents)\#     

This method is async only.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/infinity_local.html#InfinityEmbeddingsLocal.embed_query)\#     

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

Examples using InfinityEmbeddingsLocal

  * [Infinity](https://python.langchain.com/docs/integrations/text_embedding/infinity/)

__On this page