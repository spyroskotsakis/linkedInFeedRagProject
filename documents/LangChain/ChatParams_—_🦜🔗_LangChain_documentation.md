# ChatParams — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.javelin_ai_gateway.ChatParams.html
**Word Count:** 43
**Links Count:** 233
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# ChatParams\#

_class _langchain\_community.chat\_models.javelin\_ai\_gateway.ChatParams[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/javelin_ai_gateway.html#ChatParams)\#     

Bases: `BaseModel`

Parameters for the Javelin AI Gateway LLM.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _max\_tokens _: int | None_ _ = None_\#     

_param _stop _: List\[str\] | None_ _ = None_\#     

_param _temperature _: float_ _ = 0.0_\#     

__On this page