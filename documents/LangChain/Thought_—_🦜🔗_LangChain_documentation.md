# Thought — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html
**Word Count:** 43
**Links Count:** 115
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# Thought\#

_class _langchain\_experimental.tot.thought.Thought[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/thought.html#Thought)\#     

Bases: `BaseModel`

A thought in the ToT.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _children _: Set\[Thought\]__\[Optional\]_\#     

_param _text _: str_ _\[Required\]_\#     

_param _validity _: [ThoughtValidity](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.ThoughtValidity.html#langchain_experimental.tot.thought.ThoughtValidity "langchain_experimental.tot.thought.ThoughtValidity")_ _\[Required\]_\#     

__On this page