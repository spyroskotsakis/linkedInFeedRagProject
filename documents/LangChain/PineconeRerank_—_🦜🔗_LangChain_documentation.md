# PineconeRerank — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/pinecone/rerank/langchain_pinecone.rerank.PineconeRerank.html
**Word Count:** 132
**Links Count:** 120
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# PineconeRerank\#

_class _langchain\_pinecone.rerank.PineconeRerank[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/rerank.html#PineconeRerank)\#     

Bases: [`BaseDocumentCompressor`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.compressor.BaseDocumentCompressor.html#langchain_core.documents.compressor.BaseDocumentCompressor "langchain_core.documents.compressor.BaseDocumentCompressor")

Document compressor that uses Pinecone Rerank API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _async\_client _: PineconeAsyncio | None_ _ = None_\#     

Pinecone client to use for compressing documents.

_param _client _: [Pinecone](https://python.langchain.com/api_reference/pinecone/vectorstores/langchain_pinecone.vectorstores.Pinecone.html#langchain_pinecone.vectorstores.Pinecone "langchain_pinecone.vectorstores.Pinecone") | None_ _ = None_\#     

Pinecone client to use for compressing documents.

_param _model _: str_ _ = 'bge-reranker-v2-m3'_\#     

Model to use for reranking.

Model to use for reranking. Default is ‘bge-reranker-v2-m3’.

_param _pinecone\_api\_key _: SecretStr | None_ _\[Optional\]_\#     

Pinecone API key. Must be specified directly or via environment variable PINECONE\_API\_KEY.

_param _rank\_fields _: List\[str\] | None_ _ = None_\#     

Fields to use for reranking when documents are dictionaries.

_param _return\_documents _: bool_ _ = True_\#     

Whether to return the documents in the reranking results.

_param _top\_n _: int | None_ _ = 3_\#     

Number of documents to return.

_async _acompress\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/rerank.html#PineconeRerank.acompress_documents)\#     

Async compress documents using Pinecone’s rerank API.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **query** \(_str_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _arerank\(

    _documents : Sequence\[str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | dict\]_,     _query : str_,     _\*_ ,     _rank\_fields : List\[str\] | None = None_,     _model : str | None = None_,     _top\_n : int | None = None_,     _truncate : str = 'END'_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/rerank.html#PineconeRerank.arerank)\#     

Async rerank documents using Pinecone’s reranking API.

Parameters:     

  * **documents** \(_Sequence_ _\[__str_ _|_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _|__dict_ _\]_\)

  * **query** \(_str_\)

  * **rank\_fields** \(_List_ _\[__str_ _\]__|__None_\)

  * **model** \(_str_ _|__None_\)

  * **top\_n** \(_int_ _|__None_\)

  * **truncate** \(_str_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

compress\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/rerank.html#PineconeRerank.compress_documents)\#     

Compress documents using Pinecone’s rerank API.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **query** \(_str_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

rerank\(

    _documents : Sequence\[str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | dict\]_,     _query : str_,     _\*_ ,     _rank\_fields : List\[str\] | None = None_,     _model : str | None = None_,     _top\_n : int | None = None_,     _truncate : str = 'END'_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/rerank.html#PineconeRerank.rerank)\#     

Returns an ordered list of documents ordered by their relevance to the provided query.

Parameters:     

  * **documents** \(_Sequence_ _\[__str_ _|_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _|__dict_ _\]_\)

  * **query** \(_str_\)

  * **rank\_fields** \(_List_ _\[__str_ _\]__|__None_\)

  * **model** \(_str_ _|__None_\)

  * **top\_n** \(_int_ _|__None_\)

  * **truncate** \(_str_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)