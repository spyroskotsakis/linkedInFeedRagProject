# VectorSearchConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.bedrock.VectorSearchConfig.html
**Word Count:** 42
**Links Count:** 105
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# VectorSearchConfig\#

_class _langchain\_aws.retrievers.bedrock.VectorSearchConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/bedrock.html#VectorSearchConfig)\#     

Bases: `BaseModel`

Configuration for vector search.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _filter _: [SearchFilter](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.bedrock.SearchFilter.html#langchain_aws.retrievers.bedrock.SearchFilter "langchain_aws.retrievers.bedrock.SearchFilter") | None_ _ = None_\#     

_param _numberOfResults _: int_ _ = 4_\#     

_param _overrideSearchType _: Literal\['HYBRID', 'SEMANTIC'\] | None_ _ = None_\#     

__On this page