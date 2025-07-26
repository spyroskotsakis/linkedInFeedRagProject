# UnstructuredRelation — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.llm.UnstructuredRelation.html
**Word Count:** 86
**Links Count:** 121
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# UnstructuredRelation\#

_class _langchain\_experimental.graph\_transformers.llm.UnstructuredRelation[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/llm.html#UnstructuredRelation)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _head _: str_ _\[Required\]_\#     

extracted head entity like Microsoft, Apple, John. Must use human-readable unique identifier.

_param _head\_type _: str_ _\[Required\]_\#     

type of the extracted head entity like Person, Company, etc

_param _relation _: str_ _\[Required\]_\#     

relation between the head and the tail entities

_param _tail _: str_ _\[Required\]_\#     

extracted tail entity like Microsoft, Apple, John. Must use human-readable unique identifier.

_param _tail\_type _: str_ _\[Required\]_\#     

type of the extracted tail entity like Person, Company, etc

__On this page