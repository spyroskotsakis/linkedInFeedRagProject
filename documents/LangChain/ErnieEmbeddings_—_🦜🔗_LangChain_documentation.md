# ErnieEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.ernie.ErnieEmbeddings.html
**Word Count:** 104
**Links Count:** 236
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# ErnieEmbeddings\#

_class _langchain\_community.embeddings.ernie.ErnieEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ernie.html#ErnieEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.0.13: Use `QianfanEmbeddingsEndpoint` instead.

Ernie Embeddings V1 embedding models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _access\_token _: str | None_ _ = None_\#     

_param _chunk\_size _: int_ _ = 16_\#     

_param _ernie\_api\_base _: str | None_ _ = None_\#     

_param _ernie\_client\_id _: str | None_ _ = None_\#     

_param _ernie\_client\_secret _: str | None_ _ = None_\#     

_param _model\_name _: str_ _ = 'ErnieBot-Embedding-V1'_\#     

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ernie.html#ErnieEmbeddings.validate_environment)\#     

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ernie.html#ErnieEmbeddings.aembed_documents)\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed

Returns:     

List of embeddings, one for each text.

Return type:     

List\[List\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ernie.html#ErnieEmbeddings.aembed_query)\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

List\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ernie.html#ErnieEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed

Returns:     

List of embeddings, one for each text.

Return type:     

List\[List\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/ernie.html#ErnieEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

List\[float\]

Examples using ErnieEmbeddings

  * [ERNIE](https://python.langchain.com/docs/integrations/text_embedding/ernie/)

__On this page