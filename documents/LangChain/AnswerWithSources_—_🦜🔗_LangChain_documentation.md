# AnswerWithSources — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.qa_with_structure.AnswerWithSources.html
**Word Count:** 58
**Links Count:** 192
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# AnswerWithSources\#

_class _langchain.chains.openai\_functions.qa\_with\_structure.AnswerWithSources[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/qa_with_structure.html#AnswerWithSources)\#     

Bases: `BaseModel`

An answer to the question, with sources.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _answer _: str_ _\[Required\]_\#     

Answer to the question that was asked

_param _sources _: list\[str\]__\[Required\]_\#     

List of sources used to answer the question

__On this page