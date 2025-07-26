# SelectionScorer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.SelectionScorer.html
**Word Count:** 52
**Links Count:** 127
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# SelectionScorer\#

_class _langchain\_experimental.rl\_chain.base.SelectionScorer[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#SelectionScorer)\#     

Bases: `Generic`\[`TEvent`\], `ABC`, `BaseModel`

Abstract class to grade the chosen selection or the response of the llm.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_abstractmethod _score\_response\(

    _inputs : Dict\[str, Any\]_,     _llm\_response : str_,     _event : TEvent_, \) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#SelectionScorer.score_response)\#     

Parameters:     

  * **inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **llm\_response** \(_str_\)

  * **event** \(_TEvent_\)

Return type:     

float

__On this page