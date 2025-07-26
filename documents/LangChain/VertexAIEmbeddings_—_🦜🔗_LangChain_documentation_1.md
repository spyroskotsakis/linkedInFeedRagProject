# VertexAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/embeddings/langchain_google_vertexai.embeddings.VertexAIEmbeddings.html
**Word Count:** 533
**Links Count:** 171
**Scraped:** 2025-07-21 08:27:18
**Status:** completed

---

# VertexAIEmbeddings\#

_class _langchain\_google\_vertexai.embeddings.VertexAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/embeddings.html#VertexAIEmbeddings)\#     

Bases: `_VertexAICommon`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Google Cloud VertexAI embedding models.

Initialize the sentence\_transformer.

_param _additional\_headers _: Dict\[str, str\] | None_ _ = None_\#     

A key-value dictionary representing additional headers for the model call

_param _api\_endpoint _: str | None_ _ = None_ _\(alias 'base\_url'\)_\#     

Desired API endpoint, e.g., us-central1-aiplatform.googleapis.com

_param _api\_transport _: str | None_ _ = None_\#     

The desired API transport method, can be either ‘grpc’ or ‘rest’. Uses the default parameter in vertexai.init if defined.

_param _audio\_timestamp _: bool | None_ _ = None_\#     

Enable timestamp understanding of audio-only files

_param _client\_cert\_source _: Callable\[\[\], Tuple\[bytes, bytes\]\] | None_ _ = None_\#     

A callback which returns client certificate bytes and private key bytes both

_param _credentials _: Any_ _ = None_\#     

The default custom credentials \(google.auth.credentials.Credentials\) to use

_param _endpoint\_version _: Literal\['v1', 'v1beta1'\]__ = 'v1beta1'_\#     

Whether to use v1 or v1beta1 endpoint.

v1 is more performant, but v1beta1 might have some new features.

_param _frequency\_penalty _: float | None_ _ = None_\#     

Positive values penalize tokens that repeatedly appear in the generated text,

_param _full\_model\_name _: str | None_ _ = None_\#     

The full name of the model’s endpoint.

_param _include\_thoughts _: bool | None_ _ = None_\#     

Indicates whether to include thoughts in the response.

_param _location _: str_ _ = 'us-central1'_\#     

The default location to use when making API calls.

_param _max\_output\_tokens _: int | None_ _ = None_ _\(alias 'max\_tokens'\)_\#     

Token limit determines the maximum amount of text output from one prompt.

_param _max\_retries _: int_ _ = 6_\#     

The maximum number of retries to make when generating.

_param _model\_name _: str | None_ _ = None_ _\(alias 'model'\)_\#     

Underlying model name.

_param _n _: int_ _ = 1_\#     

How many completions to generate for each prompt.

_param _presence\_penalty _: float | None_ _ = None_\#     

Positive values penalize tokens that already appear in the generated text,

_param _project _: str | None_ _ = None_\#     

The default GCP project to use when making Vertex API calls.

_param _request\_parallelism _: int_ _ = 5_\#     

The amount of parallelism allowed for requests issued to VertexAI models.

_param _safety\_settings _: 'SafetySettingsType' | None_ _ = None_\#     

The default safety settings to use for all generations.

For example:

> from langchain\_google\_vertexai import HarmBlockThreshold, HarmCategory >  > safety\_settings = \{ >      >  > HarmCategory.HARM\_CATEGORY\_UNSPECIFIED: HarmBlockThreshold.BLOCK\_NONE, HarmCategory.HARM\_CATEGORY\_DANGEROUS\_CONTENT: HarmBlockThreshold.BLOCK\_MEDIUM\_AND\_ABOVE, HarmCategory.HARM\_CATEGORY\_HATE\_SPEECH: HarmBlockThreshold.BLOCK\_ONLY\_HIGH, HarmCategory.HARM\_CATEGORY\_HARASSMENT: HarmBlockThreshold.BLOCK\_LOW\_AND\_ABOVE, HarmCategory.HARM\_CATEGORY\_SEXUALLY\_EXPLICIT: HarmBlockThreshold.BLOCK\_NONE, >  > \}

_param _seed _: int | None_ _ = None_\#     

Random seed for the generation.

_param _stop _: List\[str\] | None_ _ = None_ _\(alias 'stop\_sequences'\)_\#     

Optional list of stop words to use when generating.

_param _streaming _: bool_ _ = False_\#     

Whether to stream the results or not.

_param _temperature _: float | None_ _ = None_\#     

Sampling temperature, it controls the degree of randomness in token selection.

_param _thinking\_budget _: int | None_ _ = None_\#     

Indicates the thinking budget in tokens.

_param _top\_k _: int | None_ _ = None_\#     

How the model selects tokens for output, the next token is selected from

_param _top\_p _: float | None_ _ = None_\#     

Tokens are selected from most probable to least until the sum of their

_param _tuned\_model\_name _: str | None_ _ = None_\#     

The name of a tuned model.

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

    _texts : List\[str\]_,     _batch\_size : int = 0_,     _embeddings\_task\_type : Literal\['RETRIEVAL\_QUERY', 'RETRIEVAL\_DOCUMENT', 'SEMANTIC\_SIMILARITY', 'CLASSIFICATION', 'CLUSTERING', 'QUESTION\_ANSWERING', 'FACT\_VERIFICATION', 'CODE\_RETRIEVAL\_QUERY'\] | None = None_,     _dimensions : int | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/embeddings.html#VertexAIEmbeddings.embed)\#     

Embed a list of strings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List\[str\] The list of strings to embed.

  * **batch\_size** \(_int_\) – \[int\] The batch size of embeddings to send to the model. If zero, then the largest batch size will be detected dynamically at the first request, starting from 250, down to 5.

  * **embeddings\_task\_type** \(_Literal_ _\[__'RETRIEVAL\_QUERY'__,__'RETRIEVAL\_DOCUMENT'__,__'SEMANTIC\_SIMILARITY'__,__'CLASSIFICATION'__,__'CLUSTERING'__,__'QUESTION\_ANSWERING'__,__'FACT\_VERIFICATION'__,__'CODE\_RETRIEVAL\_QUERY'__\]__|__None_\) – 

\[str\] optional embeddings task type, one of the following

> RETRIEVAL\_QUERY - Text is a query >      >  > in a search/retrieval setting. >  > RETRIEVAL\_DOCUMENT - Text is a document >      >  > in a search/retrieval setting. >  > SEMANTIC\_SIMILARITY - Embeddings will be used >      >  > for Semantic Textual Similarity \(STS\). >  > CLASSIFICATION - Embeddings will be used for classification. CLUSTERING - Embeddings will be used for clustering. CODE\_RETRIEVAL\_QUERY - Embeddings will be used for >
>> code retrieval for Java and Python. >  > The following are only supported on preview models: QUESTION\_ANSWERING FACT\_VERIFICATION

  * **dimensions** \(_int_ _|__None_\) – \[int\] optional. Output embeddings dimensions. Only supported on preview models.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_documents\(

    _texts : List\[str\]_,     _batch\_size : int = 0_,     _\*_ ,     _embeddings\_task\_type : Literal\['RETRIEVAL\_QUERY', 'RETRIEVAL\_DOCUMENT', 'SEMANTIC\_SIMILARITY', 'CLASSIFICATION', 'CLUSTERING', 'QUESTION\_ANSWERING', 'FACT\_VERIFICATION', 'CODE\_RETRIEVAL\_QUERY'\] = 'RETRIEVAL\_DOCUMENT'_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/embeddings.html#VertexAIEmbeddings.embed_documents)\#     

Embed a list of documents.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List\[str\] The list of texts to embed.

  * **batch\_size** \(_int_\) – \[int\] The batch size of embeddings to send to the model. If zero, then the largest batch size will be detected dynamically at the first request, starting from 250, down to 5.

  * **embeddings\_task\_type** \(_Literal_ _\[__'RETRIEVAL\_QUERY'__,__'RETRIEVAL\_DOCUMENT'__,__'SEMANTIC\_SIMILARITY'__,__'CLASSIFICATION'__,__'CLUSTERING'__,__'QUESTION\_ANSWERING'__,__'FACT\_VERIFICATION'__,__'CODE\_RETRIEVAL\_QUERY'__\]_\)

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_image\(

    _image\_path : str_,     _contextual\_text : str | None = None_,     _dimensions : int | None = None_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/embeddings.html#VertexAIEmbeddings.embed_image)\#     

Deprecated since version 2.0.1: Use `embed_images()` instead. It will be removed in langchain-google-vertexai==3.0.0.

Embed an image.

Parameters:     

  * **image\_path** \(_str_\) – Path to image \(Google Cloud Storage or web\) to generate

  * **for.** \(_embeddings_\)

  * **contextual\_text** \(_str_ _|__None_\) – Text to generate embeddings for.

  * **dimensions** \(_int_ _|__None_\)

Returns:     

Embedding for the image.

Return type:     

_List_\[float\]

embed\_images\(

    _uris : List\[str\]_,     _contextual\_text : str | None = None_,     _dimensions : int | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/embeddings.html#VertexAIEmbeddings.embed_images)\#     

Embed a list of images.

Parameters:     

  * **uris** \(_List_ _\[__str_ _\]_\) – Paths to image \(local, Google Cloud Storage or web\) to generate

  * **for.** \(_embeddings_\)

  * **contextual\_text** \(_str_ _|__None_\) – Text to generate embeddings for.

  * **dimensions** \(_int_ _|__None_\)

Returns:     

Embedding for the image.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_,     _\*_ ,     _embeddings\_task\_type : Literal\['RETRIEVAL\_QUERY', 'RETRIEVAL\_DOCUMENT', 'SEMANTIC\_SIMILARITY', 'CLASSIFICATION', 'CLUSTERING', 'QUESTION\_ANSWERING', 'FACT\_VERIFICATION', 'CODE\_RETRIEVAL\_QUERY'\] = 'RETRIEVAL\_QUERY'_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/embeddings.html#VertexAIEmbeddings.embed_query)\#     

Embed a text.

Parameters:     

  * **text** \(_str_\) – The text to embed.

  * **embeddings\_task\_type** \(_Literal_ _\[__'RETRIEVAL\_QUERY'__,__'RETRIEVAL\_DOCUMENT'__,__'SEMANTIC\_SIMILARITY'__,__'CLASSIFICATION'__,__'CLUSTERING'__,__'QUESTION\_ANSWERING'__,__'FACT\_VERIFICATION'__,__'CODE\_RETRIEVAL\_QUERY'__\]_\)

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

_property _async\_prediction\_client _: PredictionServiceAsyncClient | PredictionServiceAsyncClient_\#     

Returns PredictionServiceClient.

_property _max\_tokens _: int | None_\#     

_property _model\_type _: str_\#     

_property _model\_version _: [GoogleEmbeddingModelVersion](https://python.langchain.com/api_reference/google_vertexai/embeddings/langchain_google_vertexai.embeddings.GoogleEmbeddingModelVersion.html#langchain_google_vertexai.embeddings.GoogleEmbeddingModelVersion "langchain_google_vertexai.embeddings.GoogleEmbeddingModelVersion")_\#     

_property _prediction\_client _: PredictionServiceClient | PredictionServiceClient_\#     

Returns PredictionServiceClient.

task\_executor _: ClassVar\[Executor | None\]__ = FieldInfo\(annotation=NoneType, required=False, default=None, exclude=True\)_\#     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)