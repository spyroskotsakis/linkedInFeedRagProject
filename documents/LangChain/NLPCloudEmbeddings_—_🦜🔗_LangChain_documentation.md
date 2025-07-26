# NLPCloudEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.nlpcloud.NLPCloudEmbeddings.html
**Word Count:** 119
**Links Count:** 227
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# NLPCloudEmbeddings\#

_class _langchain\_community.embeddings.nlpcloud.NLPCloudEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nlpcloud.html#NLPCloudEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

NLP Cloud embedding models.

To use, you should have the nlpcloud python package installed

Example               from langchain_community.embeddings import NLPCloudEmbeddings          embeddings = NLPCloudEmbeddings()     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _gpu _: bool_ _\[Required\]_\#     

_param _model\_name _: str_ _\[Required\]_\#     

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nlpcloud.html#NLPCloudEmbeddings.validate_environment)\#     

Validate that api key and python package exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nlpcloud.html#NLPCloudEmbeddings.embed_documents)\#     

Embed a list of documents using NLP Cloud.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/nlpcloud.html#NLPCloudEmbeddings.embed_query)\#     

Embed a query using NLP Cloud.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using NLPCloudEmbeddings

  * [NLP Cloud](https://python.langchain.com/docs/integrations/text_embedding/nlp_cloud/)

  * [NLPCloud](https://python.langchain.com/docs/integrations/providers/nlpcloud/)

__On this page