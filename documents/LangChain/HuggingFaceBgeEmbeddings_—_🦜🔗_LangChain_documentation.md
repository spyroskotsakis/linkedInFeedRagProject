# HuggingFaceBgeEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.huggingface.HuggingFaceBgeEmbeddings.html
**Word Count:** 147
**Links Count:** 234
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# HuggingFaceBgeEmbeddings\#

_class _langchain\_community.embeddings.huggingface.HuggingFaceBgeEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface.html#HuggingFaceBgeEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.2.2: Use `:class:`~langchain_huggingface.HuggingFaceEmbeddings`` instead. It will not be removed until langchain-community==1.0.

HuggingFace sentence\_transformers embedding models.

To use, you should have the `sentence_transformers` python package installed. To use Nomic, make sure the version of `sentence_transformers` >= 2.3.0.

Bge Example:     

>  >     from langchain_community.embeddings import HuggingFaceBgeEmbeddings >      >     model_name = "BAAI/bge-large-en-v1.5" >     model_kwargs = {'device': 'cpu'} >     encode_kwargs = {'normalize_embeddings': True} >     hf = HuggingFaceBgeEmbeddings( >         model_name=model_name, >         model_kwargs=model_kwargs, >         encode_kwargs=encode_kwargs >     ) >     

Nomic Example:                    from langchain_community.embeddings import HuggingFaceBgeEmbeddings          model_name = "nomic-ai/nomic-embed-text-v1"     model_kwargs = {         'device': 'cpu',         'trust_remote_code':True         }     encode_kwargs = {'normalize_embeddings': True}     hf = HuggingFaceBgeEmbeddings(         model_name=model_name,         model_kwargs=model_kwargs,         encode_kwargs=encode_kwargs,         query_instruction = "search_query:",         embed_instruction = "search_document:"     )     

Initialize the sentence\_transformer.

_param _cache\_folder _: str | None_ _ = None_\#     

Path to store models. Can be also set by SENTENCE\_TRANSFORMERS\_HOME environment variable.

_param _embed\_instruction _: str_ _ = ''_\#     

Instruction to use for embedding document.

_param _encode\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass when calling the encode method of the model.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass to the model.

_param _model\_name _: str_ _ = 'BAAI/bge-large-en'_\#     

Model name to use.

_param _query\_instruction _: str_ _ = 'Represent this question for searching relevant passages: '_\#     

Instruction to use for embedding query.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface.html#HuggingFaceBgeEmbeddings.embed_documents)\#     

Compute doc embeddings using a HuggingFace transformer model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/huggingface.html#HuggingFaceBgeEmbeddings.embed_query)\#     

Compute query embeddings using a HuggingFace transformer model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using HuggingFaceBgeEmbeddings

  * [BGE on Hugging Face](https://python.langchain.com/docs/integrations/text_embedding/bge_huggingface/)

  * [Hugging Face](https://python.langchain.com/docs/integrations/providers/huggingface/)

__On this page