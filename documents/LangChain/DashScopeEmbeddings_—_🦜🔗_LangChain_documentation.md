# DashScopeEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.dashscope.DashScopeEmbeddings.html
**Word Count:** 146
**Links Count:** 229
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# DashScopeEmbeddings\#

_class _langchain\_community.embeddings.dashscope.DashScopeEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/dashscope.html#DashScopeEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

DashScope embedding models.

To use, you should have the `dashscope` python package installed, and the environment variable `DASHSCOPE_API_KEY` set with your API key or pass it as a named parameter to the constructor.

Example               from langchain_community.embeddings import DashScopeEmbeddings     embeddings = DashScopeEmbeddings(dashscope_api_key="my-api-key")     

Example               import os     os.environ["DASHSCOPE_API_KEY"] = "your DashScope API KEY"          from langchain_community.embeddings.dashscope import DashScopeEmbeddings     embeddings = DashScopeEmbeddings(         model="text-embedding-v1",     )     text = "This is a test query."     query_result = embeddings.embed_query(text)     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Any_ _ = None_\#     

The DashScope client.

_param _dashscope\_api\_key _: str | None_ _ = None_\#     

_param _max\_retries _: int_ _ = 5_\#     

Maximum number of retries to make when generating.

_param _model _: str_ _ = 'text-embedding-v1'_\#     

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/dashscope.html#DashScopeEmbeddings.embed_documents)\#     

Call out to DashScope’s embedding endpoint for embedding search docs.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/dashscope.html#DashScopeEmbeddings.embed_query)\#     

Call out to DashScope’s embedding endpoint for embedding query text.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embedding for the text.

Return type:     

_List_\[float\]

Examples using DashScopeEmbeddings

  * [DashScope](https://python.langchain.com/docs/integrations/text_embedding/dashscope/)

  * [DashScope Reranker](https://python.langchain.com/docs/integrations/document_transformers/dashscope_rerank/)

  * [DashVector](https://python.langchain.com/docs/integrations/vectorstores/dashvector/)

__On this page