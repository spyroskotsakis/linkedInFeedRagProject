# IpexLLMBgeEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.ipex_llm.IpexLLMBgeEmbeddings.html
**Word Count:** 157
**Links Count:** 234
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# IpexLLMBgeEmbeddings\#

_class _langchain\_community.embeddings.ipex\_llm.IpexLLMBgeEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ipex_llm.html#IpexLLMBgeEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Wrapper around the BGE embedding model with IPEX-LLM optimizations on Intel CPUs and GPUs.

To use, you should have the `ipex-llm` and `sentence_transformers` package installed. Refer to [here](https://python.langchain.com/v0.1/docs/integrations/text_embedding/ipex_llm/) for installation on Intel CPU.

Example on Intel CPU:                    from langchain_community.embeddings import IpexLLMBgeEmbeddings          embedding_model = IpexLLMBgeEmbeddings(         model_name="BAAI/bge-large-en-v1.5",         model_kwargs={},         encode_kwargs={"normalize_embeddings": True},     )     

Refer to [here](https://python.langchain.com/v0.1/docs/integrations/text_embedding/ipex_llm_gpu/) for installation on Intel GPU.

Example on Intel GPU:                    from langchain_community.embeddings import IpexLLMBgeEmbeddings          embedding_model = IpexLLMBgeEmbeddings(         model_name="BAAI/bge-large-en-v1.5",         model_kwargs={"device": "xpu"},         encode_kwargs={"normalize_embeddings": True},     )     

Initialize the sentence\_transformer.

_param _cache\_folder _: str | None_ _ = None_\#     

Path to store models. Can be also set by SENTENCE\_TRANSFORMERS\_HOME environment variable.

_param _embed\_instruction _: str_ _ = ''_\#     

Instruction to use for embedding document.

_param _encode\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass when calling the encode method of the model.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass to the model.

_param _model\_name _: str_ _ = 'BAAI/bge-small-en-v1.5'_\#     

Model name to use.

_param _query\_instruction _: str_ _ = 'Represent this question for searching relevant passages: '_\#     

Instruction to use for embedding query.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ipex_llm.html#IpexLLMBgeEmbeddings.embed_documents)\#     

Compute doc embeddings using a HuggingFace transformer model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ipex_llm.html#IpexLLMBgeEmbeddings.embed_query)\#     

Compute query embeddings using a HuggingFace transformer model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using IpexLLMBgeEmbeddings

  * [Local BGE Embeddings with IPEX-LLM on Intel CPU](https://python.langchain.com/docs/integrations/text_embedding/ipex_llm/)

  * [Local BGE Embeddings with IPEX-LLM on Intel GPU](https://python.langchain.com/docs/integrations/text_embedding/ipex_llm_gpu/)

__On this page