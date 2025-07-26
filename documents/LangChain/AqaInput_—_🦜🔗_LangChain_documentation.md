# AqaInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_genai/genai_aqa/langchain_google_genai.genai_aqa.AqaInput.html
**Word Count:** 56
**Links Count:** 83
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# AqaInput\#

_class _langchain\_google\_genai.genai\_aqa.AqaInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/genai_aqa.html#AqaInput)\#     

Bases: `BaseModel`

Input to GenAIAqa.invoke.

prompt\#     

The user’s inquiry.

source\_passages\#     

A list of passage that the LLM should use only to answer the user’s inquiry.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _prompt _: str_ _\[Required\]_\#     

_param _source\_passages _: List\[str\]__\[Required\]_\#     

__On this page