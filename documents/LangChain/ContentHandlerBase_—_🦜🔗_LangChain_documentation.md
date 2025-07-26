# ContentHandlerBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/utils/langchain_aws.utils.ContentHandlerBase.html
**Word Count:** 130
**Links Count:** 96
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# ContentHandlerBase\#

_class _langchain\_aws.utils.ContentHandlerBase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/utils.html#ContentHandlerBase)\#     

A handler class to transform input from LLM and BaseChatModel to a

format that SageMaker endpoint expects.

Similarly, the class handles transforming output from the SageMaker endpoint to a format that LLM & BaseChatModel class expects.

Attributes

`accepts` | The MIME type of the response data returned from endpoint   ---|---   `content_type` | The MIME type of the input data passed to endpoint      Methods

`transform_input`\(prompt, model\_kwargs\) | Transforms the input to a format that model can accept as the request Body.   ---|---   `transform_output`\(output\) | Transforms the output from the model to string that the LLM class expects.      _abstractmethod _transform\_input\(

    _prompt : INPUT\_TYPE_,     _model\_kwargs : Dict_, \) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/utils.html#ContentHandlerBase.transform_input)\#     

Transforms the input to a format that model can accept as the request Body. Should return bytes or seekable file like object in the format specified in the content\_type request header.

Parameters:     

  * **prompt** \(_INPUT\_TYPE_\)

  * **model\_kwargs** \(_Dict_\)

Return type:     

bytes

_abstractmethod _transform\_output\(

    _output : bytes_, \) → OUTPUT\_TYPE[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/utils.html#ContentHandlerBase.transform_output)\#     

Transforms the output from the model to string that the LLM class expects.

Parameters:     

**output** \(_bytes_\)

Return type:     

_OUTPUT\_TYPE_

Examples using ContentHandlerBase

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

__On this page