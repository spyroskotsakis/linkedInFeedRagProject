# JohnSnowLabsEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.johnsnowlabs.JohnSnowLabsEmbeddings.html
**Word Count:** 84
**Links Count:** 221
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# JohnSnowLabsEmbeddings\#

_class _langchain\_community.embeddings.johnsnowlabs.JohnSnowLabsEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/johnsnowlabs.html#JohnSnowLabsEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

JohnSnowLabs embedding models

To use, you should have the `johnsnowlabs` python package installed. .. rubric:: Example               from langchain_community.embeddings.johnsnowlabs import JohnSnowLabsEmbeddings          embedding = JohnSnowLabsEmbeddings(model='embed_sentence.bert')     output = embedding.embed_query("foo bar")     

Initialize the johnsnowlabs model.

_param _model _: Any_ _ = 'embed\_sentence.bert'_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/johnsnowlabs.html#JohnSnowLabsEmbeddings.embed_documents)\#     

Compute doc embeddings using a JohnSnowLabs transformer model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/johnsnowlabs.html#JohnSnowLabsEmbeddings.embed_query)\#     

Compute query embeddings using a JohnSnowLabs transformer model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using JohnSnowLabsEmbeddings

  * [John Snow Labs](https://python.langchain.com/docs/integrations/text_embedding/johnsnowlabs_embedding/)

__On this page