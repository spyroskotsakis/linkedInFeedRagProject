# FactWithEvidence — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.openai_functions.citation_fuzzy_match.FactWithEvidence.html
**Word Count:** 103
**Links Count:** 195
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# FactWithEvidence\#

_class _langchain.chains.openai\_functions.citation\_fuzzy\_match.FactWithEvidence[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/citation_fuzzy_match.html#FactWithEvidence)\#     

Bases: `BaseModel`

Class representing a single statement.

Each fact has a body and a list of sources. If there are multiple facts make sure to break them apart such that each one only uses a set of sources that are relevant to it.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _fact _: str_ _\[Required\]_\#     

Body of the sentence, as part of a response

_param _substring\_quote _: list\[str\]__\[Required\]_\#     

Each source should be a direct quote from the context, as a substring of the original content

get\_spans\(

    _context : str_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/openai_functions/citation_fuzzy_match.html#FactWithEvidence.get_spans)\#     

Parameters:     

**context** \(_str_\)

Return type:     

_Iterator_\[str\]

__On this page