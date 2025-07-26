# OpenVINOReranker — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_compressors/langchain_community.document_compressors.openvino_rerank.OpenVINOReranker.html
**Word Count:** 110
**Links Count:** 141
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# OpenVINOReranker\#

_class _langchain\_community.document\_compressors.openvino\_rerank.OpenVINOReranker[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/openvino_rerank.html#OpenVINOReranker)\#     

Bases: [`BaseDocumentCompressor`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.compressor.BaseDocumentCompressor.html#langchain_core.documents.compressor.BaseDocumentCompressor "langchain_core.documents.compressor.BaseDocumentCompressor")

OpenVINO rerank models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments passed to the model.

_param _model\_name\_or\_path _: str_ _\[Required\]_\#     

HuggingFace model id.

_param _ov\_model _: Any_ _ = None_\#     

OpenVINO model object.

_param _tokenizer _: Any_ _ = None_\#     

Tokenizer for embedding model.

_param _top\_n _: int_ _ = 4_\#     

return Top n texts.

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

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/openvino_rerank.html#OpenVINOReranker.compress_documents)\#     

Compress retrieved documents given the query context.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The retrieved documents.

  * **query** \(_str_\) – The query context.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Optional callbacks to run during compression.

Returns:     

The compressed documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

rerank\(_request : Any_\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/openvino_rerank.html#OpenVINOReranker.rerank)\#     

Parameters:     

**request** \(_Any_\)

Return type:     

_Any_

save\_model\(_model\_path : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/openvino_rerank.html#OpenVINOReranker.save_model)\#     

Parameters:     

**model\_path** \(_str_\)

Return type:     

bool

Examples using OpenVINOReranker

  * [OpenVINO Reranker](https://python.langchain.com/docs/integrations/document_transformers/openvino_rerank/)

__On this page