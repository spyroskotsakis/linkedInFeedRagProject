# SagemakerEndpointCrossEncoder — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.sagemaker_endpoint.SagemakerEndpointCrossEncoder.html
**Word Count:** 204
**Links Count:** 122
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# SagemakerEndpointCrossEncoder\#

_class _langchain\_community.cross\_encoders.sagemaker\_endpoint.SagemakerEndpointCrossEncoder[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/sagemaker_endpoint.html#SagemakerEndpointCrossEncoder)\#     

Bases: `BaseModel`, [`BaseCrossEncoder`](https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder.html#langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder "langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder")

SageMaker Inference CrossEncoder endpoint.

To use, you must supply the endpoint name from your deployed Sagemaker model & the region where it is deployed.

To authenticate, the AWS client uses the following methods to automatically load credentials: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If a specific credential profile should be used, you must pass the name of the profile from the ~/.aws/credentials file that is to be used.

Make sure the credentials / roles used have the required policies to access the Sagemaker endpoint. See: <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html>

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _content\_handler _: [CrossEncoderContentHandler](https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.sagemaker_endpoint.CrossEncoderContentHandler.html#langchain_community.cross_encoders.sagemaker_endpoint.CrossEncoderContentHandler "langchain_community.cross_encoders.sagemaker_endpoint.CrossEncoderContentHandler")_ _ = <langchain\_community.cross\_encoders.sagemaker\_endpoint.CrossEncoderContentHandler object>_\#     

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

score\(

    _text\_pairs : List\[Tuple\[str, str\]\]_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/sagemaker_endpoint.html#SagemakerEndpointCrossEncoder.score)\#     

Call out to SageMaker Inference CrossEncoder endpoint.

Parameters:     

**text\_pairs** \(_List_ _\[__Tuple_ _\[__str_ _,__str_ _\]__\]_\)

Return type:     

_List_\[float\]

__On this page