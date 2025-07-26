# FastEmbedEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.fastembed.FastEmbedEmbeddings.html
**Word Count:** 263
**Links Count:** 244
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# FastEmbedEmbeddings\#

_class _langchain\_community.embeddings.fastembed.FastEmbedEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/fastembed.html#FastEmbedEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Qdrant FastEmbedding models.

FastEmbed is a lightweight, fast, Python library built for embedding generation. See more documentation at: \* [qdrant/fastembed](https://github.com/qdrant/fastembed/) \* <https://qdrant.github.io/fastembed/>

To use this class, you must install the fastembed Python package.

pip install fastembed .. rubric:: Example

from langchain\_community.embeddings import FastEmbedEmbeddings fastembed = FastEmbedEmbeddings\(\)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _batch\_size _: int_ _ = 256_\#     

Batch size for encoding. Higher values will use more memory, but be faster. Defaults to 256.

_param _cache\_dir _: str | None_ _ = None_\#     

The path to the cache directory. Defaults to local\_cache in the parent directory

_param _doc\_embed\_type _: Literal\['default', 'passage'\]__ = 'default'_\#     

Type of embedding to use for documents The available options are: “default” and “passage”

_param _max\_length _: int_ _ = 512_\#     

The maximum number of tokens. Defaults to 512. Unknown behavior for values > 512.

_param _model _: Any_ _ = None_\#     

_param _model\_name _: str_ _ = 'BAAI/bge-small-en-v1.5'_\#     

Name of the FastEmbedding model to use Defaults to “BAAI/bge-small-en-v1.5” Find the list of supported models at <https://qdrant.github.io/fastembed/examples/Supported_Models/>

_param _parallel _: int | None_ _ = None_\#     

If >1, parallel encoding is used, recommended for encoding of large datasets. If 0, use all available cores. If None, don’t use data-parallel processing, use default onnxruntime threading. Defaults to None.

_param _providers _: Sequence\[Any\] | None_ _ = None_\#     

List of ONNX execution providers. Use \[“CUDAExecutionProvider”\] to enable the use of GPU when generating embeddings. This requires to install fastembed-gpu instead of fastembed. See <https://qdrant.github.io/fastembed/examples/FastEmbed_GPU> for more details. Defaults to None.

_param _threads _: int | None_ _ = None_\#     

The number of threads single onnxruntime session can use. Defaults to None

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/fastembed.html#FastEmbedEmbeddings.validate_environment)\#     

Validate that FastEmbed has been installed.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/fastembed.html#FastEmbedEmbeddings.embed_documents)\#     

Generate embeddings for documents using FastEmbed.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/fastembed.html#FastEmbedEmbeddings.embed_query)\#     

Generate query embeddings using FastEmbed.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using FastEmbedEmbeddings

  * [FastEmbed by Qdrant](https://python.langchain.com/docs/integrations/text_embedding/fastembed/)

__On this page