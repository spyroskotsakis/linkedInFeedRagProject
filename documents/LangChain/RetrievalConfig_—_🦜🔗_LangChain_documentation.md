# RetrievalConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.bedrock.RetrievalConfig.html
**Word Count:** 41
**Links Count:** 103
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# RetrievalConfig\#

_class _langchain\_aws.retrievers.bedrock.RetrievalConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/bedrock.html#RetrievalConfig)\#     

Bases: `BaseModel`

Configuration for retrieval.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _nextToken _: str | None_ _ = None_\#     

_param _vectorSearchConfiguration _: [VectorSearchConfig](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.bedrock.VectorSearchConfig.html#langchain_aws.retrievers.bedrock.VectorSearchConfig "langchain_aws.retrievers.bedrock.VectorSearchConfig")_ _\[Required\]_\#     

__On this page