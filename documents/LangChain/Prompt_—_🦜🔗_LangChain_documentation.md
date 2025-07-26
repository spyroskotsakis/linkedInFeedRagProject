# Prompt — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Prompt.html
**Word Count:** 39
**Links Count:** 167
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# Prompt\#

_class _langchain\_community.chains.pebblo\_retrieval.models.Prompt[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#Prompt)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _data _: list | str | None_ _\[Required\]_\#     

_param _entities _: dict | None_ _ = None_\#     

_param _entityCount _: int | None_ _ = None_\#     

_param _prompt\_gov\_enabled _: bool | None_ _ = None_\#     

__On this page