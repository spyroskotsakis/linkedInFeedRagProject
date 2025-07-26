# TogetherEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/together/embeddings/langchain_together.embeddings.TogetherEmbeddings.html
**Word Count:** 324
**Links Count:** 119
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# TogetherEmbeddings\#

_class _langchain\_together.embeddings.TogetherEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_together/embeddings.html#TogetherEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Together embedding model integration.

Setup:     

Install `langchain_together` and set environment variable `TOGETHER_API_KEY`.               pip install -U langchain_together     export TOGETHER_API_KEY="your-api-key"     

Key init args — completion params:     

model: str     

Name of Together model to use.

Key init args — client params:     

api\_key: Optional\[SecretStr\]

See full list of supported init args and their descriptions in the params section.

Instantiate:                    from __module_name__ import TogetherEmbeddings          embed = TogetherEmbeddings(         model="togethercomputer/m2-bert-80M-8k-retrieval",         # api_key="...",         # other params...     )     

Embed single text:                    input_text = "The meaning of life is 42"     vector = embed.embed_query(input_text)     print(vector[:3])                    [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915]     

Embed multiple texts:                     input_texts = ["Document 1...", "Document 2..."]     vectors = embed.embed_documents(input_texts)     print(len(vectors))     # The first 3 coordinates for the first vector     print(vectors[0][:3])                    2     [-0.024603435769677162, -0.007543657906353474, 0.0039630369283258915]     

Async:                     vector = await embed.aembed_query(input_text)     print(vector[:3])           # multiple:      # await embed.aembed_documents(input_texts)                    [-0.009100092574954033, 0.005071679595857859, -0.0029193938244134188]     

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

_param _embedding\_ctx\_length _: int_ _ = 4096_\#     

The maximum number of tokens to embed at once.

Not yet supported.

_param _http\_async\_client _: Any | None_ _ = None_\#     

Optional httpx.AsyncClient. Only used for async invocations. Must specify http\_client as well if you’d like a custom client for sync invocations.

_param _http\_client _: Any | None_ _ = None_\#     

Optional httpx.Client. Only used for sync invocations. Must specify http\_async\_client as well if you’d like a custom client for async invocations.

_param _max\_retries _: int_ _ = 2_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _ = 'togethercomputer/m2-bert-80M-8k-retrieval'_\#     

Embeddings model name to use. Instead, use ‘togethercomputer/m2-bert-80M-8k-retrieval’ for example.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Holds any model parameters valid for create call not explicitly specified.

_param _request\_timeout _: float | Tuple\[float, float\] | Any | None_ _ = None_ _\(alias 'timeout'\)_\#     

Timeout for requests to Together embedding API. Can be float, httpx.Timeout or None.

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a progress bar when embedding.

Not yet supported.

_param _skip\_empty _: bool_ _ = False_\#     

Whether to skip empty strings when embedding or raise an error. Defaults to not skipping.

Not yet supported.

_param _together\_api\_base _: str_ _\[Optional\]__\(alias 'base\_url'\)_\#     

Endpoint URL to use.

_param _together\_api\_key _: SecretStr | None_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Together AI API key.

Automatically read from env variable TOGETHER\_API\_KEY if not provided.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_together/embeddings.html#TogetherEmbeddings.aembed_documents)\#     

Embed a list of document texts using passage model asynchronously.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_together/embeddings.html#TogetherEmbeddings.aembed_query)\#     

Asynchronous Embed query text using query model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_together/embeddings.html#TogetherEmbeddings.embed_documents)\#     

Embed a list of document texts using passage model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_together/embeddings.html#TogetherEmbeddings.embed_query)\#     

Embed query text using query model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

Examples using TogetherEmbeddings

  * [TogetherEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/together/)

__On this page