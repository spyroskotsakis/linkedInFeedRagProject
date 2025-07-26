# CausalModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.CausalModel.html
**Word Count:** 49
**Links Count:** 114
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# CausalModel\#

_class _langchain\_experimental.cpal.models.CausalModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/cpal/models.html#CausalModel)\#     

Bases: `BaseModel`

Casual data.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _attribute _: str_ _\[Required\]_\#     

name of the attribute to be calculated

_param _entities _: List\[[EntityModel](https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.EntityModel.html#langchain_experimental.cpal.models.EntityModel "langchain_experimental.cpal.models.EntityModel")\]__\[Required\]_\#     

entities in the story

__On this page