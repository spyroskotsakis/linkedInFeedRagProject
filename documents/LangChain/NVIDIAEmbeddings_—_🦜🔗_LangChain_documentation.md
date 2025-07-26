# NVIDIAEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/nvidia_ai_endpoints/embeddings/langchain_nvidia_ai_endpoints.embeddings.NVIDIAEmbeddings.html
**Word Count:** 322
**Links Count:** 100
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# NVIDIAEmbeddings\#

_class _langchain\_nvidia\_ai\_endpoints.embeddings.NVIDIAEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/embeddings.html#NVIDIAEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Client to NVIDIA embeddings models.

Fields: \- model: str, the name of the model to use \- truncate: “NONE”, “START”, “END”, truncate input text if it exceeds the model’s

> maximum token length. Default is “NONE”, which raises an error if an input is too long.

  * dimensions: int, the number of dimensions for the embeddings. This parameter is     

not supported by all models.

Create a new NVIDIAEmbeddings embedder.

This class provides access to a NVIDIA NIM for embedding. By default, it connects to a hosted NIM, but can be configured to connect to a local NIM using the base\_url parameter. An API key is required to connect to the hosted NIM.

Parameters:     

  * **model** \(_str_\) – The model to use for embedding.

  * **nvidia\_api\_key** \(_str_\) – The API key to use for connecting to the hosted NIM.

  * **api\_key** \(_str_\) – Alternative to nvidia\_api\_key.

  * **base\_url** \(_str_\) – The base URL of the NIM to connect to. Format for base URL is <http://host:port>

  * **trucate** \(_str_\) – “NONE”, “START”, “END”, truncate input text if it exceeds the model’s context length. Default is “NONE”, which raises an error if an input is too long.

  * **dimensions** \(_int_\) – The number of dimensions for the embeddings. This parameter is not supported by all models.

API Key: \- The recommended way to provide the API key is through the NVIDIA\_API\_KEY

> environment variable.

Base URL: \- Connect to a self-hosted model with NVIDIA NIM using the base\_url arg to

> link to the local host at localhost:8000: embedder = NVIDIAEmbeddings\(base\_url=”http://localhost:8080/v1”\)

_param _base\_url _: str | None_ _ = None_\#     

Base url for model listing an invocation

_param _dimensions _: int | None_ _ = None_\#     

The number of dimensions for the embeddings. This parameter is not supported by all models.

_param _max\_batch\_size _: int_ _ = 50_\#     

_param _model _: str | None_ _ = None_\#     

Name of the model to invoke

_param _truncate _: Literal\['NONE', 'START', 'END'\]__ = 'NONE'_\#     

Truncate input text if it exceeds the model’s maximum token length. Default is ‘NONE’, which raises an error if an input is too long.

_classmethod _get\_available\_models\(

    _\*\* kwargs: Any_, \) → List\[Model\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/embeddings.html#NVIDIAEmbeddings.get_available_models)\#     

Get a list of available models that work with NVIDIAEmbeddings.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

_List_\[_Model_\]

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/embeddings.html#NVIDIAEmbeddings.embed_documents)\#     

Input pathway for document embeddings.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/embeddings.html#NVIDIAEmbeddings.embed_query)\#     

Input pathway for query embeddings.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

_property _available\_models _: List\[Model\]_\#     

Get a list of available models that work with NVIDIAEmbeddings.

__On this page