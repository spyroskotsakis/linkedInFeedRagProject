# LambdaWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.awslambda.LambdaWrapper.html
**Word Count:** 117
**Links Count:** 260
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# LambdaWrapper\#

_class _langchain\_community.utilities.awslambda.LambdaWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/awslambda.html#LambdaWrapper)\#     

Bases: `BaseModel`

Wrapper for AWS Lambda SDK. To use, you should have the `boto3` package installed and a lambda functions built from the AWS Console or CLI. Set up your AWS credentials with `aws configure`

Example               pip install boto3          aws configure     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _awslambda\_tool\_description _: str | None_ _ = None_\#     

If passing to an agent as a tool, the description

_param _awslambda\_tool\_name _: str | None_ _ = None_\#     

If passing to an agent as a tool, the tool name

_param _function\_name _: str | None_ _ = None_\#     

The name of your lambda function

_param _lambda\_client _: Any_ _ = None_\#     

The configured boto3 client

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/awslambda.html#LambdaWrapper.run)\#     

Invokes the lambda function and returns the result.

Parameters:     

**query** \(_str_\) – an input to passed to the lambda function as the `body` of a JSON object.

Return type:     

str

__On this page