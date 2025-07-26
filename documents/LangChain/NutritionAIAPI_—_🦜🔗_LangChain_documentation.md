# NutritionAIAPI — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.passio_nutrition_ai.NutritionAIAPI.html
**Word Count:** 57
**Links Count:** 262
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# NutritionAIAPI\#

_class _langchain\_community.utilities.passio\_nutrition\_ai.NutritionAIAPI[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/passio_nutrition_ai.html#NutritionAIAPI)\#     

Bases: `BaseModel`

Wrapper for the Passio Nutrition AI API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _auth\__: [ManagedPassioLifeAuth](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.passio_nutrition_ai.ManagedPassioLifeAuth.html#langchain_community.utilities.passio_nutrition_ai.ManagedPassioLifeAuth "langchain_community.utilities.passio_nutrition_ai.ManagedPassioLifeAuth")_ _\[Required\]_\#     

_param _more\_kwargs _: dict_ _\[Optional\]_\#     

_param _nutritionai\_api\_url _: str_ _ = 'https://api.passiolife.com/v2/products/napi/food/search/advanced'_\#     

_param _nutritionai\_subscription\_key _: str_ _\[Required\]_\#     

run\(_query : str_\) → Dict | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/passio_nutrition_ai.html#NutritionAIAPI.run)\#     

Run query through NutrtitionAI API and parse result.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_ | None

Examples using NutritionAIAPI

  * [Passio NutritionAI](https://python.langchain.com/docs/integrations/tools/passio_nutrition_ai/)

__On this page