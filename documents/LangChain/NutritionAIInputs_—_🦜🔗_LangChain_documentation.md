# NutritionAIInputs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.passio_nutrition_ai.tool.NutritionAIInputs.html
**Word Count:** 57
**Links Count:** 409
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# NutritionAIInputs\#

_class _langchain\_community.tools.passio\_nutrition\_ai.tool.NutritionAIInputs[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/passio_nutrition_ai/tool.html#NutritionAIInputs)\#     

Bases: `BaseModel`

Inputs to the Passio Nutrition AI tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

A query to look up using Passio Nutrition AI, usually a few words.

__On this page