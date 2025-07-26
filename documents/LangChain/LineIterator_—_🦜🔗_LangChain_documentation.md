# LineIterator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.sagemaker_endpoint.LineIterator.html
**Word Count:** 125
**Links Count:** 94
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# LineIterator\#

_class _langchain\_aws.llms.sagemaker\_endpoint.LineIterator\(_stream : Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/llms/sagemaker_endpoint.html#LineIterator)\#     

> A helper class for parsing the byte stream input. >  > The output of the model will be in the following format: >  > b’\{“outputs”: \[” a”\]\}

‘     

b’\{“outputs”: \[” challenging”\]\}

‘     

b’\{“outputs”: \[” problem”\]\}

‘     

…

While usually each PayloadPart event from the event stream will contain a byte array with a full json, this is not guaranteed and some of the json objects may be split acrossPayloadPart events.

For example:

\{‘PayloadPart’: \{‘Bytes’: b’\{“outputs”: ‘\}\} \{‘PayloadPart’: \{‘Bytes’: b’\[” problem”\]\}

‘\}\}

> This class accounts for this by concatenating bytes written via the ‘write’ function and then exposing a method which will return lines \(ending with a ‘

‘ character\)     

within the buffer via the ‘scan\_lines’ function. It maintains the position of the last read position to ensure that previous bytes are not exposed again.

For more details see: <https://aws.amazon.com/blogs/machine-learning/elevating-the-generative-ai-experience-introducing-streaming-support-in-amazon-sagemaker-hosting/>

Methods

`__init__`\(stream\) |    ---|---      Parameters:     

**stream** \(_Any_\)

\_\_init\_\_\(_stream : Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/llms/sagemaker_endpoint.html#LineIterator.__init__)\#     

Parameters:     

**stream** \(_Any_\)

Return type:     

None

__On this page