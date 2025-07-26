# EmbeddingsVectorizer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/redis/cache/langchain_redis.cache.EmbeddingsVectorizer.html
**Word Count:** 314
**Links Count:** 104
**Scraped:** 2025-07-21 08:27:44
**Status:** completed

---

# EmbeddingsVectorizer\#

_class _langchain\_redis.cache.EmbeddingsVectorizer[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#EmbeddingsVectorizer)\#     

Bases: `BaseVectorizer`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _cache _: EmbeddingsCache | None_ _ = None_\#     

_param _dims _: Annotated\[int | None, Field\(strict=True, gt=0\)\]__ = None_\#     

Constraints:     

  * **strict** = True

  * **gt** = 0

_param _dtype _: str_ _ = 'float32'_\#     

_param _embeddings _: [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_ _\[Required\]_\#     

_param _model _: str_ _ = 'custom\_embeddings'_\#     

_async _aembed\(

    _text : str_,     _dtype : str | VectorDataType = 'float32'_,     _\*\* kwargs: Any_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#EmbeddingsVectorizer.aembed)\#     

Asynchronously generate a vector embedding for a text string.

Parameters:     

  * **text** \(_str_\) – The text to convert to a vector embedding

  * **preprocess** – Function to apply to the text before embedding

  * **as\_buffer** – Return the embedding as a binary buffer instead of a list

  * **skip\_cache** – Bypass the cache for this request

  * **\*\*kwargs** \(_Any_\) – Additional model-specific parameters

  * **dtype** \(_str_ _|__VectorDataType_\)

  * **\*\*kwargs**

Returns:     

The vector embedding as either a list of floats or binary buffer

Return type:     

_List_\[float\]

Examples               >>> embedding = await vectorizer.aembed("Hello world")     

_async _aembed\_many\(

    _texts : List\[str\]_,     _dtype : str | VectorDataType = 'float32'_,     _\*\* kwargs: Any_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#EmbeddingsVectorizer.aembed_many)\#     

Asynchronously generate vector embeddings for multiple texts efficiently.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of texts to convert to vector embeddings

  * **preprocess** – Function to apply to each text before embedding

  * **batch\_size** – Number of texts to process in each API call

  * **as\_buffer** – Return embeddings as binary buffers instead of lists

  * **skip\_cache** – Bypass the cache for this request

  * **\*\*kwargs** \(_Any_\) – Additional model-specific parameters

  * **dtype** \(_str_ _|__VectorDataType_\)

  * **\*\*kwargs**

Returns:     

List of vector embeddings in the same order as the input texts

Return type:     

_List_\[_List_\[float\]\]

Examples               >>> embeddings = await vectorizer.aembed_many(["Hello", "World"], batch_size=2)     

batchify\(

    _seq : list_,     _size : int_,     _preprocess : Callable | None = None_, \)\#     

Split a sequence into batches of specified size.

Parameters:     

  * **seq** \(_list_\) – Sequence to split into batches

  * **size** \(_int_\) – Batch size

  * **preprocess** \(_Callable_ _|__None_\) – Optional function to preprocess each item

Yields:     

Batches of the sequence

embed\(

    _text : str_,     _dtype : str | VectorDataType = 'float32'_,     _\*\* kwargs: Any_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#EmbeddingsVectorizer.embed)\#     

Generate a vector embedding for a text string.

Parameters:     

  * **text** \(_str_\) – The text to convert to a vector embedding

  * **preprocess** – Function to apply to the text before embedding

  * **as\_buffer** – Return the embedding as a binary buffer instead of a list

  * **skip\_cache** – Bypass the cache for this request

  * **\*\*kwargs** \(_Any_\) – Additional model-specific parameters

  * **dtype** \(_str_ _|__VectorDataType_\)

  * **\*\*kwargs**

Returns:     

The vector embedding as either a list of floats or binary buffer

Return type:     

_List_\[float\]

Examples               >>> embedding = vectorizer.embed("Hello world")     

embed\_many\(

    _texts : List\[str\]_,     _dtype : str | VectorDataType = 'float32'_,     _\*\* kwargs: Any_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#EmbeddingsVectorizer.embed_many)\#     

Generate vector embeddings for multiple texts efficiently.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of texts to convert to vector embeddings

  * **preprocess** – Function to apply to each text before embedding

  * **batch\_size** – Number of texts to process in each API call

  * **as\_buffer** – Return embeddings as binary buffers instead of lists

  * **skip\_cache** – Bypass the cache for this request

  * **\*\*kwargs** \(_Any_\) – Additional model-specific parameters

  * **dtype** \(_str_ _|__VectorDataType_\)

  * **\*\*kwargs**

Returns:     

List of vector embeddings in the same order as the input texts

Return type:     

_List_\[_List_\[float\]\]

Examples               >>> embeddings = vectorizer.embed_many(["Hello", "World"], batch_size=2)     

encode\(

    _texts : str | List\[str\]_,     _dtype : str | VectorDataType_,     _\*\* kwargs: Any_, \) → ndarray[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#EmbeddingsVectorizer.encode)\#     

Parameters:     

  * **texts** \(_str_ _|__List_ _\[__str_ _\]_\)

  * **dtype** \(_str_ _|__VectorDataType_\)

  * **kwargs** \(_Any_\)

Return type:     

_ndarray_

_property _type _: str_\#     

Return the type of vectorizer.

__On this page