# Qa — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Qa.html
**Word Count:** 39
**Links Count:** 179
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# Qa\#

_class _langchain\_community.chains.pebblo\_retrieval.models.Qa[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#Qa)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _classifier\_location _: str_ _\[Required\]_\#     

_param _context _: List\[[Context](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Context.html#langchain_community.chains.pebblo_retrieval.models.Context "langchain_community.chains.pebblo_retrieval.models.Context") | None\] | [Context](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Context.html#langchain_community.chains.pebblo_retrieval.models.Context "langchain_community.chains.pebblo_retrieval.models.Context") | None_ _\[Required\]_\#     

_param _name _: str_ _\[Required\]_\#     

_param _prompt _: [Prompt](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Prompt.html#langchain_community.chains.pebblo_retrieval.models.Prompt "langchain_community.chains.pebblo_retrieval.models.Prompt") | None_ _\[Required\]_\#     

_param _prompt\_time _: str_ _\[Required\]_\#     

_param _response _: [Prompt](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Prompt.html#langchain_community.chains.pebblo_retrieval.models.Prompt "langchain_community.chains.pebblo_retrieval.models.Prompt") | None_ _\[Required\]_\#     

_param _user _: str_ _\[Required\]_\#     

_param _user\_identities _: List\[str\] | None_ _\[Required\]_\#     

__On this page