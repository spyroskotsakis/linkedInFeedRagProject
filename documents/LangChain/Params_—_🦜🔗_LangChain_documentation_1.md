# Params — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.mlflow_ai_gateway.Params.html
**Word Count:** 50
**Links Count:** 290
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# Params\#

_class _langchain\_community.llms.mlflow\_ai\_gateway.Params[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/mlflow_ai_gateway.html#Params)\#     

Bases: `BaseModel`

Parameters for the MLflow AI Gateway LLM.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _candidate\_count _: int_ _ = 1_\#     

The number of candidates to return.

_param _max\_tokens _: int | None_ _ = None_\#     

_param _stop _: List\[str\] | None_ _ = None_\#     

_param _temperature _: float_ _ = 0.0_\#     

__On this page