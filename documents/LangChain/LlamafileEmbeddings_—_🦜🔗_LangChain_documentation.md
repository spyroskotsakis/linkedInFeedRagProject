# LlamafileEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.llamafile.LlamafileEmbeddings.html
**Word Count:** 201
**Links Count:** 224
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# LlamafileEmbeddings\#

_class _langchain\_community.embeddings.llamafile.LlamafileEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llamafile.html#LlamafileEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Llamafile lets you distribute and run large language models with a single file.

To get started, see: [Mozilla-Ocho/llamafile](https://github.com/Mozilla-Ocho/llamafile)

To use this class, you will need to first:

  1. Download a llamafile.

  2. Make the downloaded file executable: chmod +x path/to/model.llamafile

  3. Start the llamafile in server mode with embeddings enabled:

> ./path/to/model.llamafile –server –nobrowser –embedding

Example               from langchain_community.embeddings import LlamafileEmbeddings     embedder = LlamafileEmbeddings()     doc_embeddings = embedder.embed_documents(         [             "Alpha is the first letter of the Greek alphabet",             "Beta is the second letter of the Greek alphabet",         ]     )     query_embedding = embedder.embed_query(         "What is the second letter of the Greek alphabet"     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _base\_url _: str_ _ = 'http://localhost:8080'_\#     

Base url where the llamafile server is listening.

_param _request\_timeout _: int | None_ _ = None_\#     

Timeout for server requests

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llamafile.html#LlamafileEmbeddings.embed_documents)\#     

Embed documents using a llamafile server running at self.base\_url. llamafile server should be started in a separate process before invoking this method.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/llamafile.html#LlamafileEmbeddings.embed_query)\#     

Embed a query using a llamafile server running at self.base\_url. llamafile server should be started in a separate process before invoking this method.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using LlamafileEmbeddings

  * [llamafile](https://python.langchain.com/docs/integrations/text_embedding/llamafile/)

__On this page