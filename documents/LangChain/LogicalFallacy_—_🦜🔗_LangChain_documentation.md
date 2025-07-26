# LogicalFallacy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/fallacy_removal/langchain_experimental.fallacy_removal.models.LogicalFallacy.html
**Word Count:** 40
**Links Count:** 102
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# LogicalFallacy\#

_class _langchain\_experimental.fallacy\_removal.models.LogicalFallacy[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/fallacy_removal/models.html#LogicalFallacy)\#     

Bases: `BaseModel`

Logical fallacy.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _fallacy\_critique\_request _: str_ _\[Required\]_\#     

_param _fallacy\_revision\_request _: str_ _\[Required\]_\#     

_param _name _: str_ _ = 'Logical Fallacy'_\#     

__On this page