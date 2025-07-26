# Model2vecEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.model2vec.Model2vecEmbeddings.html
**Word Count:** 118
**Links Count:** 226
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# Model2vecEmbeddings\#

_class _langchain\_community.embeddings.model2vec.Model2vecEmbeddings\(_model : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/model2vec.html#Model2vecEmbeddings)\#     

Model2Vec embedding models.

Install model2vec first, run ‘pip install -U model2vec’. The github repository for model2vec is : [MinishLab/model2vec](https://github.com/MinishLab/model2vec)

Example               from langchain_community.embeddings import Model2vecEmbeddings          embedding = Model2vecEmbeddings("minishlab/potion-base-8M")     embedding.embed_documents([         "It's dangerous to go alone!",         "It's a secret to everybody.",     ])     embedding.embed_query(         "Take this with you."     )     

Initialize embeddings.

Parameters:     

**model** \(_str_\) – Model name.

Methods

`__init__`\(model\) | Initialize embeddings.   ---|---   `aembed_documents`\(texts\) | Asynchronous Embed search docs.   `aembed_query`\(text\) | Asynchronous Embed query text.   `embed_documents`\(texts\) | Embed documents using the model2vec embeddings model.   `embed_query`\(text\) | Embed a query using the model2vec embeddings model.      \_\_init\_\_\(_model : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/model2vec.html#Model2vecEmbeddings.__init__)\#     

Initialize embeddings.

Parameters:     

**model** \(_str_\) – Model name.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/model2vec.html#Model2vecEmbeddings.embed_documents)\#     

Embed documents using the model2vec embeddings model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/model2vec.html#Model2vecEmbeddings.embed_query)\#     

Embed a query using the model2vec embeddings model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

__On this page