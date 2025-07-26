# ChatModelContentHandler — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/chat_models/langchain_aws.chat_models.sagemaker_endpoint.ChatModelContentHandler.html
**Word Count:** 99
**Links Count:** 99
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# ChatModelContentHandler\#

_class _langchain\_aws.chat\_models.sagemaker\_endpoint.ChatModelContentHandler[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/chat_models/sagemaker_endpoint.html#ChatModelContentHandler)\#     

Content handler for ChatSagemakerEndpoint class.

Attributes

`accepts` | The MIME type of the response data returned from endpoint   ---|---   `content_type` | The MIME type of the input data passed to endpoint      Methods

`transform_input`\(prompt, model\_kwargs\) | Transforms the input to a format that model can accept as the request Body.   ---|---   `transform_output`\(output\) | Transforms the output from the model to string that the LLM class expects.      _abstractmethod _transform\_input\(

    _prompt : INPUT\_TYPE_,     _model\_kwargs : Dict_, \) → bytes\#     

Transforms the input to a format that model can accept as the request Body. Should return bytes or seekable file like object in the format specified in the content\_type request header.

Parameters:     

  * **prompt** \(_INPUT\_TYPE_\)

  * **model\_kwargs** \(_Dict_\)

Return type:     

bytes

_abstractmethod _transform\_output\(

    _output : bytes_, \) → OUTPUT\_TYPE\#     

Transforms the output from the model to string that the LLM class expects.

Parameters:     

**output** \(_bytes_\)

Return type:     

_OUTPUT\_TYPE_

__On this page