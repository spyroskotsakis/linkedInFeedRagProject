# WatsonxRerank — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/ibm/rerank/langchain_ibm.rerank.WatsonxRerank.html
**Word Count:** 211
**Links Count:** 127
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# WatsonxRerank\#

_class _langchain\_ibm.rerank.WatsonxRerank[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/rerank.html#WatsonxRerank)\#     

Bases: [`BaseDocumentCompressor`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.compressor.BaseDocumentCompressor.html#langchain_core.documents.compressor.BaseDocumentCompressor "langchain_core.documents.compressor.BaseDocumentCompressor")

Document compressor that uses watsonx Rerank API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _apikey _: SecretStr | None_ _\[Optional\]_\#     

API key to the Watson Machine Learning or CPD instance.

_param _instance\_id _: SecretStr | None_ _\[Optional\]_\#     

Instance\_id of the CPD instance.

_param _model\_id _: str_ _\[Required\]_\#     

Type of model to use.

_param _params _: dict | RerankParameters | None_ _ = None_\#     

Model parameters to use during request generation.

_param _password _: SecretStr | None_ _\[Optional\]_\#     

Password to the CPD instance.

_param _project\_id _: str | None_ _ = None_\#     

ID of the Watson Studio project.

_param _space\_id _: str | None_ _ = None_\#     

ID of the Watson Studio space.

_param _streaming _: bool_ _ = False_\#     

Whether to stream the results or not.

_param _token _: SecretStr | None_ _\[Optional\]_\#     

Token to the CPD instance.

_param _url _: SecretStr_ _\[Optional\]_\#     

URL to the Watson Machine Learning or CPD instance.

_param _username _: SecretStr | None_ _\[Optional\]_\#     

Username to the CPD instance.

_param _validate\_model _: bool_ _ = True_\#     

Model ID validation.

_param _verify _: str | bool | None_ _ = None_\#     

You can pass one of following as verify: \* the path to a CA\_BUNDLE file \* the path of directory with certificates of trusted CAs \* True - default path to truststore will be taken \* False - no verification will be made

_param _version _: SecretStr | None_ _ = None_\#     

Version of the CPD instance.

_param _watsonx\_client _: APIClient | None_ _ = None_\#     

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

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/rerank.html#WatsonxRerank.compress_documents)\#     

Compress documents using watsonx’s rerank API.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of documents to compress.

  * **query** \(_str_\) – The query to use for compressing the documents.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to run during the compression process.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of compressed documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

rerank\(

    _documents : Sequence\[str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | dict\]_,     _query : str_,     _\*\* kwargs: Any_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/rerank.html#WatsonxRerank.rerank)\#     

Parameters:     

  * **documents** \(_Sequence_ _\[__str_ _|_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _|__dict_ _\]_\)

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_Dict_\[str, _Any_\]\]

__On this page