# EntityModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/cpal/langchain_experimental.cpal.models.EntityModel.html
**Word Count:** 47
**Links Count:** 117
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# EntityModel\#

_class _langchain\_experimental.cpal.models.EntityModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/cpal/models.html#EntityModel)\#     

Bases: `BaseModel`

Entity in the story.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _code _: str_ _\[Required\]_\#     

entity actions

_param _depends\_on _: List\[str\]__ = \[\]_\#     

ancestor entities

_param _name _: str_ _\[Required\]_\#     

entity name

_param _value _: float_ _\[Required\]_\#     

entity initial value

__On this page