# OracleEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.oracleai.OracleEmbeddings.html
**Word Count:** 132
**Links Count:** 229
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# OracleEmbeddings\#

_class _langchain\_community.embeddings.oracleai.OracleEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/oracleai.html#OracleEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Get Embeddings

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _conn _: Any_ _ = None_\#     

Embedding Parameters

_param _params _: Dict\[str, Any\]__\[Required\]_\#     

Proxy

_param _proxy _: str | None_ _ = None_\#     

_static _load\_onnx\_model\(

    _conn : Connection_,     _dir : str_,     _onnx\_file : str_,     _model\_name : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/oracleai.html#OracleEmbeddings.load_onnx_model)\#     

Load an ONNX model to Oracle Database. :param conn: Oracle Connection, :param dir: Oracle Directory, :param onnx\_file: ONNX file name, :param model\_name: Name of the model.

Parameters:     

  * **conn** \(_Connection_\)

  * **dir** \(_str_\)

  * **onnx\_file** \(_str_\)

  * **model\_name** \(_str_\)

Return type:     

None

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/oracleai.html#OracleEmbeddings.embed_documents)\#     

Compute doc embeddings using an OracleEmbeddings. :param texts: The list of texts to embed.

Returns:     

List of embeddings, one for each input text.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/oracleai.html#OracleEmbeddings.embed_query)\#     

Compute query embedding using an OracleEmbeddings. :param text: The text to embed.

Returns:     

Embedding for the text.

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[float\]

Examples using OracleEmbeddings

  * [Oracle AI Vector Search: Generate Embeddings](https://python.langchain.com/docs/integrations/text_embedding/oracleai/)

  * [OracleAI Vector Search](https://python.langchain.com/docs/integrations/providers/oracleai/)

__On this page