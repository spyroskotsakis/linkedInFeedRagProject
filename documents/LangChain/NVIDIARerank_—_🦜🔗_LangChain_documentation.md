# NVIDIARerank — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/nvidia_ai_endpoints/reranking/langchain_nvidia_ai_endpoints.reranking.NVIDIARerank.html
**Word Count:** 521
**Links Count:** 109
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# NVIDIARerank\#

_class _langchain\_nvidia\_ai\_endpoints.reranking.NVIDIARerank[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/reranking.html#NVIDIARerank)\#     

Bases: [`BaseDocumentCompressor`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.compressor.BaseDocumentCompressor.html#langchain_core.documents.compressor.BaseDocumentCompressor "langchain_core.documents.compressor.BaseDocumentCompressor")

LangChain Document Compressor that uses the NVIDIA NeMo Retriever Reranking API.

> Create a new NVIDIARerank document compressor. >  > This class provides access to a NVIDIA NIM for reranking. By default, it connects to a hosted NIM, but can be configured to connect to a local NIM using the base\_url parameter. An API key is required to connect to the hosted NIM. >  > Args: >      >  > model \(str\): The model to use for reranking. nvidia\_api\_key \(str\): The API key to use for connecting to the hosted NIM. api\_key \(str\): Alternative to nvidia\_api\_key. base\_url \(str\): The base URL of the NIM to connect to. truncate \(str\): “NONE”, “END”, truncate input text if it exceeds >
>> the model’s context length. Default is model dependent and is likely to raise an error if an input is too long. >  > API Key: \- The recommended way to provide the API key is through the NVIDIA\_API\_KEY >
>> environment variable. >  > Base URL: \- Connect to a self-hosted model with NVIDIA NIM using the base\_url arg to >
>> link to the local host at localhost:8000: ranker = NVIDIARerank\(base\_url=”http://localhost:8000/v1”\) >  > Example: >>> from langchain\_nvidia\_ai\_endpoints import NVIDIARerank >>> from langchain\_core.documents import Document >      >      >     >>> query = "What is the GPU memory bandwidth of H100 SXM?" >     >>> passages = [ >             "The Hopper GPU is paired with the Grace CPU using NVIDIA's ultra-fast >             chip-to-chip interconnect, delivering 900GB/s of bandwidth, 7X faster >             than PCIe Gen5. This innovative design will deliver up to 30X higher >             aggregate system memory bandwidth to the GPU compared to today's fastest >             servers and up to 10X higher performance for applications running >             terabytes of data.", >      >
>> > “A100 provides up to 20X higher performance over the prior generation and can be partitioned into seven GPU instances to dynamically adjust to shifting demands. The A100 80GB debuts the world’s fastest memory bandwidth at over 2 terabytes per second \(TB/s\) to run the largest models and datasets.”, >>>  >>> “Accelerated servers with H100 deliver the compute power—along with 3 terabytes per second \(TB/s\) of memory bandwidth per GPU and scalability with NVLink and NVSwitch™.”, >>  >> \] >      >      >     >>> client = NVIDIARerank( >             model="nvidia/nv-rerankqa-mistral-4b-v3", >             api_key="$API_KEY_REQUIRED_IF_EXECUTING_OUTSIDE_NGC" >         ) >      >      >      >     >>> response = client.compress_documents( >             query=query, >             documents=[Document(page_content=passage) for passage in passages] >         ) >      >      >      >     >>> print(f"Most relevant: {response[0].page_content} >     

“     

> > f”Least relevant: \{response\[-1\].page\_content\}” >  > \)

Most relevant: Accelerated servers with H100 deliver the compute power—along with 3 terabytes per second \(TB/s\) of memory bandwidth per GPU and scalability with NVLink and NVSwitch™. Least relevant: A100 provides up to 20X higher performance over the prior generation and can be partitioned into seven GPU instances to dynamically adjust to shifting demands. The A100 80GB debuts the world’s fastest memory bandwidth at over 2 terabytes per second \(TB/s\) to run the largest models and datasets.

_param _base\_url _: str | None_ _ = None_\#     

Base url for model listing an invocation

_param _extra\_headers _: dict_ _\[Optional\]_\#     

Extra headers to include in the request.

_param _max\_batch\_size _: int_ _ = 32_\#     

The maximum batch size.

Constraints:     

  * **ge** = 1

_param _model _: str | None_ _ = None_\#     

The model to use for reranking.

_param _top\_n _: int_ _ = 5_\#     

The number of documents to return.

Constraints:     

  * **ge** = 0

_param _truncate _: Literal\['NONE', 'END'\] | None_ _ = None_\#     

Truncate input text if it exceeds the model’s maximum token length. Default is model dependent and is likely to raise error if an input is too long.

_classmethod _get\_available\_models\(

    _\*\* kwargs: Any_, \) → List\[Model\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/reranking.html#NVIDIARerank.get_available_models)\#     

Get a list of available models that work with NVIDIARerank.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

_List_\[_Model_\]

_async _acompress\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : Callbacks | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async compress retrieved documents given the query context.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The retrieved documents.

  * **query** \(_str_\) – The query context.

  * **callbacks** \(_Optional_ _\[__Callbacks_ _\]_\) – Optional callbacks to run during compression.

Returns:     

The compressed documents.

Return type:     

Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

compress\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_nvidia_ai_endpoints/reranking.html#NVIDIARerank.compress_documents)\#     

Compress documents using the NVIDIA NeMo Retriever Reranking microservice API.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of documents to compress.

  * **query** \(_str_\) – The query to use for compressing the documents.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to run during the compression process.

Returns:     

A sequence of compressed documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_property _available\_models _: List\[Model\]_\#     

Get a list of available models that work with NVIDIARerank.

__On this page