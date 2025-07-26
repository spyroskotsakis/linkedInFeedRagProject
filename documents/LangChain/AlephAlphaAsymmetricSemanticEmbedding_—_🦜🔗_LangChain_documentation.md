# AlephAlphaAsymmetricSemanticEmbedding — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.aleph_alpha.AlephAlphaAsymmetricSemanticEmbedding.html
**Word Count:** 400
**Links Count:** 243
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# AlephAlphaAsymmetricSemanticEmbedding\#

_class _langchain\_community.embeddings.aleph\_alpha.AlephAlphaAsymmetricSemanticEmbedding[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/aleph_alpha.html#AlephAlphaAsymmetricSemanticEmbedding)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Aleph Alpha’s asymmetric semantic embedding.

AA provides you with an endpoint to embed a document and a query. The models were optimized to make the embeddings of documents and the query for a document as similar as possible. To learn more, check out: <https://docs.aleph-alpha.com/docs/tasks/semantic_embed/>

Example

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aleph\_alpha\_api\_key _: str | None_ _ = None_\#     

API key for Aleph Alpha API.

_param _compress\_to\_size _: int | None_ _ = None_\#     

Should the returned embeddings come back as an original 5120-dim vector, or should it be compressed to 128-dim.

_param _contextual\_control\_threshold _: int | None_ _ = None_\#     

Attention control parameters only apply to those tokens that have explicitly been set in the request.

_param _control\_log\_additive _: bool_ _ = True_\#     

Apply controls on prompt items by adding the log\(control\_factor\) to attention scores.

_param _host _: str_ _ = 'https://api.aleph-alpha.com'_\#     

The hostname of the API host. The default one is “<https://api.aleph-alpha.com>”\)

_param _hosting _: str | None_ _ = None_\#     

Determines in which datacenters the request may be processed. You can either set the parameter to “aleph-alpha” or omit it \(defaulting to None\). Not setting this value, or setting it to None, gives us maximal flexibility in processing your request in our own datacenters and on servers hosted with other providers. Choose this option for maximal availability. Setting it to “aleph-alpha” allows us to only process the request in our own datacenters. Choose this option for maximal data privacy.

_param _model _: str_ _ = 'luminous-base'_\#     

Model name to use.

_param _nice _: bool_ _ = False_\#     

Setting this to True, will signal to the API that you intend to be nice to other users by de-prioritizing your request below concurrent ones.

_param _normalize _: bool_ _ = False_\#     

Should returned embeddings be normalized

_param _request\_timeout\_seconds _: int_ _ = 305_\#     

Client timeout that will be set for HTTP requests in the requests library’s API calls. Server will close all requests after 300 seconds with an internal server error.

_param _total\_retries _: int_ _ = 8_\#     

The number of retries made in case requests fail with certain retryable status codes. If the last retry fails a corresponding exception is raised. Note, that between retries an exponential backoff is applied, starting with 0.5 s after the first retry and doubling for each retry made. So with the default setting of 8 retries a total wait time of 63.5 s is added between the retries.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/aleph_alpha.html#AlephAlphaAsymmetricSemanticEmbedding.embed_documents)\#     

Call out to Aleph Alpha’s asymmetric Document endpoint.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/aleph_alpha.html#AlephAlphaAsymmetricSemanticEmbedding.embed_query)\#     

Call out to Aleph Alpha’s asymmetric, query embedding endpoint :param text: The text to embed.

Returns:     

Embeddings for the text.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

Examples using AlephAlphaAsymmetricSemanticEmbedding

  * [Aleph Alpha](https://python.langchain.com/docs/integrations/providers/aleph_alpha/)

__On this page