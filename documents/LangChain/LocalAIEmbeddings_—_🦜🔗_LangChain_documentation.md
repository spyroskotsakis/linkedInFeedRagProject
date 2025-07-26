# LocalAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.localai.LocalAIEmbeddings.html
**Word Count:** 258
**Links Count:** 256
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# LocalAIEmbeddings\#

_class _langchain\_community.embeddings.localai.LocalAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/localai.html#LocalAIEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

LocalAI embedding models.

Since LocalAI and OpenAI have 1:1 compatibility between APIs, this class uses the `openai` Python package’s `openai.Embedding` as its client. Thus, you should have the `openai` python package installed, and defeat the environment variable `OPENAI_API_KEY` by setting to a random string. You also need to specify `OPENAI_API_BASE` to point to your LocalAI service endpoint.

Example               from langchain_community.embeddings import LocalAIEmbeddings     openai = LocalAIEmbeddings(         openai_api_key="random-string",         openai_api_base="http://localhost:8080"     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allowed\_special _: Literal\['all'\] | Set\[str\]__ = \{\}_\#     

_param _chunk\_size _: int_ _ = 1000_\#     

Maximum number of texts to embed in each batch

_param _deployment _: str_ _ = 'text-embedding-ada-002'_\#     

_param _disallowed\_special _: Literal\['all'\] | Set\[str\] | Sequence\[str\]__ = 'all'_\#     

_param _embedding\_ctx\_length _: int_ _ = 8191_\#     

The maximum number of tokens to embed at once.

_param _headers _: Any_ _ = None_\#     

_param _max\_retries _: int_ _ = 6_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _ = 'text-embedding-ada-002'_\#     

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Holds any model parameters valid for create call not explicitly specified.

_param _openai\_api\_base _: str | None_ _ = None_\#     

_param _openai\_api\_key _: str | None_ _ = None_\#     

_param _openai\_api\_version _: str | None_ _ = None_\#     

_param _openai\_organization _: str | None_ _ = None_\#     

_param _openai\_proxy _: str | None_ _ = None_\#     

_param _request\_timeout _: float | Tuple\[float, float\] | None_ _ = None_\#     

Timeout in seconds for the LocalAI request.

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a progress bar when embedding.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/localai.html#LocalAIEmbeddings.validate_environment)\#     

Validate that api key and python package exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

_async _aembed\_documents\(

    _texts : List\[str\]_,     _chunk\_size : int | None = 0_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/localai.html#LocalAIEmbeddings.aembed_documents)\#     

Call out to LocalAI’s embedding endpoint async for embedding search docs.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

  * **chunk\_size** \(_int_ _|__None_\) – The chunk size of embeddings. If None, will use the chunk size specified by the class.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/localai.html#LocalAIEmbeddings.aembed_query)\#     

Call out to LocalAI’s embedding endpoint async for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_,     _chunk\_size : int | None = 0_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/localai.html#LocalAIEmbeddings.embed_documents)\#     

Call out to LocalAI’s embedding endpoint for embedding search docs.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

  * **chunk\_size** \(_int_ _|__None_\) – The chunk size of embeddings. If None, will use the chunk size specified by the class.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/localai.html#LocalAIEmbeddings.embed_query)\#     

Call out to LocalAI’s embedding endpoint for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

Examples using LocalAIEmbeddings

  * [LocalAI](https://python.langchain.com/docs/integrations/text_embedding/localai/)

__On this page