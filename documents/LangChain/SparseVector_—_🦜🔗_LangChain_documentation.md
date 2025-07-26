# SparseVector — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseVector.html
**Word Count:** 51
**Links Count:** 77
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# SparseVector\#

_class _langchain\_qdrant.sparse\_embeddings.SparseVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/sparse_embeddings.html#SparseVector)\#     

Bases: `BaseModel`

Sparse vector structure

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _indices _: list\[int\]__\[Required\]_\#     

indices must be unique

_param _values _: list\[float\]__\[Required\]_\#     

values and indices must be the same length

__On this page