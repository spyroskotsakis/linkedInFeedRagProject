# AqaOutput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_genai/genai_aqa/langchain_google_genai.genai_aqa.AqaOutput.html
**Word Count:** 66
**Links Count:** 87
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# AqaOutput\#

_class _langchain\_google\_genai.genai\_aqa.AqaOutput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_genai/genai_aqa.html#AqaOutput)\#     

Bases: `BaseModel`

Output from GenAIAqa.invoke.

answer\#     

The answer to the user’s inquiry.

attributed\_passages\#     

A list of passages that the LLM used to construct the answer.

answerable\_probability\#     

The probability of the question being answered from the provided passages.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _answer _: str_ _\[Required\]_\#     

_param _answerable\_probability _: float_ _\[Required\]_\#     

_param _attributed\_passages _: List\[str\]__\[Required\]_\#     

__On this page