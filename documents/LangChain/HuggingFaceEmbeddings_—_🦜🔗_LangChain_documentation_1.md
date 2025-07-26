# HuggingFaceEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/huggingface/embeddings/langchain_huggingface.embeddings.huggingface.HuggingFaceEmbeddings.html
**Word Count:** 166
**Links Count:** 103
**Scraped:** 2025-07-21 08:26:28
**Status:** completed

---

# HuggingFaceEmbeddings\#

_class _langchain\_huggingface.embeddings.huggingface.HuggingFaceEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_huggingface/embeddings/huggingface.html#HuggingFaceEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

HuggingFace sentence\_transformers embedding models.

To use, you should have the `sentence_transformers` python package installed.

Example               from langchain_huggingface import HuggingFaceEmbeddings          model_name = "sentence-transformers/all-mpnet-base-v2"     model_kwargs = {'device': 'cpu'}     encode_kwargs = {'normalize_embeddings': False}     hf = HuggingFaceEmbeddings(         model_name=model_name,         model_kwargs=model_kwargs,         encode_kwargs=encode_kwargs     )     

Initialize the sentence\_transformer.

_param _cache\_folder _: str | None_ _ = None_\#     

Path to store models. Can be also set by SENTENCE\_TRANSFORMERS\_HOME environment variable.

_param _encode\_kwargs _: dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass when calling the encode method for the documents of the Sentence Transformer model, such as prompt\_name, prompt, batch\_size, precision, normalize\_embeddings, and more. See also the Sentence Transformer documentation: <https://sbert.net/docs/package_reference/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode>

_param _model\_kwargs _: dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass to the Sentence Transformer model, such as device, prompts, default\_prompt\_name, revision, trust\_remote\_code, or token. See also the Sentence Transformer documentation: <https://sbert.net/docs/package_reference/SentenceTransformer.html#sentence_transformers.SentenceTransformer>

_param _model\_name _: str_ _ = 'sentence-transformers/all-mpnet-base-v2'__\(alias 'model'\)_\#     

Model name to use.

_param _multi\_process _: bool_ _ = False_\#     

Run encode\(\) on multiple GPUs.

_param _query\_encode\_kwargs _: dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass when calling the encode method for the query of the Sentence Transformer model, such as prompt\_name, prompt, batch\_size, precision, normalize\_embeddings, and more. See also the Sentence Transformer documentation: <https://sbert.net/docs/package_reference/SentenceTransformer.html#sentence_transformers.SentenceTransformer.encode>

_param _show\_progress _: bool_ _ = False_\#     

Whether to show a progress bar.

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

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_huggingface/embeddings/huggingface.html#HuggingFaceEmbeddings.embed_documents)\#     

Compute doc embeddings using a HuggingFace transformer model.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

list\[list\[float\]\]

embed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_huggingface/embeddings/huggingface.html#HuggingFaceEmbeddings.embed_query)\#     

Compute query embeddings using a HuggingFace transformer model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

list\[float\]

Examples using HuggingFaceEmbeddings

  * [Aerospike](https://python.langchain.com/docs/integrations/vectorstores/aerospike/)

  * [self-query-qdrant](https://python.langchain.com/docs/templates/self-query-qdrant/)

__On this page