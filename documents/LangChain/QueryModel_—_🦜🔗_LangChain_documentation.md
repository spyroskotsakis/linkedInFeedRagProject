# QueryModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.QueryModel.html
**Word Count:** 53
**Links Count:** 115
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# QueryModel\#

_class _langchain\_experimental.cpal.models.QueryModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/cpal/models.html#QueryModel)\#     

Bases: `BaseModel`

Query data of the story.

translate a question about the story outcome into a programmatic expression

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _expression _: str_ _\[Required\]_\#     

_param _llm\_error\_msg _: str_ _\[Required\]_\#     

_param _question _: str_ _\[Required\]__\(alias 'narrative\_input'\)_\#     

__On this page