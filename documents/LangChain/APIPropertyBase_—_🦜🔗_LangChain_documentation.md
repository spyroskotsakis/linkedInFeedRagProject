# APIPropertyBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIPropertyBase.html
**Word Count:** 80
**Links Count:** 417
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# APIPropertyBase\#

_class _langchain\_community.tools.openapi.utils.api\_models.APIPropertyBase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIPropertyBase)\#     

Bases: `BaseModel`

Base model for an API property.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _default _: Any | None_ _ = None_\#     

The default value of the property.

_param _description _: str | None_ _ = None_\#     

The description of the property.

_param _name _: str_ _\[Required\]_\#     

The name of the property.

_param _required _: bool_ _\[Required\]_\#     

Whether the property is required.

_param _type _: SCHEMA\_TYPE_ _\[Required\]_\#     

The type of the property.

Either a primitive type, a component/parameter type, or an array or ‘object’ \(dict\) of the above.

__On this page