# EntitySettingModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.EntitySettingModel.html
**Word Count:** 62
**Links Count:** 115
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# EntitySettingModel\#

_class _langchain\_experimental.cpal.models.EntitySettingModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/cpal/models.html#EntitySettingModel)\#     

Bases: `BaseModel`

Entity initial conditions.

Initial conditions for an entity

\{“name”: “bud”, “attribute”: “pet\_count”, “value”: 12\}

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _attribute _: str_ _\[Required\]_\#     

name of the attribute to be calculated

_param _name _: str_ _\[Required\]_\#     

name of the entity

_param _value _: float_ _\[Required\]_\#     

entity’s attribute value \(calculated\)

__On this page