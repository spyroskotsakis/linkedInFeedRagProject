# LlamaCppEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.llamacpp.LlamaCppEmbeddings.html
**Word Count:** 223
**Links Count:** 246
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# LlamaCppEmbeddings\#

_class _langchain\_community.embeddings.llamacpp.LlamaCppEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llamacpp.html#LlamaCppEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

llama.cpp embedding models.

To use, you should have the llama-cpp-python library installed, and provide the path to the Llama model as a named parameter to the constructor. Check out: [abetlen/llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

Example               from langchain_community.embeddings import LlamaCppEmbeddings     llama = LlamaCppEmbeddings(model_path="/path/to/model.bin")     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _device _: str | None_ _ = None_\#     

Device type to use and pass to the model

_param _f16\_kv _: bool_ _ = False_\#     

Use half-precision for key/value cache.

_param _logits\_all _: bool_ _ = False_\#     

Return logits for all tokens, not just the last token.

_param _model\_path _: str_ _ = ''_\#     

_param _n\_batch _: int | None_ _ = 512_\#     

Number of tokens to process in parallel. Should be a number between 1 and n\_ctx.

_param _n\_ctx _: int_ _ = 512_\#     

Token context window.

_param _n\_gpu\_layers _: int | None_ _ = None_\#     

Number of layers to be loaded into gpu memory. Default None.

_param _n\_parts _: int_ _ = -1_\#     

Number of parts to split the model into. If -1, the number of parts is automatically determined.

_param _n\_threads _: int | None_ _ = None_\#     

Number of threads to use. If None, the number of threads is automatically determined.

_param _seed _: int_ _ = -1_\#     

Seed. If -1, a random seed is used.

_param _use\_mlock _: bool_ _ = False_\#     

Force system to keep model in RAM.

_param _verbose _: bool_ _ = True_\#     

Print verbose output to stderr.

_param _vocab\_only _: bool_ _ = False_\#     

Only load the vocabulary, no weights.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llamacpp.html#LlamaCppEmbeddings.embed_documents)\#     

Embed a list of documents using the Llama model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llamacpp.html#LlamaCppEmbeddings.embed_query)\#     

Embed a query using the Llama model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using LlamaCppEmbeddings

  * [Llama.cpp](https://python.langchain.com/docs/integrations/providers/llamacpp/)

__On this page