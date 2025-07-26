# HuggingFaceHubEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.huggingface_hub.HuggingFaceHubEmbeddings.html
**Word Count:** 180
**Links Count:** 231
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# HuggingFaceHubEmbeddings\#

_class _langchain\_community.embeddings.huggingface\_hub.HuggingFaceHubEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface_hub.html#HuggingFaceHubEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.2.2: Use `:class:`~langchain_huggingface.HuggingFaceEndpointEmbeddings`` instead. It will not be removed until langchain-community==1.0.

HuggingFaceHub embedding models.

To use, you should have the `huggingface_hub` python package installed, and the environment variable `HUGGINGFACEHUB_API_TOKEN` set with your API token, or pass it as a named parameter to the constructor.

Example               from langchain_community.embeddings import HuggingFaceHubEmbeddings     model = "sentence-transformers/all-mpnet-base-v2"     hf = HuggingFaceHubEmbeddings(         model=model,         task="feature-extraction",         huggingfacehub_api_token="my-api-key",     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _huggingfacehub\_api\_token _: str | None_ _ = None_\#     

_param _model _: str | None_ _ = None_\#     

Model name to use.

_param _model\_kwargs _: dict | None_ _ = None_\#     

Keyword arguments to pass to the model.

_param _repo\_id _: str | None_ _ = None_\#     

Huggingfacehub repository id, for backward compatibility.

_param _task _: str | None_ _ = 'feature-extraction'_\#     

Task to call the model with.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface_hub.html#HuggingFaceHubEmbeddings.aembed_documents)\#     

Async Call to HuggingFaceHub’s embedding endpoint for embedding search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface_hub.html#HuggingFaceHubEmbeddings.aembed_query)\#     

Async Call to HuggingFaceHub’s embedding endpoint for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface_hub.html#HuggingFaceHubEmbeddings.embed_documents)\#     

Call out to HuggingFaceHub’s embedding endpoint for embedding search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface_hub.html#HuggingFaceHubEmbeddings.embed_query)\#     

Call out to HuggingFaceHub’s embedding endpoint for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using HuggingFaceHubEmbeddings

  * [Hugging Face](https://python.langchain.com/docs/integrations/providers/huggingface/)

__On this page