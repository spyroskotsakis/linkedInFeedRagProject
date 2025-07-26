# Plan — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Plan.html
**Word Count:** 40
**Links Count:** 111
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# Plan\#

_class _langchain\_experimental.plan\_and\_execute.schema.Plan[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/schema.html#Plan)\#     

Bases: `BaseModel`

Plan.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _steps _: List\[[Step](https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Step.html#langchain_experimental.plan_and_execute.schema.Step "langchain_experimental.plan_and_execute.schema.Step")\]__\[Required\]_\#     

The steps.

__On this page