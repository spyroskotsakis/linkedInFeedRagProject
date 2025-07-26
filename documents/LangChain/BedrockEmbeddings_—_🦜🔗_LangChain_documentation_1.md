# BedrockEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.bedrock.BedrockEmbeddings.html
**Word Count:** 278
**Links Count:** 239
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# BedrockEmbeddings\#

_class _langchain\_community.embeddings.bedrock.BedrockEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/bedrock.html#BedrockEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Deprecated since version 0.2.11: Use `:class:`~langchain_aws.BedrockEmbeddings`` instead. It will not be removed until langchain-community==1.0.

Bedrock embedding models.

To authenticate, the AWS client uses the following methods to automatically load credentials: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If a specific credential profile should be used, you must pass the name of the profile from the ~/.aws/credentials file that is to be used.

Make sure the credentials / roles used have the required policies to access the Bedrock service.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Any_ _ = None_\#     

Bedrock client.

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

_param _region\_name _: str | None_ _ = None_\#     

The aws region e.g., us-west-2. Fallsback to AWS\_DEFAULT\_REGION env variable or region specified in ~/.aws/config in case it is not provided here.

_async _aembed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/bedrock.html#BedrockEmbeddings.aembed_documents)\#     

Asynchronous compute doc embeddings using a Bedrock model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/bedrock.html#BedrockEmbeddings.aembed_query)\#     

Asynchronous compute query embeddings using a Bedrock model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/bedrock.html#BedrockEmbeddings.embed_documents)\#     

Compute doc embeddings using a Bedrock model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/bedrock.html#BedrockEmbeddings.embed_query)\#     

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