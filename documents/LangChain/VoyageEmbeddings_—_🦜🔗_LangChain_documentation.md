# VoyageEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.voyageai.VoyageEmbeddings.html
**Word Count:** 257
**Links Count:** 237
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# VoyageEmbeddings\#

_class _langchain\_community.embeddings.voyageai.VoyageEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/voyageai.html#VoyageEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.0.29: Use `:class:`~langchain_voyageai.VoyageAIEmbeddings`` instead. It will not be removed until langchain-community==1.0.

Voyage embedding models.

To use, you should have the environment variable `VOYAGE_API_KEY` set with your API key or pass it as a named parameter to the constructor.

Example               from langchain_community.embeddings import VoyageEmbeddings          voyage = VoyageEmbeddings(voyage_api_key="your-api-key", model="voyage-2")     text = "This is a test query."     query_result = voyage.embed_query(text)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _batch\_size _: int_ _\[Required\]_\#     

Maximum number of texts to embed in each API request.

_param _max\_retries _: int_ _ = 6_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _\[Required\]_\#     

_param _request\_timeout _: float | Tuple\[float, float\] | None_ _ = None_\#     

Timeout in seconds for the API request.

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a progress bar when embedding. Must have tqdm installed if set to True.

_param _truncation _: bool_ _ = True_\#     

Whether to truncate the input texts to fit within the context length.

If True, over-length input texts will be truncated to fit within the context length, before vectorized by the embedding model. If False, an error will be raised if any given text exceeds the context length.

_param _voyage\_api\_base _: str_ _ = 'https://api.voyageai.com/v1/embeddings'_\#     

_param _voyage\_api\_key _: SecretStr | None_ _ = None_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/voyageai.html#VoyageEmbeddings.embed_documents)\#     

Call out to Voyage Embedding endpoint for embedding search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_general\_texts\(

    _texts : List\[str\]_,     _\*_ ,     _input\_type : str | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/voyageai.html#VoyageEmbeddings.embed_general_texts)\#     

Call out to Voyage Embedding endpoint for embedding general text.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

  * **input\_type** \(_str_ _|__None_\) – Type of the input text. Default to None, meaning the type is unspecified. Other options: query, document.

Returns:     

Embedding for the text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/voyageai.html#VoyageEmbeddings.embed_query)\#     

Call out to Voyage Embedding endpoint for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)