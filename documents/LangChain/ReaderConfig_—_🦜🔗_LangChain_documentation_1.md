# ReaderConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.titan_takeoff.ReaderConfig.html
**Word Count:** 100
**Links Count:** 295
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# ReaderConfig\#

_class _langchain\_community.llms.titan\_takeoff.ReaderConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/titan_takeoff.html#ReaderConfig)\#     

Bases: `BaseModel`

Configuration for the reader to be deployed in Titan Takeoff API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _consumer\_group _: str_ _ = 'primary'_\#     

The consumer group to place the reader into

_param _device _: [Device](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.titan_takeoff.Device.html#langchain_community.llms.titan_takeoff.Device "langchain_community.llms.titan_takeoff.Device")_ _ = Device.cuda_\#     

The device to use for inference, cuda or cpu

_param _max\_batch\_size _: int_ _ = 4_\#     

The max batch size for continuous batching of requests

_param _max\_seq\_length _: int_ _ = 512_\#     

The maximum sequence length to use for inference, defaults to 512

_param _model\_name _: str_ _\[Required\]_\#     

The name of the model to use

_param _tensor\_parallel _: int | None_ _ = None_\#     

The number of gpus you would like your model to be split across

__On this page