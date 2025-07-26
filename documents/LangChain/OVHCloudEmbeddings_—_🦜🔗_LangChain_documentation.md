# OVHCloudEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.ovhcloud.OVHCloudEmbeddings.html
**Word Count:** 114
**Links Count:** 225
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# OVHCloudEmbeddings\#

_class _langchain\_community.embeddings.ovhcloud.OVHCloudEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ovhcloud.html#OVHCloudEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

OVHcloud AI Endpoints Embeddings.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _access\_token _: str_ _ = ''_\#     

OVHcloud AI Endpoints model name for embeddings generation

_param _model\_name _: str_ _ = ''_\#     

OVHcloud AI Endpoints region

_param _region _: str_ _ = 'kepler'_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ovhcloud.html#OVHCloudEmbeddings.embed_documents)\#     

Embed a list of documents. :param texts: The list of texts to embed. :type texts: List\[str\]

Returns:     

List of embeddings, one for each input text.

Return type:     

List\[List\[float\]\]

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ovhcloud.html#OVHCloudEmbeddings.embed_query)\#     

Embed a single query text. :param text: The text to embed. :type text: str

Returns:     

Embeddings for the text.

Return type:     

List\[float\]

Parameters:     

**text** \(_str_\)

Examples using OVHCloudEmbeddings

  * [OVHcloud](https://python.langchain.com/docs/integrations/text_embedding/ovhcloud/)

__On this page