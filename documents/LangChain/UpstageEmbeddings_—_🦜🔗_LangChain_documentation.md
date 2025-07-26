# UpstageEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/upstage/embeddings/langchain_upstage.embeddings.UpstageEmbeddings.html
**Word Count:** 283
**Links Count:** 122
**Scraped:** 2025-07-21 08:45:22
**Status:** completed

---

# UpstageEmbeddings\#

_class _langchain\_upstage.embeddings.UpstageEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/embeddings.html#UpstageEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

UpstageEmbeddings embedding model.

To use, set the environment variable UPSTAGE\_API\_KEY with your API key or pass it as a named parameter to the constructor.

Example               from langchain_upstage import UpstageEmbeddings          model = UpstageEmbeddings(model='solar-embedding-1-large')     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allowed\_special _: Literal\['all'\] | Set\[str\]__ = \{\}_\#     

Not yet supported.

_param _chunk\_size _: int_ _ = 1000_\#     

Maximum number of texts to embed in each batch.

Not yet supported.

_param _default\_headers _: Mapping\[str, str\] | None_ _ = None_\#     

_param _default\_query _: Mapping\[str, object\] | None_ _ = None_\#     

_param _dimensions _: int | None_ _ = None_\#     

The number of dimensions the resulting output embeddings should have.

Not yet supported.

_param _disallowed\_special _: Literal\['all'\] | Set\[str\] | Sequence\[str\]__ = 'all'_\#     

Not yet supported.

_param _embed\_batch\_size _: int_ _ = 10_\#     

_param _embedding\_ctx\_length _: int_ _ = 4096_\#     

The maximum number of tokens to embed at once.

Not yet supported.

_param _http\_async\_client _: Any | None_ _ = None_\#     

Optional httpx.AsyncClient. Only used for async invocations. Must specify http\_client as well if you’d like a custom client for sync invocations.

_param _http\_client _: Any | None_ _ = None_\#     

Optional httpx.Client. Only used for sync invocations. Must specify http\_async\_client as well if you’d like a custom client for async invocations.

_param _max\_retries _: int_ _ = 2_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _\[Required\]_\#     

Embeddings model name to use. Do not add suffixes like -query and -passage. Instead, use ‘solar-embedding-1-large’ for example.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Holds any model parameters valid for create call not explicitly specified.

_param _request\_timeout _: float | Tuple\[float, float\] | Any | None_ _ = None_ _\(alias 'timeout'\)_\#     

Timeout for requests to Upstage embedding API. Can be float, httpx.Timeout or None.

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a progress bar when embedding.

Not yet supported.

_param _skip\_empty _: bool_ _ = False_\#     

Whether to skip empty strings when embedding or raise an error. Defaults to not skipping.

Not yet supported.

_param _upstage\_api\_base _: str | None_ _\[Optional\]__\(alias 'base\_url'\)_\#     

Endpoint URL to use.

_param _upstage\_api\_key _: SecretStr_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Automatically inferred from env are UPSTAGE\_API\_KEY if not provided.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/embeddings.html#UpstageEmbeddings.aembed_documents)\#     

Embed a list of document texts using passage model asynchronously.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/embeddings.html#UpstageEmbeddings.aembed_query)\#     

Asynchronous Embed query text using query model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/embeddings.html#UpstageEmbeddings.embed_documents)\#     

Embed a list of document texts using passage model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/embeddings.html#UpstageEmbeddings.embed_query)\#     

Embed query text using query model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

__On this page