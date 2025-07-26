# StepResponse — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/plan_and_execute/langchain_experimental.plan_and_execute.schema.StepResponse.html
**Word Count:** 41
**Links Count:** 110
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# StepResponse\#

_class _langchain\_experimental.plan\_and\_execute.schema.StepResponse[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/plan_and_execute/schema.html#StepResponse)\#     

Bases: `BaseModel`

Step response.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _response _: str_ _\[Required\]_\#     

The response.

__On this page