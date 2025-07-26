# ContentHandlerBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.sagemaker_endpoint.ContentHandlerBase.html
**Word Count:** 126
**Links Count:** 291
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# ContentHandlerBase\#

_class _langchain\_community.llms.sagemaker\_endpoint.ContentHandlerBase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/sagemaker_endpoint.html#ContentHandlerBase)\#     

Handler class to transform input from LLM to a format that SageMaker endpoint expects.

Similarly, the class handles transforming output from the SageMaker endpoint to a format that LLM class expects.

Attributes

`accepts` | The MIME type of the response data returned from endpoint   ---|---   `content_type` | The MIME type of the input data passed to endpoint      Methods

`transform_input`\(prompt, model\_kwargs\) | Transforms the input to a format that model can accept as the request Body.   ---|---   `transform_output`\(output\) | Transforms the output from the model to string that the LLM class expects.      _abstractmethod _transform\_input\(

    _prompt : INPUT\_TYPE_,     _model\_kwargs : Dict_, \) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/sagemaker_endpoint.html#ContentHandlerBase.transform_input)\#     

Transforms the input to a format that model can accept as the request Body. Should return bytes or seekable file like object in the format specified in the content\_type request header.

Parameters:     

  * **prompt** \(_INPUT\_TYPE_\)

  * **model\_kwargs** \(_Dict_\)

Return type:     

bytes

_abstractmethod _transform\_output\(

    _output : bytes_, \) → OUTPUT\_TYPE[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/sagemaker_endpoint.html#ContentHandlerBase.transform_output)\#     

Transforms the output from the model to string that the LLM class expects.

Parameters:     

**output** \(_bytes_\)

Return type:     

_OUTPUT\_TYPE_

Examples using ContentHandlerBase

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

__On this page