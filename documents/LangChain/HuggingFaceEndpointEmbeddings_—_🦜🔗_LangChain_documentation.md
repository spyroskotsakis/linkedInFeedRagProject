# HuggingFaceEndpointEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/huggingface/embeddings/langchain_huggingface.embeddings.huggingface_endpoint.HuggingFaceEndpointEmbeddings.html
**Word Count:** 198
**Links Count:** 99
**Scraped:** 2025-07-21 08:26:28
**Status:** completed

---

# HuggingFaceEndpointEmbeddings\#

_class _langchain\_huggingface.embeddings.huggingface\_endpoint.HuggingFaceEndpointEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_huggingface/embeddings/huggingface_endpoint.html#HuggingFaceEndpointEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

HuggingFaceHub embedding models.

To use, you should have the `huggingface_hub` python package installed, and the environment variable `HUGGINGFACEHUB_API_TOKEN` set with your API token, or pass it as a named parameter to the constructor.

Example               from langchain_huggingface import HuggingFaceEndpointEmbeddings     model = "sentence-transformers/all-mpnet-base-v2"     hf = HuggingFaceEndpointEmbeddings(         model=model,         task="feature-extraction",         huggingfacehub_api_token="my-api-key",     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _huggingfacehub\_api\_token _: str | None_ _\[Optional\]_\#     

_param _model _: str | None_ _ = None_\#     

Model name to use.

_param _model\_kwargs _: dict | None_ _ = None_\#     

Keyword arguments to pass to the model.

_param _provider _: str | None_ _ = None_\#     

Name of the provider to use for inference with the model specified in `repo_id`. e.g. “sambanova”. if not specified, defaults to HF Inference API. available providers can be found in the \[huggingface\_hub documentation\]\(<https://huggingface.co/docs/huggingface_hub/guides/inference#supported-providers-and-tasks>\).

_param _repo\_id _: str | None_ _ = None_\#     

Huggingfacehub repository id, for backward compatibility.

_param _task _: str | None_ _ = 'feature-extraction'_\#     

Task to call the model with.

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_huggingface/embeddings/huggingface_endpoint.html#HuggingFaceEndpointEmbeddings.aembed_documents)\#     

Async Call to HuggingFaceHub’s embedding endpoint for embedding search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_huggingface/embeddings/huggingface_endpoint.html#HuggingFaceEndpointEmbeddings.aembed_query)\#     

Async Call to HuggingFaceHub’s embedding endpoint for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

list\[float\]

embed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_huggingface/embeddings/huggingface_endpoint.html#HuggingFaceEndpointEmbeddings.embed_documents)\#     

Call out to HuggingFaceHub’s embedding endpoint for embedding search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

list\[list\[float\]\]

embed\_query\(

    _text : str_, \) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_huggingface/embeddings/huggingface_endpoint.html#HuggingFaceEndpointEmbeddings.embed_query)\#     

Call out to HuggingFaceHub’s embedding endpoint for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

list\[float\]

__On this page