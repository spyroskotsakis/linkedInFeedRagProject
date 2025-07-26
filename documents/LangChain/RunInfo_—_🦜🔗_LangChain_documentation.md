# RunInfo — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.run_info.RunInfo.html
**Word Count:** 96
**Links Count:** 108
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# RunInfo\#

_class _langchain\_core.outputs.run\_info.RunInfo[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/outputs/run_info.html#RunInfo)\#     

Bases: `BaseModel`

Class that contains metadata for a single execution of a Chain or model.

Defined for backwards compatibility with older versions of langchain\_core.

This model will likely be deprecated in the future.

Users can acquire the run\_id information from callbacks or via run\_id information present in the astream\_event API \(depending on the use case\).

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _run\_id _: UUID_ _\[Required\]_\#     

A unique identifier for the model or chain run.

__On this page