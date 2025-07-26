# SystemSettingModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.SystemSettingModel.html
**Word Count:** 49
**Links Count:** 113
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# SystemSettingModel\#

_class _langchain\_experimental.cpal.models.SystemSettingModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/cpal/models.html#SystemSettingModel)\#     

Bases: `BaseModel`

System initial conditions.

Initial global conditions for the system.

\{“parameter”: “interest\_rate”, “value”: .05\}

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _parameter _: str_ _\[Required\]_\#     

_param _value _: float_ _\[Required\]_\#     

__On this page