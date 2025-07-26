# OpenCLIPEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/open_clip/langchain_experimental.open_clip.open_clip.OpenCLIPEmbeddings.html
**Word Count:** 82
**Links Count:** 122
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# OpenCLIPEmbeddings\#

_class _langchain\_experimental.open\_clip.open\_clip.OpenCLIPEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/open_clip/open_clip.html#OpenCLIPEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

OpenCLIP Embeddings model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _checkpoint _: str_ _ = 'laion2b\_s32b\_b79k'_\#     

_param _model _: Any_ _\[Required\]_\#     

_param _model\_name _: str_ _ = 'ViT-H-14'_\#     

_param _preprocess _: Any_ _\[Required\]_\#     

_param _tokenizer _: Any_ _\[Required\]_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/open_clip/open_clip.html#OpenCLIPEmbeddings.embed_documents)\#     

Embed search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

_List_\[_List_\[float\]\]

embed\_image\(

    _uris : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/open_clip/open_clip.html#OpenCLIPEmbeddings.embed_image)\#     

Parameters:     

**uris** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/open_clip/open_clip.html#OpenCLIPEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

Examples using OpenCLIPEmbeddings

  * [LanceDB](https://python.langchain.com/docs/integrations/vectorstores/lancedb/)

  * [OpenClip](https://python.langchain.com/docs/integrations/text_embedding/open_clip/)

  * [SingleStoreDB](https://python.langchain.com/docs/integrations/vectorstores/singlestoredb/)

__On this page