# HuggingFaceInferenceAPIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.huggingface.HuggingFaceInferenceAPIEmbeddings.html
**Word Count:** 167
**Links Count:** 227
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# HuggingFaceInferenceAPIEmbeddings\#

_class _langchain\_community.embeddings.huggingface.HuggingFaceInferenceAPIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface.html#HuggingFaceInferenceAPIEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.2.2: Use `:class:`~langchain_huggingface.HuggingFaceEndpointEmbeddings`` instead. It will not be removed until langchain-community==1.0.

Embed texts using the HuggingFace API.

Requires a HuggingFace Inference API key and a model name.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _additional\_headers _: Dict\[str, str\]__ = \{\}_\#     

Pass additional headers to the requests library if needed.

_param _api\_key _: SecretStr_ _\[Required\]_\#     

Your API key for the HuggingFace Inference API.

_param _api\_url _: str | None_ _ = None_\#     

Custom inference endpoint url. None for using default public url.

_param _model\_name _: str_ _ = 'sentence-transformers/all-MiniLM-L6-v2'_\#     

The name of the model to use for text embeddings.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface.html#HuggingFaceInferenceAPIEmbeddings.embed_documents)\#     

Get the embeddings for a list of texts.

Parameters:     

**texts** \(_Documents_\) – A list of texts to get embeddings for.

Returns:     

Embedded texts as List\[List\[float\]\], where each inner List\[float\]     

corresponds to a single input text.

Return type:     

_List_\[_List_\[float\]\]

Example               from langchain_community.embeddings import (         HuggingFaceInferenceAPIEmbeddings,     )          hf_embeddings = HuggingFaceInferenceAPIEmbeddings(         api_key="your_api_key",         model_name="sentence-transformers/all-MiniLM-l6-v2"     )     texts = ["Hello, world!", "How are you?"]     hf_embeddings.embed_documents(texts)     

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface.html#HuggingFaceInferenceAPIEmbeddings.embed_query)\#     

Compute query embeddings using a HuggingFace transformer model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using HuggingFaceInferenceAPIEmbeddings

  * [Hugging Face](https://python.langchain.com/docs/integrations/text_embedding/huggingfacehub/)

__On this page