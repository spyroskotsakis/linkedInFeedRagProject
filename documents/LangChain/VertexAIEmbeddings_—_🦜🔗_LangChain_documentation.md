# VertexAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.vertexai.VertexAIEmbeddings.html
**Word Count:** 333
**Links Count:** 256
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# VertexAIEmbeddings\#

_class _langchain\_community.embeddings.vertexai.VertexAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/vertexai.html#VertexAIEmbeddings)\#     

Bases: `_VertexAICommon`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.0.12: Use `:class:`~langchain_google_vertexai.VertexAIEmbeddings`` instead. It will not be removed until langchain-community==1.0.

Google Cloud VertexAI embedding models.

Initialize the sentence\_transformer.

_param _credentials _: Any_ _ = None_\#     

The default custom credentials \(google.auth.credentials.Credentials\) to use

_param _location _: str_ _ = 'us-central1'_\#     

The default location to use when making API calls.

_param _max\_output\_tokens _: int_ _ = 128_\#     

Token limit determines the maximum amount of text output from one prompt.

_param _max\_retries _: int_ _ = 6_\#     

The maximum number of retries to make when generating.

_param _model\_name _: str_ _\[Required\]_\#     

Underlying model name.

_param _n _: int_ _ = 1_\#     

How many completions to generate for each prompt.

_param _project _: str | None_ _ = None_\#     

The default GCP project to use when making Vertex API calls.

_param _request\_parallelism _: int_ _ = 5_\#     

The amount of parallelism allowed for requests issued to VertexAI models.

_param _show\_progress\_bar _: bool_ _ = False_\#     

Whether to show a tqdm progress bar. Must have tqdm installed.

_param _stop _: List\[str\] | None_ _ = None_\#     

Optional list of stop words to use when generating.

_param _streaming _: bool_ _ = False_\#     

Whether to stream the results or not.

_param _temperature _: float_ _ = 0.0_\#     

Sampling temperature, it controls the degree of randomness in token selection.

_param _top\_k _: int_ _ = 40_\#     

How the model selects tokens for output, the next token is selected from

_param _top\_p _: float_ _ = 0.95_\#     

Tokens are selected from most probable to least until the sum of their

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/vertexai.html#VertexAIEmbeddings.validate_environment)\#     

Validates that the python package exists in environment.

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

embed\(

    _texts : List\[str\]_,     _batch\_size : int = 0_,     _embeddings\_task\_type : Literal\['RETRIEVAL\_QUERY', 'RETRIEVAL\_DOCUMENT', 'SEMANTIC\_SIMILARITY', 'CLASSIFICATION', 'CLUSTERING'\] | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/vertexai.html#VertexAIEmbeddings.embed)\#     

Embed a list of strings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List\[str\] The list of strings to embed.

  * **batch\_size** \(_int_\) – \[int\] The batch size of embeddings to send to the model. If zero, then the largest batch size will be detected dynamically at the first request, starting from 250, down to 5.

  * **embeddings\_task\_type** \(_Literal_ _\[__'RETRIEVAL\_QUERY'__,__'RETRIEVAL\_DOCUMENT'__,__'SEMANTIC\_SIMILARITY'__,__'CLASSIFICATION'__,__'CLUSTERING'__\]__|__None_\) – 

\[str\] optional embeddings task type, one of the following

> RETRIEVAL\_QUERY - Text is a query >      >  > in a search/retrieval setting. >  > RETRIEVAL\_DOCUMENT - Text is a document >      >  > in a search/retrieval setting. >  > SEMANTIC\_SIMILARITY - Embeddings will be used >      >  > for Semantic Textual Similarity \(STS\). >  > CLASSIFICATION - Embeddings will be used for classification. CLUSTERING - Embeddings will be used for clustering.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_documents\(

    _texts : List\[str\]_,     _batch\_size : int = 0_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/vertexai.html#VertexAIEmbeddings.embed_documents)\#     

Embed a list of documents.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List\[str\] The list of texts to embed.

  * **batch\_size** \(_int_\) – \[int\] The batch size of embeddings to send to the model. If zero, then the largest batch size will be detected dynamically at the first request, starting from 250, down to 5.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/vertexai.html#VertexAIEmbeddings.embed_query)\#     

Embed a text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

_property _is\_codey\_model _: bool_\#     

task\_executor _: ClassVar\[Executor | None\]__ = FieldInfo\(annotation=NoneType, required=False, default=None, exclude=True\)_\#     

__On this page