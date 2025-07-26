# LaserEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.laser.LaserEmbeddings.html
**Word Count:** 197
**Links Count:** 229
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# LaserEmbeddings\#

_class _langchain\_community.embeddings.laser.LaserEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/laser.html#LaserEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

LASER Language-Agnostic SEntence Representations. LASER is a Python library developed by the Meta AI Research team and used for creating multilingual sentence embeddings for over 147 languages as of 2/25/2024 See more documentation at: \* [facebookresearch/LASER](https://github.com/facebookresearch/LASER/) \* [facebookresearch/LASER](https://github.com/facebookresearch/LASER/tree/main/laser_encoders) \* <https://arxiv.org/abs/2205.12654>

To use this class, you must install the laser\_encoders Python package.

pip install laser\_encoders .. rubric:: Example

from laser\_encoders import LaserEncoderPipeline encoder = LaserEncoderPipeline\(lang=”eng\_Latn”\) embeddings = encoder.encode\_sentences\(\[“Hello”, “World”\]\)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _lang _: str | None_ _ = None_\#     

The language or language code you’d like to use If empty, this implementation will default to using a multilingual earlier LASER encoder model \(called laser2\) Find the list of supported languages at [facebookresearch/flores](https://github.com/facebookresearch/flores/blob/main/flores200/README.md#languages-in-flores-200)

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/laser.html#LaserEmbeddings.validate_environment)\#     

Validate that laser\_encoders has been installed.

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/laser.html#LaserEmbeddings.embed_documents)\#     

Generate embeddings for documents using LASER.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/laser.html#LaserEmbeddings.embed_query)\#     

Generate single query text embeddings using LASER.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using LaserEmbeddings

  * [Facebook - Meta](https://python.langchain.com/docs/integrations/providers/facebook/)

  * [LASER Language-Agnostic SEntence Representations Embeddings by Meta AI](https://python.langchain.com/docs/integrations/text_embedding/laser/)

__On this page