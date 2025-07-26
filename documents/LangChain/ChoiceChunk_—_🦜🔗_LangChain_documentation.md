# ChoiceChunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.ChoiceChunk.html
**Word Count:** 40
**Links Count:** 112
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# ChoiceChunk\#

_class _langchain\_community.adapters.openai.ChoiceChunk[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#ChoiceChunk)\#     

Bases: [`IndexableBaseModel`](https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.IndexableBaseModel.html#langchain_community.adapters.openai.IndexableBaseModel "langchain_community.adapters.openai.IndexableBaseModel")

Choice chunk.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _delta _: dict_ _\[Required\]_\#     

__On this page