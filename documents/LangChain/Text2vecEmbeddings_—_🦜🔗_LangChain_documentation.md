# Text2vecEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.text2vec.Text2vecEmbeddings.html
**Word Count:** 102
**Links Count:** 229
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# Text2vecEmbeddings\#

_class _langchain\_community.embeddings.text2vec.Text2vecEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/text2vec.html#Text2vecEmbeddings)\#     

Bases: [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings"), `BaseModel`

text2vec embedding models.

Install text2vec first, run ‘pip install -U text2vec’. The github repository for text2vec is : [shibing624/text2vec](https://github.com/shibing624/text2vec)

Example               from langchain_community.embeddings.text2vec import Text2vecEmbeddings          embedding = Text2vecEmbeddings()     embedding.embed_documents([         "This is a CoSENT(Cosine Sentence) model.",         "It maps sentences to a 768 dimensional dense vector space.",     ])     embedding.embed_query(         "It can be used for text matching or semantic search."     )     

_param _device _: str | None_ _ = None_\#     

_param _encoder\_type _: Any_ _ = 'MEAN'_\#     

_param _max\_seq\_length _: int_ _ = 256_\#     

_param _model _: Any_ _ = None_\#     

_param _model\_name\_or\_path _: str | None_ _ = None_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/text2vec.html#Text2vecEmbeddings.embed_documents)\#     

Embed documents using the text2vec embeddings model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/text2vec.html#Text2vecEmbeddings.embed_query)\#     

Embed a query using the text2vec embeddings model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

__On this page