# Choice — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.Choice.html
**Word Count:** 39
**Links Count:** 112
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# Choice\#

_class _langchain\_community.adapters.openai.Choice[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#Choice)\#     

Bases: [`IndexableBaseModel`](https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.IndexableBaseModel.html#langchain_community.adapters.openai.IndexableBaseModel "langchain_community.adapters.openai.IndexableBaseModel")

Choice.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _message _: dict_ _\[Required\]_\#     

__On this page