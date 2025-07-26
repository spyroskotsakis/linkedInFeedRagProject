# ReaderConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.titan_takeoff.ReaderConfig.html
**Word Count:** 68
**Links Count:** 214
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# ReaderConfig\#

_class _langchain\_community.embeddings.titan\_takeoff.ReaderConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/titan_takeoff.html#ReaderConfig)\#     

Bases: `BaseModel`

Configuration for the reader to be deployed in Takeoff.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _consumer\_group _: str_ _ = 'primary'_\#     

The consumer group to place the reader into

_param _device _: [Device](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.titan_takeoff.Device.html#langchain_community.embeddings.titan_takeoff.Device "langchain_community.embeddings.titan_takeoff.Device")_ _ = Device.cuda_\#     

The device to use for inference, cuda or cpu

_param _model\_name _: str_ _\[Required\]_\#     

The name of the model to use

__On this page