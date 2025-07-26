# BedrockRerank — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/document_compressors/langchain_aws.document_compressors.rerank.BedrockRerank.html
**Word Count:** 317
**Links Count:** 127
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# BedrockRerank\#

_class _langchain\_aws.document\_compressors.rerank.BedrockRerank[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/document_compressors/rerank.html#BedrockRerank)\#     

Bases: [`BaseDocumentCompressor`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.compressor.BaseDocumentCompressor.html#langchain_core.documents.compressor.BaseDocumentCompressor "langchain_core.documents.compressor.BaseDocumentCompressor")

Document compressor that uses AWS Bedrock Rerank API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aws\_access\_key\_id _: SecretStr | None_ _\[Optional\]_\#     

AWS access key id.

If provided, aws\_secret\_access\_key must also be provided. If not specified, the default credential profile or, if on an EC2 instance, credentials from IMDS will be used. See: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If not provided, will be read from ‘AWS\_ACCESS\_KEY\_ID’ environment variable.

_param _aws\_secret\_access\_key _: SecretStr | None_ _\[Optional\]_\#     

AWS secret\_access\_key.

If provided, aws\_access\_key\_id must also be provided. If not specified, the default credential profile or, if on an EC2 instance, credentials from IMDS will be used. See: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If not provided, will be read from ‘AWS\_SECRET\_ACCESS\_KEY’ environment variable.

_param _aws\_session\_token _: SecretStr | None_ _\[Optional\]_\#     

AWS session token.

If provided, aws\_access\_key\_id and aws\_secret\_access\_key must also be provided. Not required unless using temporary credentials. See: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If not provided, will be read from ‘AWS\_SESSION\_TOKEN’ environment variable.

_param _client _: Any_ _ = None_\#     

Bedrock client to use for compressing documents.

_param _config _: Any_ _ = None_\#     

An optional botocore.config.Config instance to pass to the client.

_param _credentials\_profile\_name _: str | None_ _\[Optional\]_\#     

AWS profile for authentication, optional.

_param _endpoint\_url _: str | None_ _ = None_ _\(alias 'base\_url'\)_\#     

Needed if you don’t want to default to us-east-1 endpoint

_param _model\_arn _: str_ _\[Required\]_\#     

The ARN of the reranker model.

_param _region\_name _: str | None_ _ = None_\#     

The aws region, e.g., us-west-2.

Falls back to AWS\_REGION or AWS\_DEFAULT\_REGION env variable or region specified in ~/.aws/config in case it is not provided here.

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

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/document_compressors/rerank.html#BedrockRerank.compress_documents)\#     

Compress documents using Bedrock’s rerank API.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of documents to compress.

  * **query** \(_str_\) – The query to use for compressing the documents.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to run during the compression process.

Returns:     

A sequence of compressed documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

rerank\(

    _documents : Sequence\[str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | dict\]_,     _query : str_,     _top\_n : int | None = None_,     _additional\_model\_request\_fields : Dict\[str, Any\] | None = None_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/document_compressors/rerank.html#BedrockRerank.rerank)\#     

Returns an ordered list of documents based on their relevance to the query.

Parameters:     

  * **query** \(_str_\) – The query to use for reranking.

  * **documents** \(_Sequence_ _\[__str_ _|_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _|__dict_ _\]_\) – A sequence of documents to rerank.

  * **top\_n** \(_int_ _|__None_\) – The number of top-ranked results to return. Defaults to self.top\_n.

  * **additional\_model\_request\_fields** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Additional fields to pass to the model.

Returns:     

A list of ranked documents with relevance scores.

Return type:     

List\[Dict\[str, Any\]\]

__On this page