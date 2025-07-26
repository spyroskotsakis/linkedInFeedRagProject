# InterventionModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.InterventionModel.html
**Word Count:** 58
**Links Count:** 115
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# InterventionModel\#

_class _langchain\_experimental.cpal.models.InterventionModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/cpal/models.html#InterventionModel)\#     

Bases: `BaseModel`

Intervention data of the story aka initial conditions.               >>> intervention.dict()     {         entity_settings: [             {"name": "bud", "attribute": "pet_count", "value": 12},             {"name": "pat", "attribute": "pet_count", "value": 0},         ],         system_settings: None,     }     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _entity\_settings _: List\[[EntitySettingModel](https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.EntitySettingModel.html#langchain_experimental.cpal.models.EntitySettingModel "langchain_experimental.cpal.models.EntitySettingModel")\]__\[Required\]_\#     

_param _system\_settings _: List\[[SystemSettingModel](https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.SystemSettingModel.html#langchain_experimental.cpal.models.SystemSettingModel "langchain_experimental.cpal.models.SystemSettingModel")\] | None_ _ = None_\#     

__On this page