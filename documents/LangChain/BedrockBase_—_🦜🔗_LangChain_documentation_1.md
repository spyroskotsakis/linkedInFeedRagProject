# BedrockBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.bedrock.BedrockBase.html
**Word Count:** 331
**Links Count:** 308
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# BedrockBase\#

_class _langchain\_community.llms.bedrock.BedrockBase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/bedrock.html#BedrockBase)\#     

Bases: `BaseModel`, `ABC`

Base class for Bedrock models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _config _: Any_ _ = None_\#     

An optional botocore.config.Config instance to pass to the client.

_param _credentials\_profile\_name _: str | None_ _ = None_\#     

The name of the profile in the ~/.aws/credentials or ~/.aws/config files, which has either access keys or role information specified. If not specified, the default credential profile or, if on an EC2 instance, credentials from IMDS will be used. See: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

_param _endpoint\_url _: str | None_ _ = None_\#     

Needed if you don’t want to default to us-east-1 endpoint

_param _guardrails _: Mapping\[str, Any\] | None_ _ = \{'id': None, 'trace': False, 'version': None\}_\#     

An optional dictionary to configure guardrails for Bedrock.

This field ‘guardrails’ consists of two keys: ‘id’ and ‘version’, which should be strings, but are initialized to None. It’s used to determine if specific guardrails are enabled and properly set.

Type:     

Optional\[Mapping\[str, str\]\]: A mapping with ‘id’ and ‘version’ keys.

Example: llm = Bedrock\(model\_id=”<model\_id>”, client=<bedrock\_client>,

> model\_kwargs=\{\}, guardrails=\{ >
>> “id”: “<guardrail\_id>”, “version”: “<guardrail\_version>”\}\)

To enable tracing for guardrails, set the ‘trace’ key to True and pass a callback handler to the ‘run\_manager’ parameter of the ‘generate’, ‘\_call’ methods.

Example: llm = Bedrock\(model\_id=”<model\_id>”, client=<bedrock\_client>,

> > model\_kwargs=\{\}, guardrails=\{ >> >>> “id”: “<guardrail\_id>”, “version”: “<guardrail\_version>”, “trace”: True\}, >  > callbacks=\[BedrockAsyncCallbackHandler\(\)\]\)

\[<https://python.langchain.com/docs/modules/callbacks/>\] for more information on callback handlers.

class BedrockAsyncCallbackHandler\(AsyncCallbackHandler\):     

async def on\_llm\_error\(     

self, error: BaseException, \*\*kwargs: Any,

\) -> Any:     

reason = kwargs.get\(“reason”\) if reason == “GUARDRAIL\_INTERVENED”:

> …Logic to handle guardrail intervention…

_param _model\_id _: str_ _\[Required\]_\#     

Id of the model to call, e.g., amazon.titan-text-express-v1, this is equivalent to the modelId property in the list-foundation-models api. For custom and provisioned models, an ARN value is expected.

_param _model\_kwargs _: Dict | None_ _ = None_\#     

Keyword arguments to pass to the model.

_param _provider _: str | None_ _ = None_\#     

The model provider, e.g., amazon, cohere, ai21, etc. When not supplied, provider is extracted from the first part of the model\_id e.g. ‘amazon’ in ‘amazon.titan-text-express-v1’. This value should be provided for model ids that do not have the provider in them, e.g., custom and provisioned models that have an ARN associated with them.

_param _provider\_stop\_sequence\_key\_name\_map _: Mapping\[str, str\]__ = \{'ai21': 'stop\_sequences', 'amazon': 'stopSequences', 'anthropic': 'stop\_sequences', 'cohere': 'stop\_sequences', 'mistral': 'stop'\}_\#     

_param _region\_name _: str | None_ _ = None_\#     

The aws region e.g., us-west-2. Fallsback to AWS\_DEFAULT\_REGION env variable or region specified in ~/.aws/config in case it is not provided here.

_param _streaming _: bool_ _ = False_\#     

Whether to stream the results.

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/bedrock.html#BedrockBase.validate_environment)\#     

Validate that AWS credentials to and python package exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

__On this page