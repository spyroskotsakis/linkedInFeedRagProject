# BedrockEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/embeddings/langchain_aws.embeddings.bedrock.BedrockEmbeddings.html
**Word Count:** 395
**Links Count:** 126
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# BedrockEmbeddings\#

_class _langchain\_aws.embeddings.bedrock.BedrockEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/embeddings/bedrock.html#BedrockEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Bedrock embedding models.

To authenticate, the AWS client uses the following methods to automatically load credentials: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If a specific credential profile should be used, you must pass the name of the profile from the ~/.aws/credentials file that is to be used.

Make sure the credentials / roles used have the required policies to access the Bedrock service.

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

Bedrock client.

_param _config _: Any_ _ = None_\#     

An optional botocore.config.Config instance to pass to the client.

_param _credentials\_profile\_name _: str | None_ _ = None_\#     

The name of the profile in the ~/.aws/credentials or ~/.aws/config files, which has either access keys or role information specified. If not specified, the default credential profile or, if on an EC2 instance, credentials from IMDS will be used. See: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

_param _endpoint\_url _: str | None_ _ = None_\#     

Needed if you don’t want to default to us-east-1 endpoint

_param _model\_id _: str_ _ = 'amazon.titan-embed-text-v1'_\#     

Id of the model to call, e.g., amazon.titan-embed-text-v1, this is equivalent to the modelId property in the list-foundation-models api

_param _model\_kwargs _: Dict | None_ _ = None_\#     

Keyword arguments to pass to the model.

_param _normalize _: bool_ _ = False_\#     

Whether the embeddings should be normalized to unit vectors

_param _provider _: str | None_ _ = None_\#     

Name of the provider, e.g., amazon, cohere, etc.. If not specified, the provider will be inferred from the model\_id.

_param _region\_name _: str | None_ _ = None_\#     

The aws region e.g., us-west-2. Falls back to AWS\_REGION/AWS\_DEFAULT\_REGION env variable or region specified in ~/.aws/config in case it is not provided here.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/embeddings/bedrock.html#BedrockEmbeddings.aembed_documents)\#     

Asynchronous compute doc embeddings using a Bedrock model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/embeddings/bedrock.html#BedrockEmbeddings.aembed_query)\#     

Asynchronous compute query embeddings using a Bedrock model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/embeddings/bedrock.html#BedrockEmbeddings.embed_documents)\#     

Compute doc embeddings using a Bedrock model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/embeddings/bedrock.html#BedrockEmbeddings.embed_query)\#     

Compute query embeddings using a Bedrock model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using BedrockEmbeddings

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [Amazon MemoryDB](https://python.langchain.com/docs/integrations/vectorstores/memorydb/)

  * [Bedrock](https://python.langchain.com/docs/integrations/text_embedding/bedrock/)

__On this page