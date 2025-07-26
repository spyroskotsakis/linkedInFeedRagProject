# ResultModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.ResultModel.html
**Word Count:** 43
**Links Count:** 111
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# ResultModel\#

_class _langchain\_experimental.cpal.models.ResultModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/cpal/models.html#ResultModel)\#     

Bases: `BaseModel`

Result of the story query.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _question _: str_ _\[Required\]__\(alias 'narrative\_input'\)_\#     

__On this page