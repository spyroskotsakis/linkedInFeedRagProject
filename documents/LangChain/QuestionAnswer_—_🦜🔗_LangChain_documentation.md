# QuestionAnswer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.QuestionAnswer.html
**Word Count:** 85
**Links Count:** 193
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# QuestionAnswer\#

_class _langchain.chains.openai\_functions.citation\_fuzzy\_match.QuestionAnswer[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/citation_fuzzy_match.html#QuestionAnswer)\#     

Bases: `BaseModel`

A question and its answer as a list of facts each one should have a source. each sentence contains a body and a list of sources.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _answer _: list\[[FactWithEvidence](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.FactWithEvidence.html#langchain.chains.openai_functions.citation_fuzzy_match.FactWithEvidence "langchain.chains.openai_functions.citation_fuzzy_match.FactWithEvidence")\]__\[Required\]_\#     

Body of the answer, each fact should be its separate object with a body and a list of sources

_param _question _: str_ _\[Required\]_\#     

Question that was asked

__On this page