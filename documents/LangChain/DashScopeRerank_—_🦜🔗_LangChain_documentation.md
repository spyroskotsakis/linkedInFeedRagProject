# DashScopeRerank — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_compressors/langchain_community.document_compressors.dashscope_rerank.DashScopeRerank.html
**Word Count:** 174
**Links Count:** 138
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# DashScopeRerank\#

_class _langchain\_community.document\_compressors.dashscope\_rerank.DashScopeRerank[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/dashscope_rerank.html#DashScopeRerank)\#     

Bases: [`BaseDocumentCompressor`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.compressor.BaseDocumentCompressor.html#langchain_core.documents.compressor.BaseDocumentCompressor "langchain_core.documents.compressor.BaseDocumentCompressor")

Document compressor that uses DashScope Rerank API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Any_ _ = None_\#     

DashScope client to use for compressing documents.

_param _dashscope\_api\_key _: str | None_ _ = None_ _\(alias 'api\_key'\)_\#     

DashScope API key. Must be specified directly or via environment variable DASHSCOPE\_API\_KEY.

_param _model _: str | None_ _ = None_\#     

Model to use for reranking.

_param _top\_n _: int | None_ _ = 3_\#     

Number of documents to return.

_async _acompress\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : Callbacks | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async compress retrieved documents given the query context.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The retrieved documents.

  * **query** \(_str_\) – The query context.

  * **callbacks** \(_Optional_ _\[__Callbacks_ _\]_\) – Optional callbacks to run during compression.

Returns:     

The compressed documents.

Return type:     

Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

compress\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/dashscope_rerank.html#DashScopeRerank.compress_documents)\#     

Compress documents using DashScope’s rerank API.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of documents to compress.

  * **query** \(_str_\) – The query to use for compressing the documents.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to run during the compression process.

Returns:     

A sequence of compressed documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

rerank\(

    _documents : Sequence\[str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | dict\]_,     _query : str_,     _\*_ ,     _top\_n : int | None = -1_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/dashscope_rerank.html#DashScopeRerank.rerank)\#     

Returns an ordered list of documents ordered by their relevance to the provided query.

Parameters:     

  * **query** \(_str_\) – The query to use for reranking.

  * **documents** \(_Sequence_ _\[__str_ _|_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _|__dict_ _\]_\) – A sequence of documents to rerank.

  * **top\_n** \(_int_ _|__None_\) – The number of results to return. If None returns all results. Defaults to self.top\_n.

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

Examples using DashScopeRerank

  * [DashScope Reranker](https://python.langchain.com/docs/integrations/document_transformers/dashscope_rerank/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)