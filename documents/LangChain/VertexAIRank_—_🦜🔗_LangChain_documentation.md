# VertexAIRank — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/vertex_rank/langchain_google_community.vertex_rank.VertexAIRank.html
**Word Count:** 221
**Links Count:** 151
**Scraped:** 2025-07-21 07:59:55
**Status:** completed

---

# VertexAIRank\#

_class _langchain\_google\_community.vertex\_rank.VertexAIRank[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/vertex_rank.html#VertexAIRank)\#     

Bases: [`BaseDocumentCompressor`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.compressor.BaseDocumentCompressor.html#langchain_core.documents.compressor.BaseDocumentCompressor "langchain_core.documents.compressor.BaseDocumentCompressor")

Initializes the Vertex AI Ranker with configurable parameters.

Inherits from BaseDocumentCompressor for document processing and validation features, respectively.

project\_id\#     

Google Cloud project ID

Type:     

str

location\_id\#     

Location ID for the ranking service.

Type:     

str

ranking\_config\#     

Required. The name of the rank service config, such as default\_config. It is set to default\_config by default if unspecified.

Type:     

str

model\#     

The identifier of the model to use. It is one of:

  * `semantic-ranker-512@latest`: Semantic ranking model with maximum input token size 512.

It is set to `semantic-ranker-512@latest` by default if unspecified.

Type:     

str

top\_n\#     

The number of results to return. If this is unset or no bigger than zero, returns all results.

Type:     

int

ignore\_record\_details\_in\_response\#     

If true, the response will contain only record ID and score. By default, it is false, the response will contain record details.

Type:     

bool

id\_field\#     

Specifies a unique document metadata field

Type:     

Optional\[str\]

to use as an id.     

title\_field\#     

Specifies the document metadata field

Type:     

Optional\[str\]

to use as title.     

credentials\#     

Google Cloud credentials object.

Type:     

Optional\[Credentials\]

credentials\_path\#     

Path to the Google Cloud service

Type:     

Optional\[str\]

account credentials file.     

timeout\#     

Timeout for API calls in seconds.

Type:     

Optional\[int\]

Constructor for VertexAIRanker, allowing for specification of ranking configuration and initialization of Google Cloud services.

The parameters accepted are the same as the attributes listed above.

_param _client _: Any_ _ = None_\#     

_param _credentials _: Credentials | None_ _ = None_\#     

_param _credentials\_path _: str | None_ _ = None_\#     

_param _id\_field _: str | None_ _ = None_\#     

_param _ignore\_record\_details\_in\_response _: bool_ _ = False_\#     

_param _location\_id _: str_ _ = 'global'_\#     

_param _model _: str_ _ = 'semantic-ranker-512@latest'_\#     

_param _project\_id _: str_ _ = None_\#     

_param _ranking\_config _: str_ _ = 'default\_config'_\#     

_param _timeout _: int | None_ _ = None_\#     

_param _title\_field _: str | None_ _ = None_\#     

_param _top\_n _: int_ _ = 10_\#     

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

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/vertex_rank.html#VertexAIRank.compress_documents)\#     

Compresses documents using Vertex AI’s rerank API.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of Document instances to compress.

  * **query** \(_str_\) – Query string to use for compressing the documents.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to execute during compression \(not used here\).

Returns:     

A list of Document instances, compressed.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page