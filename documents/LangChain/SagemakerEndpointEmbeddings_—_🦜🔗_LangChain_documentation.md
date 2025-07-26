# SagemakerEndpointEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.sagemaker_endpoint.SagemakerEndpointEmbeddings.html
**Word Count:** 308
**Links Count:** 243
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# SagemakerEndpointEmbeddings\#

_class _langchain\_community.embeddings.sagemaker\_endpoint.SagemakerEndpointEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sagemaker_endpoint.html#SagemakerEndpointEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Custom Sagemaker Inference Endpoints.

To use, you must supply the endpoint name from your deployed Sagemaker model & the region where it is deployed.

To authenticate, the AWS client uses the following methods to automatically load credentials: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If a specific credential profile should be used, you must pass the name of the profile from the ~/.aws/credentials file that is to be used.

Make sure the credentials / roles used have the required policies to access the Sagemaker endpoint. See: <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html>

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client _: Any_ _ = None_\#     

_param _content\_handler _: [EmbeddingsContentHandler](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.sagemaker_endpoint.EmbeddingsContentHandler.html#langchain_community.embeddings.sagemaker_endpoint.EmbeddingsContentHandler "langchain_community.embeddings.sagemaker_endpoint.EmbeddingsContentHandler")_ _\[Required\]_\#     

The content handler class that provides an input and output transform functions to handle formats between LLM and the endpoint.

_param _credentials\_profile\_name _: str | None_ _ = None_\#     

The name of the profile in the ~/.aws/credentials or ~/.aws/config files, which has either access keys or role information specified. If not specified, the default credential profile or, if on an EC2 instance, credentials from IMDS will be used. See: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

_param _endpoint\_kwargs _: Dict | None_ _ = None_\#     

Optional attributes passed to the invoke\_endpoint function. See \`boto3\`\_. docs for more info. .. \_boto3: <<https://boto3.amazonaws.com/v1/documentation/api/latest/index.html>>

_param _endpoint\_name _: str_ _ = ''_\#     

The name of the endpoint from the deployed Sagemaker model. Must be unique within an AWS Region.

_param _model\_kwargs _: Dict | None_ _ = None_\#     

Keyword arguments to pass to the model.

_param _region\_name _: str_ _ = ''_\#     

The aws region where the Sagemaker model is deployed, eg. us-west-2.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sagemaker_endpoint.html#SagemakerEndpointEmbeddings.validate_environment)\#     

Dont do anything if client provided externally

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\_documents\(

    _texts : List\[str\]_,     _chunk\_size : int = 64_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sagemaker_endpoint.html#SagemakerEndpointEmbeddings.embed_documents)\#     

Compute doc embeddings using a SageMaker Inference Endpoint.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

  * **chunk\_size** \(_int_\) – The chunk size defines how many input texts will be grouped together as request. If None, will use the chunk size specified by the class.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/sagemaker_endpoint.html#SagemakerEndpointEmbeddings.embed_query)\#     

Compute query embeddings using a SageMaker inference endpoint.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

Examples using SagemakerEndpointEmbeddings

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [SageMaker](https://python.langchain.com/docs/integrations/text_embedding/sagemaker-endpoint/)

__On this page