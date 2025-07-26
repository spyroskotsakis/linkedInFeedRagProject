# Framework — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Framework.html
**Word Count:** 47
**Links Count:** 253
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# Framework\#

_class _langchain\_community.utilities.pebblo.Framework[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#Framework)\#     

Bases: `BaseModel`

Pebblo Framework instance.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _name _: str_ _\[Required\]_\#     

Name of the Framework.

_param _version _: str_ _\[Required\]_\#     

Version of the Framework.

__On this page