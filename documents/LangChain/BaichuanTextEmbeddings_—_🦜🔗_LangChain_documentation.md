# BaichuanTextEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.baichuan.BaichuanTextEmbeddings.html
**Word Count:** 168
**Links Count:** 226
**Scraped:** 2025-07-21 08:07:57
**Status:** completed

---

# BaichuanTextEmbeddings\#

_class _langchain\_community.embeddings.baichuan.BaichuanTextEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/baichuan.html#BaichuanTextEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Baichuan Text Embedding models.

Setup:     

To use, you should set the environment variable `BAICHUAN_API_KEY` to your API key or pass it as a named parameter to the constructor.               export BAICHUAN_API_KEY="your-api-key"     

Instantiate:                    from langchain_community.embeddings import BaichuanTextEmbeddings          embeddings = BaichuanTextEmbeddings()     

Embed:                    # embed the documents     vectors = embeddings.embed_documents([text1, text2, ...])          # embed the query     vectors = embeddings.embed_query(text)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _baichuan\_api\_key _: SecretStr_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Automatically inferred from env var BAICHUAN\_API\_KEY if not provided.

_param _chunk\_size _: int_ _ = 16_\#     

Chunk size when multiple texts are input

_param _model\_name _: str_ _ = 'Baichuan-Text-Embedding'__\(alias 'model'\)_\#     

The model used to embed the documents.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/baichuan.html#BaichuanTextEmbeddings.embed_documents)\#     

Public method to get embeddings for a list of documents.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

A list of embeddings, one for each text, or None if an error occurs.

Return type:     

_List_\[_List_\[float\]\] | None

embed\_query\(

    _text : str_, \) → List\[float\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/baichuan.html#BaichuanTextEmbeddings.embed_query)\#     

Public method to get embedding for a single query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text, or None if an error occurs.

Return type:     

_List_\[float\] | None

Examples using BaichuanTextEmbeddings

  * [Baichuan](https://python.langchain.com/docs/integrations/providers/baichuan/)

  * [Baichuan Text Embeddings](https://python.langchain.com/docs/integrations/text_embedding/baichuan/)

__On this page