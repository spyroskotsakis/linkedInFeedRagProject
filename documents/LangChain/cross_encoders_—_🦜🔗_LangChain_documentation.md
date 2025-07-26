# cross_encoders — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cross_encoders.html
**Word Count:** 37
**Links Count:** 100
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# `cross_encoders`\#

**Cross encoders** are wrappers around cross encoder models from different APIs and     

services.

**Cross encoder models** can be LLMs or not.

**Class hierarchy:**               BaseCrossEncoder --> <name>CrossEncoder  # Examples: SagemakerEndpointCrossEncoder     

**Classes**

[`cross_encoders.fake.FakeCrossEncoder`](https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.fake.FakeCrossEncoder.html#langchain_community.cross_encoders.fake.FakeCrossEncoder "langchain_community.cross_encoders.fake.FakeCrossEncoder") | Fake cross encoder model.   ---|---   [`cross_encoders.huggingface.HuggingFaceCrossEncoder`](https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.huggingface.HuggingFaceCrossEncoder.html#langchain_community.cross_encoders.huggingface.HuggingFaceCrossEncoder "langchain_community.cross_encoders.huggingface.HuggingFaceCrossEncoder") | HuggingFace cross encoder models.   [`cross_encoders.sagemaker_endpoint.CrossEncoderContentHandler`](https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.sagemaker_endpoint.CrossEncoderContentHandler.html#langchain_community.cross_encoders.sagemaker_endpoint.CrossEncoderContentHandler "langchain_community.cross_encoders.sagemaker_endpoint.CrossEncoderContentHandler")\(\) | Content handler for CrossEncoder class.   [`cross_encoders.sagemaker_endpoint.SagemakerEndpointCrossEncoder`](https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.sagemaker_endpoint.SagemakerEndpointCrossEncoder.html#langchain_community.cross_encoders.sagemaker_endpoint.SagemakerEndpointCrossEncoder "langchain_community.cross_encoders.sagemaker_endpoint.SagemakerEndpointCrossEncoder") | SageMaker Inference CrossEncoder endpoint.