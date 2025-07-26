# GooglePalmEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.google_palm.GooglePalmEmbeddings.html
**Word Count:** 95
**Links Count:** 230
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# GooglePalmEmbeddings\#

_class _langchain\_community.embeddings.google\_palm.GooglePalmEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/google_palm.html#GooglePalmEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Google’s PaLM Embeddings APIs.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Any_ _\[Required\]_\#     

_param _google\_api\_key _: str | None_ _\[Required\]_\#     

_param _model\_name _: str_ _ = 'models/embedding-gecko-001'_\#     

Model name to use.

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a tqdm progress bar. Must have tqdm installed.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/google_palm.html#GooglePalmEmbeddings.validate_environment)\#     

Validate api key, python package exists.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/google_palm.html#GooglePalmEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/google_palm.html#GooglePalmEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

Examples using GooglePalmEmbeddings

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

__On this page