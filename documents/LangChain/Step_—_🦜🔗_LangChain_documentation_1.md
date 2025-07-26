# Step — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.Step.html
**Word Count:** 40
**Links Count:** 110
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# Step\#

_class _langchain\_experimental.plan\_and\_execute.schema.Step[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/schema.html#Step)\#     

Bases: `BaseModel`

Step.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _value _: str_ _\[Required\]_\#     

The value.

__On this page